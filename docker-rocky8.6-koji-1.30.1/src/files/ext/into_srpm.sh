#!/bin/bash -u
#
# Turn a centos git repo into a .src.rpm file
#
# Might want to drop this in ~/bin/ and chmod u+x it

#
#  License: GPLv2
#
#  Initial Author: Pat Riehecky <riehecky at fnal.gov>
#

#####################################################################
usage() {
    echo ''                                               >&2
    echo "$0 [-hqts] [-d dist] [-b branch] [-c shasum]"   >&2
    echo ''                                               >&2
    echo 'You need to run this from inside a sources git repo' >&2
    echo ''                                               >&2
    echo ' -h: This help message'                         >&2
    echo ' -q: Suppress warnings'                         >&2
    echo ' -t: Set srpm timestamp to commit date'         >&2
    echo ' -s: Allow building as a SCL style package'     >&2
    echo ''                                               >&2
    echo ' -d: Use this %{dist} instead of automatic value'>&2
    echo ''                                               >&2
    echo ' -b: specify a branch to examine'               >&2
    echo "     defaults to repo's current branch"         >&2
    echo "     NOTE: your repo will be set to this branch">&2
    echo ''                                               >&2
    echo ' -c: specify a commit id'                       >&2
    echo "     defaults to repo's current commit id"      >&2
    echo "     NOTE: your repo will be set to this commit">&2
    echo ''                                               >&2
    echo "  $0"                                           >&2
    echo "  $0 -b c7 -t"                                  >&2
    echo "  $0 -b c7 -s"                                  >&2
    echo "  $0 -b c7 -d yourdisthere"                     >&2
    echo "  $0 -b remotes/origin/c7"                      >&2
    echo "  $0 -c 865ae5909b2b5d5fb37971b7ad7960f1fd5a5ffa" >&2
    echo "  $0 -b c7 -c 865ae5909b2b5d5fb37971b7ad7960f1fd5a5ffa" >&2
    exit 1
}

#####################################################################

QUIET=0
KEEPTIMESTAMP=0
ALLOWSCL=0
COMMITHASH=""
BRANCH=""
DIST=''

#####################################################################
# setup args in the right order for making getopt evaluation
# nice and easy.  You'll need to read the manpages for more info
# utilizing 'while' construct rather than 'for arg' to avoid unnecessary
# shifting of program args
args=$(getopt -o htsqb:c:d: -- "$@")
eval set -- "$args"

while [[ 0 -eq 0 ]]; do
    case $1 in
        -- )
            # end of getopt args, shift off the -- and get out of the loop
            shift
            break
           ;;
         -t )
            # keep timestamps of commit on srpm
            KEEPTIMESTAMP=1
            shift
           ;;
         -q )
            # suppress warnings
            QUIET=1
            shift
           ;;
         -s )
            # try to detect if this was an SCL and build as such
            ALLOWSCL=1
            shift
           ;;
         -d )
            # Set %{dist} to this instead the automatic value
            DIST=$2
            shift
            shift
           ;;
         -c )
            # Use this commit id
            COMMITHASH=$2
            shift
            shift
           ;;
         -b )
            # Check this particular branch 
            BRANCH=$2
            shift
            shift
           ;;
         -h )
            # get help
            usage
           ;;
    esac
done

if [[ ! -d .git ]] || [[ ! -d SPECS ]]; then
    echo 'You need to run this from inside a sources git repo' >&2
    exit 1
fi

which git >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo 'You need git in PATH' >&2
    exit 1
fi

which get_sources.sh >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo 'You need get_sources.sh from centos-git-common in PATH' >&2
    exit 1
fi

which return_disttag.sh >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo 'You need return_disttag.sh from centos-git-common in PATH' >&2
    exit 1
fi

which show_possible_srpms.sh >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo 'You need show_possible_srpms.sh from centos-git-common in PATH' >&2
    exit 1
fi

