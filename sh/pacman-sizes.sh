#!/bin/sh

pacman -Qi | grep -E '^(Name|Installed)' | cut -f2 -d':' | paste -d" " - - | sed 's/ \(\w\)/\1/g' | sort -hk 2
