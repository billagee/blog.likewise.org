---
layout: post
title: "Raspberry Pi terminal screenshots with fbgrab"
date: 2013-01-13 11:26
comments: true
categories: 
---

Say you're on the console on your Raspberry Pi, and you want to take a screenshot. But without X running, what does one do?

Simple: Use fbgrab. To install it, just:

<pre>sudo apt-get install fbgrab</pre>

Pass fbgrab the name of the virtual terminal/tty you want to snapshot, and it'll spit out a PNG file.

For example, say you have an awesome console program running on /dev/tty1, and want to screenshot it - just run:

<pre>sudo fbgrab -c 1 screenshot.png</pre>

And that's it! Here's an example of the output:

{% img /images/screenshot.png 'cmus screenshot' %}


