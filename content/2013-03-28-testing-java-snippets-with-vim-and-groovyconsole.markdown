---
layout: post
title: "Testing Java snippets with Vim and GroovyConsole"
date: 2013-03-28 07:54
comments: true
categories: 
---

For instructional purposes (either when experimenting on your own, or when demonstrating code to others) it's always useful to be able to run snippets of code in a <a href="http://en.wikipedia.org/wiki/REPL">REPL</a>, or a similar environment allowing fast turnaround in the edit/compile/run cycle.

When using Java, the customary IDEs offer ways to get REPL-like behavior, but what if you don't want to use a traditional Java IDE?

Perhaps you just want to demonstrate a trivial bit of code without much overhead.

In that situation, a couple of nice options for Java are:

- Use GroovyConsole as a Java REPL
- Edit your code in Vim, and compile and run it without leaving the editor

### 1.  Using GroovyConsole

If you're on a Mac, GroovyConsole can be installed via the homebrew groovy formula (or, just get it from <a href="http://groovy.codehaus.org">http://groovy.codehaus.org</a>):

<pre>brew install groovy</pre>

Launch GroovyConsole with this command:

<pre>groovyConsole</pre>

Then simply type in a code snippet and run it with &lt;Command-R&gt; (or on Windows, &lt;CTRL-R&gt;):

{% img /images/groovyConsole.png 'groovyConsole screenshot' %}

### 2.  Using Vim as an improvised Java IDE

<div style="float: left; width: 100%;">
{% img right /images/vim/foo-dot-java.png 'foo dot java' %}
First, launch vim and write a small program - for example, Foo.java:
</div>
<div style="float: left; width: 100%;">
{% img right /images/vim/foo-javac.png 'running javac from vim' %}
Then, compile your program without leaving vim by passing the file open in your vim buffer to javac, using the <tt>:!</tt> command sequence and <tt>%</tt>
</div>
<div style="float: left; width: 100%;">
{% img right /images/vim/foo-enter-to-continue.png 'ENTER prompt from vim' %}
If all goes well, you'll temporarily be dropped to the shell, with no visible errors, and get prompted to press ENTER to continue back to vim:
</div>
<div style="float: left; width: 100%;">
{% img right /images/vim/java-foo.png 'running Foo.class in java' %}
Back in the editor, use <tt>:!java Foo</tt> to invoke the Java class file you just created with javac:
</div>
<div style="float: left; width: 100%;">
{% img right /images/vim/output.png 'Foo.class output' %}
Finally, you'll see your program's output in the console.
</div>

For further fun, try compiling with <tt>javac -g %</tt>, then launch your class file with <tt>jdb Foo</tt> to debug your program from within vim.

Also, you might consider taking the <a href="http://www.vim.org/scripts/script.php?script_id=1785">javacomplete omni-completion plugin</a> for a spin.

