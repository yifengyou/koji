#!/bin/bash -u
#
# Extracts what appears to be the value of %{dist} from the commit message
#
# Might want to drop this in ~/bin/ and chmod u+x it

#####################################################################
usage() {
    echo ''                                               >&2
    echo "$0 [-hr]"                                       >&2
    echo ''                                               >&2
    echo ' -h: This help message'                         >&2
    echo ' -r: Use the Redhat tag rather than centos tag' >&2
    echo ' -q: Suppress warnings'                         >&2
    echo ''                                               >&2
    echo '  Attempt to extract what appears to be the value of %{dist}' >&2
    echo '  from the git.centos.org commit message'       >&2
    exit 1
}

#####################################################################
build_with_dist_scl() {
    SPECFILE=$1
    DIST=$2
    SCL=${3:-}

    if [[ "x${SCL}" == 'x' ]]; then
        result=$(rpm --define "%_topdir `pwd`" --define "dist ${DIST}" -q --specfile "${SPECFILE}" --qf '%{n}-%{v}-%{r}\n' 2>/dev/null | head -n 1)
    else
        result=$(rpm --define "%_topdir `pwd`" --define "dist ${DIST}" --define "scl ${SCL}" -q --specfile "${SPECFILE}" --qf '%{n}-%{v}-%{r}\n' 2>/dev/null | head -n 1)
    fi

    echo ${result}
}

#####################################################################
# setup args in the right order for making getopt evaluation
# nice and easy.  You'll need to read the manpages for more info
args=$(getopt -o hrq -- "$@")
if [[ $? -ne 0 ]]; then
    usage
fi
eval set -- "$args"

RHELTAG=0
QUIET=0
for arg in "$@"; do
    case $1 in
        -- )
            # end of getopt args, shift off the -- and get out of the loop
            shift
            break 2
           ;;
         -r )
            # skip any package with 'centos' in the dist area
            RHELTAG=1
           ;;
         -q )
            # suppress warnings
            QUIET=1
           ;;
         -h )
            # get help
            usage
           ;;
    esac
done

warn () {
    [[ ${QUIET} -eq 1 ]] && return
    echo 1>&2 "$@"
}

if [[ ! -d .git ]] || [[ ! -d SPECS ]]; then
    echo 'You need to run this from inside a sources git repo' >&2
    exit 1
fi

rpm -q scl-utils-build >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo 'Without scl-utils-build some SCL style sources be parsed' >&2
    exit 1
fi

# check metadata file and extract package name
packagename=""
shopt -s nullglob
set -- .*.metadata
if (( $# == 0 ))
then
    echo 'Missing metadata. Please run from inside a sources git repo' >&2
    exit 1
elif (( $# > 1 ))
then
    warn "Warning: multiple metadata files found. Using $1"
fi
meta=$1
pn=${meta%.metadata}
pn=${pn#.}

filter () {
    # filter used for log messages
    if [[ ${RHELTAG} -eq 1 ]]
    then
        grep -v centos | grep import
    else
        grep import
    fi
}

# extract nvr from commit message of last import
msg=$(git log --pretty=format:"%s" | filter | head -n 1)
set -- $msg
pkg="$2"

# strip .src.rpm if present
git_nvr="${pkg%.src.rpm}"

scl=''

SPEC=$(cd SPECS; ls *.spec)

#now get nvr from spec with placeholder dist
mydist="XXXjsdf9ur7qlkasdh4gygXXX"
test_nvr=$(build_with_dist_scl "SPECS/${SPEC}" ${mydist})

test_nodist=$(echo ${test_nvr} | sed -e 's/-[a-zA-Z0-9\.]*$//')
git_nodist=$(echo ${git_nvr} | sed -e 's/-[a-zA-Z0-9\._]*$//')

if [[ "${git_nodist}" != "${test_nodist}" ]]; then
    warn "Warning: ${git_nvr} != ${test_nvr}"
    warn "Warning: Trying as a Software Collection"
    scl=$(echo ${git_nodist} |sed -e "s/-${test_nodist}//")
    test_nvr=$(build_with_dist_scl "SPECS/${SPEC}" ${mydist} ${scl})
    test_nodist=$(echo ${test_nvr} | sed -e 's/-[a-zA-Z0-9\.]*$//')
fi

if [[ "${git_nodist}" != "${test_nodist}" ]]; then
    git_name=$(echo ${git_nvr} | cut -d '-' -f 1)
    test_name=$(echo ${test_nvr} | cut -d '-' -f 1)
    warn "Warning: ${git_name} != ${test_name}"
    echo "Warning: Couldn't match srpm name" >&2
    exit 1
fi

#use our placeholder dist to split the nvr
head=${test_nvr%$mydist*}

if [ ".$head" = ".$test_nvr" ]
then
    #no dist tag
    echo ""
    exit
fi

tail=${test_nvr#*$mydist}

frag=${git_nvr#$head}
dist=${frag%$tail}

# sanity check
if [[ "x${scl}" == 'x' ]]; then
    verifynvr=$(build_with_dist_scl "SPECS/${SPEC}" ${dist})
else
    verifynvr=$(build_with_dist_scl "SPECS/${SPEC}" ${dist} ${scl})
fi

if [ ".$verifynvr" != ".$git_nvr" ]
then
    warn "Warning: $verifynvr != $git_nvr"
    warn "Warning: check failed. The %{dist} value may be incorrect"
fi

echo "$dist"
