#!/bin/sh
x11vnc -passwd "$1" -display :0 -auth `ps aux | grep Xorg | sed -n -e 's/^.*-auth //p'`
