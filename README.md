# Note: In development - consider the below a roadmap

# kali0conf
## Intro
Auto setup i3 desktop environment for kali linux live cd, as an alternative to customizing the iso.

Created to stop wasting time installing the same apps over and over and getting rid of of that 
awful live cd feeling. It should be easy to port to any debian based live cd.
  
Simply wget the setup.sh file and run [insert tiny url link here] or
[insert raw github link here]. 

## What it does
0. Select config bundle (see screenshots in config folder)
3. download config bundle: 
  - wallpaper, 
  - .i3 config
  - misc dotfiles (e.g. .fonts/, .zshrc, .vimrc, aliases, ..)
  - firefox addon list (e.g. noscript, tamper data, ublock origin, HackBar, REST Easy, HTTPS Everywhere, JavaScript Deobfuscator, ..),
  - firefox bookmark list
  - application install list (e.g. feh, ncdu, htop, alpine, iptraf, mc, irssi, atop, ..)
  - application remove list (e.g. , ..)
1. grep: check if we are in a virtualbox environment 
1. apt-get: install virtualbox guest addons
2. apt-get: uninstall redundant apps of current desktop environment [uninstall list]
3. apt-get: install i3-wm, i3-lock, i3-bar, dwm-tools, suckless-tools and [install list]
4. gksudo firefox -install-global-extension: install [firefox addon list]
5. sqlite: create firefox bookmarks 
5. passwd: change the root password
4. useradd: create non-root user 
5. passwd: set the non-root user password 
5. mv: move i3 configs, dotfiles to the user's home directory 
4. .... todo .....
8. logout

Finally login and enjoy your brand new i3 environment
