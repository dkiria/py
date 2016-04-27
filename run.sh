#! /bin/bash
#./sudo_install.sh

action=$(yad --width 500 --height 100 --entry --title "command app" \
    --image=gnome-start \
    --button="Switch User:2" \
    --button="gtk-ok:0" --button="gtk-close:1" \
    --text "Choose action:" \
    --entry-text \
    "ls" "ping" "Reboot" "Suspend" "Logout" "ps" "df"  "ifconfig " )
ret=$?

[[ $ret -eq 1 ]] && exit 10

if [[ $ret -eq 2 ]]; then
    gdmflexiserver --startnew &
    exit 0
fi
case $action in
    	ifconfig*) cmd="ifconfig" ;;
	ping*) cmd="./tester.py ping" ;;
    	ls*) cmd="ls" ;;
   	ps*) cmd="ps" ;;
    	df*) cmd="df" ;;
    	Reboot*) cmd="sudo /sbin/reboot" ;;
    	Suspend*) cmd="sudo /bin/sh -c 'echo disk > /sys/power/state'" ;;
    	Logout*) 
    	case $(wmctrl -m | grep Name) in
        	*Openbox) cmd="openbox --exit" ;;
        	*FVWM) cmd="FvwmCommand Quit" ;;
            	*Metacity) cmd="gnome-save-session --kill" ;; 
        	*) exit 1 ;;
    	esac
    	;;
    	*) exit 20 ;;    
	esac

eval exec $cmd
