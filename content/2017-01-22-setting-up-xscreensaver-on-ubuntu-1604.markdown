Title: Setting up XScreenSaver on Ubuntu 16.04
Date: 2017-01-22 19:00
Tags: Ubuntu, XScreenSaver
Slug: setting-up-xscreensaver-on-ubuntu-1604

[comment]: <>  ( ![xscreensaver-config screenshot]({attach}images/xscreensaver-config.png){:height="36px" width="36px"} )

![xscreensaver-config screenshot]({attach}images/xscreensaver-config.png){:height="60%" width="60%"}

Do you have a burning desire (or a mandatory policy) to make your Ubuntu machine lock its display when you step away?

Or do you have a fondness (maybe a _burn-in_ desire?) for a time when screensavers had other uses?

If so, this post describes how I installed XScreenSaver (and optional-but-essential add-ons like the <a target="_blank" href="https://www.youtube.com/watch?v=Q54NVuxhGso">CompanionCube screensaver</a>) on Ubuntu 16.04.

Here's the apt-get command I use to kick things off:

```
sudo apt-get install \
  xscreensaver xscreensaver-data-extra \
  xscreensaver-gl xscreensaver-gl-extra
```

Once the install is complete, here's how I run the config util to pick the list of screensavers to run (among other settings):

```
xscreensaver-demo
```

If you're ever curious what other optional packages exist, search with:

```
apt-cache search xscreensaver
```

And read <a target="_blank" href="https://www.jwz.org/xscreensaver/man1.html">the XScreenSaver manpage</a> for more info!

For my own reference, these are the screensavers I currently have enabled in my config file (```/home/bill/.xscreensaver```):

```
bill@foo:~$ cat /home/bill/.xscreensaver | grep "^  GL"
  GL: 				lament -root -fps			   \n\
  GL: 				sonar -root				   \n\
  GL: 				stairs -root				   \n\
  GL: 				sierpinski3d -root			   \n\
  GL: 				molecule -root				   \n\
  GL: 				glmatrix -root				   \n\
  GL: 				polyhedra -root				   \n\
  GL: 				tangram -root				   \n\
  GL: 				topblock -root				   \n\
  GL: 				companioncube -root -count 9		   \n\
  GL: 				kaleidocycle -root			   \n\
  GL: 				unknownpleasures -root			   \n\
  GL: 				splitflap -root				   \n\
```
