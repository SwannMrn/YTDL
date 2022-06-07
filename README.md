# PyTube

## A YouTube Downloader based on JavaScript and HTML

### By Serguei V, Swann M, and Luis BLZ

### ToDo:

Written in the ***Project*** Tab (top right)

### How we did it

We made a local server (URL is ***localhost:5000***) using NodeJS, npm and Express (basically JavaScript).

In the files, there is ***app.js***, which launches and sends the files in the server for use and display.

***script.js*** is the file linked to the ***index.html*** file, which collects the YouTube link in the **text input**. 

Then, the link is used with the **ytdl-core** JavaScript module, which downloads the video on the server.

The JavaScript then creates an URL that downloads the video to the user's device.

The video is deleted once the console is closed/the server is closed (**Ctrl+c** to kill program in the shell).

There it is! It works! 

NB: We also have a mp3 option to download the audio, which uses the same process, except ytdl-core takes the **mp3** argument to download the audio only.

Note that the only quality available for videos is 720p.

### Pros:

The download speed is much speedier than on other websites, since YOU host the server (localhost), it has no capping for download speed. I usually download a 10-15 minites video in 10 seconds.

There are no ads, no limits to how much videos you can download, and it will always work as long as the **ytdl-core** module is kept up to date!

### Installation

Remember, you should execute the **.bat** files for Windows, and **.sh** for Linux/Ubuntu!

Download/Copy the Github repository.

Go into the ***Setup*** folder, and execute ***node-setup*** file to install NodeJS.

Execute ***modules-setup*** to install the modules. 

NB: You need to have finished the installation of NodeJS before executing modules-setup (in node-setup).

**Done!** To start the website, execute ***start*** in the main folder.
