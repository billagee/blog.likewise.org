Title: Debugging a JavaScript WebdriverIO project in Visual Studio Code
Date: 2017-02-19 19:00
Tags: JavaScript, WebdriverIO, VSCode, Selenium, WebDriver
Slug: debugging-a-javascript-webdriverio-project-in-vscode

![vscode loves webdriverio]({attach}images/vscode-heart-webdriverio.png){:height="50%" width="50%"}

When working on Selenium tests, do you appreciate a traditional IDE-based approach to debugging, with a GUI that lets you set breakpoints, step through your code line-by-line, inspect variables, and evaluate expressions on the fly?

Here's a .gif to illustrate what I mean:

![vscode-debug-gif]({attach}images/video/out.gif)

Have you also tried <a target="_blank" href="http://webdriver.io/">WebdriverIO</a> (the popular library for developing Selenium WebDriver test scenarios using Node.JS), but not yet come across a way to enjoy that type of debugging experience?

<a target="_blank" href="https://code.visualstudio.com/">Visual Studio Code</a> is a useful, lightweight, open-source IDE with support for debugging Node.JS apps.

And it allows you to interactively debug WebdriverIO code. So, in this post I'll document how to configure VS Code as your one-stop-shop for interactive WebdriverIO debugging!

We'll start from the beginning, installing each piece of software you need - and once that's complete, we'll build and debug a WebdriverIO test in the VS Code IDE.

Let's begin!

## Installing Java

Things will go more smoothly later if you first ensure you have `java` in your shell's PATH. WebdriverIO will expect it to be present so it can launch the Selenium standalone server (which is a Java app) for you.