if [[ ${ALLOWSCL} -eq 1 ]]; then
    rpm -q scl-utils-build >/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo 'Without scl-utils-build some SCL style sources be parsed' >&2
        exit 1
    fi
fi

# Set us to requested branch for further operations
if [[ "x${BRANCH}" != 'x' ]]; then
    if [[ $QUIET -eq 1 ]]; then
        git fetch >/dev/null
        git checkout ${BRANCH} >/dev/null
    else
        git fetch
        git checkout ${BRANCH}
    fi
fi

# Set us to requested commit for further operations
if [[ "x${COMMITHASH}" != 'x' ]]; then
    if [[ $QUIET -eq 1 ]]; then
        git fetch >/dev/null
        git checkout ${COMMITHASH} >/dev/null
    else
        git fetch
        git checkout ${COMMITHASH}
    fi
fi

# Download archive from git.centos.org
if [[ $QUIET -eq 1 ]]; then
    get_sources.sh
else
    get_sources.sh -q
fi

SPECFILE=$(cd SPECS; ls *.spec)

# determine automatically unless we've got one set
if [[ "x${DIST}" == 'x' ]]; then
    if [[ ${QUIET} -eq 1 ]]; then
        DIST=$(return_disttag.sh -q)
    else
        DIST=$(return_disttag.sh)
    fi
fi

# Determine if we are an SCL
ISSCL=0
if [[ ${ALLOWSCL} -eq 1 ]]; then
    mytestsclname='DA39A3EE5E6B4B0D3255BFEF95601890AFD80709'
    mysclcheck=$(rpm --define "dist ${DIST}" --define "scl ${mytestsclname}" -q --specfile "SPECS/${SPECFILE}" --qf '%{n}-%{v}-%{r}\n' 2>/dev/null | head -n 1)
    echo ${mysclcheck} | grep -q ${mytestsclname}
    if [[ $? -eq 0 ]]; then
        ISSCL=1
        BASENAME=$(echo ${mysclcheck} | sed -e 's/DA39A3EE5E6B4B0D3255BFEF95601890AFD80709//')
        RPMNAME=$(show_possible_srpms.sh | head -1)
        SCLNAME=$(echo ${RPMNAME} | sed -e "s/${BASENAME}.src.rpm//")
        if [[ $(echo ${SCLNAME} | wc -l) -ne 1 ]]; then
            echo "$0 failed to determine unique SCL name" >&2
            echo "Found:"                                 >&2
            echo "${SCLNAME}"                             >&2
        fi

        scl_check=$(rpm --define "dist ${DIST}" --define "scl ${SCLNAME}" -q --specfile "SPECS/${SPECFILE}" --qf '%{n}-%{v}-%{r}.src.rpm\n' 2>/dev/null | head -n 1)
        if [[ "${RPMNAME}" != "${scl_check}" ]]; then
            echo "$0 failed to verify SCL name" >&2
            echo "Found:"                       >&2
            echo "${SCLNAME}"                   >&2
            echo "made:     ${scl_check}"       >&2
            echo "expected: ${RPMNAME}"         >&2
        fi
    fi
fi

# build our rpmopts list
RPMOPTS="-bs --nodeps"

# put it all together
if [[ ${ISSCL} -eq 1 ]]; then
    rpmbuild --define "%_topdir `pwd`" ${RPMOPTS} --define "%dist ${DIST}" --define "%scl ${SCLNAME}" SPECS/${SPECFILE}
    RC=$?
else
    rpmbuild --define "%_topdir `pwd`" ${RPMOPTS} --define "%dist ${DIST}" SPECS/${SPECFILE}
    RC=$?
fi

if [[ ${KEEPTIMESTAMP} -eq 1 ]]; then
    timestamp=$(git log --pretty=%ai -1)
    find . -type f -name \*.src.rpm -exec touch -d "${timestamp}" {} \;
fi

if [[ ${RC} -ne 0 ]]; then
    if [[ ${QUIET} -eq 1 ]]; then
        echo "$0 failed to recreate srpm" >&2
    fi
    exit 1
fi
