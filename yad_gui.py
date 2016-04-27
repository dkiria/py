#! /bin/bash

# some defaults
user="root"
suargs="-p"
force="no"

# parse commandline   
if [[ $# -eq 0 ]]; then
    echo "Usage: ${0##*/} [-f] [-u user] [--] "
    exit 1
fi

OPTIND=1
while getopts u: opt; do
    case "$opt" in
        f) force="yes" ;;
        u) user="$OPTARG" ;;
    esac
done
shift $((OPTIND - 1))

cmd="$*"

if [[ $force != "no" ]]; then
    # check for sudo
    sudo_check=$(sudo -H -S -- echo SUDO_OK 2>&1 &)
    if [[ $sudo_check == "SUDO_OK" ]]; then
        eval sudo $cmd
        exit $?
    fi
fi

# get password
pass=$(yad --class="GSu" \
    --title="Password" \
    --text="Enter password for user <b>$user</b>:" \
    --image="dialog-password" \
    --entry --hide-text)
[[ -z "$pass" ]] && exit 1



echo $pass > test.txt
