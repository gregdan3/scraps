#!/bin/bash
pacman -Qqi | awk '/^Name/{name=$3} /^Installed Size/{print $4$5, name}' | sort -h
