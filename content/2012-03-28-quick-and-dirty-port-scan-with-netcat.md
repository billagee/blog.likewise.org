---
layout: post
title: "Quick and dirty port scan with netcat"
date: 2012-03-28T22:01:00-07:00
categories:
 - netcat
 - perl
---

<div class='post'>
<a href="http://nc110.sourceforge.net/">netcat</a> (or "nc" on the command line) is a useful tool for many reasons.<br /><br />One common test automation task I've found it handy for is polling a port, waiting for a service to start responding.<br /><br />While there are many ways to do that, using nc could hardly be simpler.<br /><br />And it's easy to script - here's a short Perl snippet showing how to wrap nc to poll a port on a host:<br /><br /><script src="https://gist.github.com/2233382.js"> </script></div>
