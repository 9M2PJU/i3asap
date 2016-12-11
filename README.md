# kali0conf
## Intro
Auto setup i3 desktop environment for kali linux live cd, as an alternative to customizing the iso.

After running kali0conf your system should no longer have that 
awful live cd feeling. 

It should be easily portable to any debian based live cd. 
  
Simply wget the setup.sh file and run [insert tiny url link here] or
[insert raw github link here]. 

## What it does
0. Select configs (see screenshots in config folder)
0. passwd: you should change the root password
1. grep: check if we are in a virtualbox environment 
1. apt-get: install virtualbox guest addons
2. grep: identify current desktop environment 
2. apt-get: uninstall redundant apps of desktop environment
3. apt-get: install i3-vm, dmenu, feh, ncdu, htop, alpine, iptraf, mc, irssi, atop, .. todo 
3. wget: fetch wallpaper from unsplash.com
3. wget: .i3 files, .font directory, .zshrc, .vimrc, .compton.conf, .xinitrc
4. useradd: create non-root user 
4. .... todo .....
4. logout root and login as non-root user in a brand new i3 environment
