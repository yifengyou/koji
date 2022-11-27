#!/bin/bash -u
#
# Might want to drop this in ~/bin/ and chmod u+x it
#

#####################################################################
usage() {
    echo ''                                               >&2
    echo "$0 [-hrcq] [-b branch]"                         >&2
    echo ''                                               >&2
    echo ' Finds all possible srpms for a given repo'     >&2
    echo ' based on the commit log'                       >&2
    echo ''                                               >&2
    echo 'You need to run this from inside a sources git repo' >&2
    echo ''                                               >&2
    echo ' -h: This help message'                         >&2
    echo ' -r: Use the Redhat commits only'               >&2
    echo ' -c: Return in sha:srpm format'                 >&2
    echo ' -q: Suppress warnings'                         >&2
    echo ''                                               >&2
    echo ' -b: specify a branch to examine'               >&2
    echo "     defaults to repo's current branch"         >&2
    echo ''                                               >&2
    echo "  $0"                                           >&2
    echo "  $0 -b c7"                                     >&2
    echo "  $0 -r -b c7"                                  >&2
    echo "  $0 -c -b remotes/origin/c7"                   >&2
    echo "  $0 -c -r -b remotes/origin/c7"                >&2
    exit 1
}

#####################################################################
warn () {
    [[ ${QUIET} -eq 1 ]] && return
    echo 1>&2 "$@"
}

#####################################################################

RHELAUTHOR="CentOS Buildsys <bugs@centos.org>"

RHELONLY=0
QUIET=0
WITHCOMMITHASH=0
BRANCH=""

# for setting any overrides, such as RHELAUTHOR or default BRANCH
if [ -f /etc/centos-git-common ]; then
  . /etc/centos-git-common
fi

#####################################################################
# setup args in the right order for making getopt evaluation
# nice and easy.  You'll need to read the manpages for more info
# utilizing 'while' construct rather than 'for arg' to avoid unnecessary
# shifting of program args
args=$(getopt -o hrcqb: -- "$@")
eval set -- "$args"

while [[ 0 -eq 0 ]]; do
    case $1 in
        -- )
            # end of getopt args, shift off the -- and get out of the loop
            shift
            break
           ;;
         -r )
            # Only look at commits by RHEL
            RHELONLY=1
            shift
           ;;
         -c )
            # return with the commit hash as a prefix of the resulting srpm
            WITHCOMMITHASH=1
            shift
           ;;
         -q )
            # suppress warnings
            QUIET=1
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

# commit message contains white space, set IFS to \n
IFS='
'

LOGARGS="--pretty=%H|\%s"
if [[ ${RHELONLY} -eq 1 ]]; then
    LOGARGS="${LOGARGS} --author='${RHELAUTHOR}'"
fi

if [[ "x${BRANCH}" != 'x' ]]; then
    LOGARGS="${LOGARGS} ${BRANCH}"
fi

loglist=$(git log ${LOGARGS} |grep import)
if [[ $? -ne 0 ]]; then
    exit 1
fi

# flag for if nothing is found
FOUND=False
for entry in $loglist; do
    FOUND=True

    pkg=$(echo ${entry} | cut -d' ' -f2)
    # strip .src.rpm if present
    nvr="${pkg%.src.rpm}"
    if [[ ${WITHCOMMITHASH} -eq 1 ]]; then
        shasum=$(echo ${entry} | cut -d'|' -f1)
        echo "${shasum}:${nvr}.src.rpm"
    else
        echo "${nvr}.src.rpm"
    fi
done

if [ "${FOUND}" != "True" ]
then
    warn "No SRPMs found"
fi

