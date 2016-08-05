---
layout: post
title: "Using TextMate to rapidly test Java code examples/SSCCEs"
date: 2013-04-14 11:26
comments: true
categories: 
---
My last post was about executing small Java programs from within vim, without leaving the editor to manually open a shell.

The goal was to rapidly execute example code for your own edification, or when showing code to other people - basically any time you need a <a href="http://sscce.org/">Short, Self Contained, Correct (Compilable), Example</a> (also known as an SSCCE).

While vim does indeed work for that purpose, I feel <a href="http://macromates.com/">TextMate</a> has the edge when it comes to running Java examples.

Here's what setting up and using TextMate to run Java programs on a Mac looks like:

- After you install TextMate, open the Bundle settings (in 'TextMate > Preferences > Bundles') and make sure the 'Java' checkbox is set:

{% img /images/textmate/java-bundle.png 'textmate bundle dialog' %}

- Open or compose your demo program, and make sure you've saved the file to disk.

- In the bottom status bar, Make sure the Java bundle is selected:

{% img /images/textmate/java-status-bar.png 'textmate status bar with Java' %}

- Now simply use Command-R to run your code! A new window should open to display the output.

{% img /images/textmate/java-output.png 'textmate Java output' %}


