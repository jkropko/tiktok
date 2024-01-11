# A general data pipeline to the TikTok Research API

## Installation

First, download, install, and launch the [Docker Desktop Client](https://www.docker.com/products/docker-desktop/) on your computer.

Next, find a way to access the command line on your system. The location of the command line varies depending on whether you are using a Mac, Windows, or Linux system. Here are general instructions for finding the command line on [Mac](https://www.wikihow.com/Get-to-the-Command-Line-on-a-Mac), [Windows](https://www.wikihow.com/Open-the-Command-Prompt-in-Windows), and [Linux](https://www.makeuseof.com/how-to-open-terminal-in-linux/).

Then determine where on your computer you would like a folder for the files associated with this project to exist. Use the `cd` command on the command line for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd) or [Mac or Linux](https://www.macworld.com/article/221277/command-line-navigating-files-folders-mac-terminal.html) followed by the file address of this location to navigate to that folder.

Separately, make sure you've signed up for a free account on [Github](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home). Once you have done so, type the following into the command line:
```
git clone https://github.com/jkropko/tiktok
```

The `git clone` command downloads the files you need to run the code for operating the TikTok data pipeline. It will create a new folder in your current directory named "tiktok". You only need to do this one time.

## Usage

Use the `cd` command to navigate to the "tiktok" folder. Then to launch the development environments, type
```
docker compose up
```

You will see output start to display in your terminal window. Within the output, you will see text such as

```
Or copy and paste one of these URLs:
pipeline-github-jupyterlab-1  |         http://ea59a8fbdbac:8888/lab?token=205a9abc0c59b11e2ba7d21c35703dd1013b5f42617f1646
pipeline-github-jupyterlab-1  |         http://127.0.0.1:8888/lab?token=205a9abc0c59b11e2ba7d21c35703dd1013b5f42617f1646
``	

Copy the URL that begins http://127.0.0.1:8888/ and paste it into a web browser to launch JupyterLab with all associated packages and databases connected.