So, install a JRE for your platform before going further (if you don't already have one).

The version I used when writing this tutorial was:

```
$ java -version
java version "1.8.0_05"
Java(TM) SE Runtime Environment (build 1.8.0_05-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.5-b02, mixed mode)
```

## Installing nvm and Node.JS

Both WebdriverIO and VS Code will expect you to provide your own installation of Node.JS. For that, you have a few choices:

* You can visit <a target="_blank" href="https://nodejs.org/">https://nodejs.org/</a> and download an installer.

* Mac folks can use Homebrew or MacPorts.

* Or, <a target="_blank" href="https://github.com/creationix/nvm">nvm</a> works great as well (it allows you to install multiple node versions).

For this tutorial, I'll be using nvm to install node 6, since as of this writing (early 2018) I encountered problems debugging with node 8.

Here's how I installed nvm (see <a target="_blank" href="https://github.com/creationix/nvm">the docs</a> for the latest instructions for this step):

```
# Install nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash

# Activate nvm without opening a new terminal
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

And to install node, I ran:

```
$ nvm install 6
```

The node and npm versions that gave me were:

```
$ node -v && npm -v
v6.12.3
3.10.10
```

That environment will be what I use for the rest of this tutorial.

## Creating a WebdriverIO Project

These steps are based on the developer guide at <a target="_blank" href="http://webdriver.io/guide.html">http://webdriver.io/guide.html</a>, with a few small changes.

```
# Create a new dir for your project, with a boilerplate package.json
mkdir webdriverio-test && \
  cd webdriverio-test && \
  npm init -y

# Install WebdriverIO, and tell npm to add it as a dependency in package.json
npm install webdriverio --save-dev
```

Now, run the WebdriverIO config helper:

```
./node_modules/.bin/wdio config
```

It'll prompt you for a series of questions - I accepted the defaults for each, EXCEPT the ```Do you want to add a service to your test setup?``` question.

For that one, select ```selenium-standalone```

Here's what my final settings resembled:

```
? Where do you want to execute your tests? On my local machine
? Which framework do you want to use? mocha
? Shall I install the framework adapter for you? Yes
? Where are your test specs located? ./test/specs/**/*.js
? Which reporter do you want to use?
? Do you want to add a service to your test setup?  selenium-standalone - https://github.com/webdriverio/wdio-selenium-standalone-service
? Shall I install the services for you? Yes
? Level of logging verbosity silent
? In which directory should screenshots gets saved if a command fails? ./errorShots/
? What is the base url? http://localhost
```

That will create ```wdio.conf.js``` in your current dir.

### Creating a test spec file

Now create the spec dir that the config utility asked about:

```
mkdir -p test/specs
```

Then create the file ```test/specs/foo.spec.js``` with these contents:

```
var assert = require('assert');
describe('webdriver.io page', function() {
    it('should have the right title - the fancy generator way', function () {
        // Tell mocha this test is allowed to run for 10 minutes, so we have
        // sufficient time for debugging.
        //
        // Note you can also set this globally in mochaOpts in wdio.conf.js:
        this.timeout(10 * 60 * 1000);

        browser.url('http://webdriver.io');
        var title = browser.getTitle();
        assert.equal(title, 'WebdriverIO - WebDriver bindings for Node.js');
    });
});
```

To see if all is well, run the following command to launch your test - you should see a browser launch, and eventually a passing result will be printed:

```
$ ./node_modules/.bin/wdio

․

1 passing (10.00s)
```

## Debugging with VS Code

If you haven't installed <a target="_blank" href="https://code.visualstudio.com/">VS Code</a> yet, please do so now :)

Once that's done, use the ```File > Open``` menu in VS Code to open the ```webdriverio-test``` directory you created earlier.

### User settings configuration

As of vscode 1.19.2, I had to add this to my settings.json file (which can be opened via the menu ```Code > Preferences > Settings```):

```
    "terminal.integrated.shellArgs.osx": [],
```

### launch.json configuration

Now, let's create a launch.json file and add a configuration for debugging your test spec.

To do that, click ```View > Debug``` or the debugging icon in the left of the IDE:

![vscode-debug-button]({attach}images/vscode/debug-button.png)

Then click the small gear in the debug menu to open launch.json:

![vscode-config-gear]({attach}images/vscode/config-gear.png)

Click Node.js in the menu that appears - this will open a boilerplate launch.json.

Delete the contents of launch.json, and insert the following text:

(UPDATED: Thanks to Wiktor Zychla for pointers on configuring the inspector protocol here! See his post at: http://www.wiktorzychla.com/2017/08/debugging-javascript-webdriver-io-in.html)

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "protocol": "inspector",
            "port": 5859,
            "address": "localhost",
            "name": "WebdriverIO",
            "timeout": 20000,
            "runtimeExecutable": "${workspaceRoot}/node_modules/.bin/wdio",
            "windows": {
                "runtimeExecutable": "${workspaceRoot}/node_modules/.bin/wdio.cmd"
            },
            "cwd": "${workspaceRoot}",
            "console": "integratedTerminal",
            // This args config runs only the file that's open and displayed
            // (e.g., a file in test/spec/):
            "args":[
                "--spec", "${relativeFile}"
                // To run a specific file, you can use:
                //"--spec", "test/specs/foo.spec.js"
            ]
        }
    ]
}
```

### Enable debugging in wdio.conf.js

Open ```wdio.conf.js``` in the editor.

Just under the ```exports.config = {``` line, add these lines:

```
    debug: true,
    execArgv: ['--inspect=127.0.0.1:5859'],
```

This allows VS Code to connect to the wdio runner for debugging.

If you forget this step, the first time you try to debug the IDE will likely show you the error message ```Cannot connect to runtime process```

### First run

Now it's time for action! Open the ```test/specs/foo.spec.js``` file in the IDE, making sure it's the active tab in the editor (so that the file name is plugged into the ```${relativeFile}``` in your debug config in ```launch.json```).

Now click the green play button next to DEBUG in the IDE. You should see your test run to completion, since no breakpoints are set.

![vscode-debug-play-button]({attach}images/vscode/debug-play-button.png)

### Setting a breakpoint

Now place a breakpoint in foo.spec.js, at line 11, by clicking the gutter to the left of the line number (you'll see a red dot appear).

Then press the debug button again and watch the IDE stop execution at line 11, as shown here:

![vscode-breakpoint-hit]({attach}images/vscode/breakpoint-hit.png)

Click the ```DEBUG CONSOLE``` menu, click the small prompt box at its bottom, and experiment with adding JS statements - for example:

```
browser.getTitle()
```

That should print the browser window's title as shown here:

![vscode-debug-console]({attach}images/vscode/debug-console.png)

Now try inspecting elements interactively with the ```$``` and ```$$``` WebdriverIO helpers - for example:

```
$$("div").length

$$("div")[3].getText()
```

Note that code completion works here! It comes in handy when guessing at the first few characters of functions you suspect might exist:

![vscode-debug-console-code-completion]({attach}images/vscode/debug-console-code-completion.png)

That's all for now!
