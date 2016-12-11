# kali0conf
## Intro
Auto setup i3 desktop environment for kali linux live cd - as an alternative to customizing the iso.
Simply wget the setup.sh file and run [insert tiny url link here] or
[insert raw github link here]. 

## What it does
0.  passwd: you should change the root password
1a. grep: verify if we are in a virtualbox environment 
1b. apt-get: install virtualbox guest addons
2a. grep: identify current desktop environment 
2b. apt-get: uninstall desktop environment
3a. apt-get: install i3-vm, feh, 
3b. wget: fetch wallpaper from unsplash.com
3c. feh: set desktop wallpaper
3d. wget: .i3 files, .font directory, .zshrc, .vimrc, .compton.conf
4a. useradd: create non-root user 
..... todo .....
n-1. logout root and login as non-root user in a brand new i3 environment
