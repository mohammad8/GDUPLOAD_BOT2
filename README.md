# Google Drive Uploader Telegram Bot
**A Telegram bot to upload files from Telegram or Direct links to Google Drive.**
- Find it on Telegram as [Google Drive Uploader](https://t.me/gdriveruploadtd_bot)

## Features
- [X] Telegram files support.
- [X] Direct Links support.
- [X] Custom Upload Folder.
- [X] TeamDrive Support.
- [X] Clone/Copy Google Drive Files.
- [X] Delete Google Drive Files.
- [X] Empty Google Drive trash.
- [X] youtube-dl support.
- [X] Docker Supported


### How To Deploy Video Tutorial:

[![](https://telegra.ph/file/291e37efec46c3a408319.png)](https://youtu.be/sTQkY0UE20c)


## Deploying

### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Deploy on Railway

[![Deploy To Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/prxpostern/GDUPLOAD_BOT2&envs=API_ID,API_HASH,BOT_TOKEN,SUDO_USERS,DATABASE_URL,DOWNLOAD_DIRECTORY,ENV,G_DRIVE_CLIENT_ID,G_DRIVE_CLIENT_SECRET,SUPPORT_CHAT_LINK&optionalEnvs=DATABASE_URL&G_DRIVE_CLIENT_IDDefault=202264815644.apps.googleusercontent.com&G_DRIVE_CLIENT_SECRETDefault=X4Z3ca8xfWDb1Voo-F9a7ZxJ&ENVDefault=ANYTHING&DOWNLOAD_DIRECTORYDefault=./downloads/)

### Deploy on Qovery

[![Deploy to Qovery](https://img.shields.io/badge/Deploy-Qovery-6EC0D9.svg)](https://qovery.com)




### Installation
- Install required modules.
```sh
apt install -y git python3 ffmpeg
```
- Clone this git repository.
```sh 
git clone https://github.com/kjeymax/GDUPLOAD_BOT2
```
- Change Directory
```sh 
cd GDUPLOAD_BOT2
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Configuration
**There are two Ways for configuring this bot.**
1. Add values to Environment Variables. And add a `ENV` var to Anything to enable it.
2. Add values in [config.py](./bot/config.py). And make sure that no `ENV` environment variables existing.

### Configuration Values
- `BOT_TOKEN` - Get it by contacting to [BotFather](https://t.me/botfather)
- `APP_ID` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `SUDO_USERS` - List of Telegram User ID of sudo users, seperated by space.
- `DATABASE_URL` - Postgres database url.
- `DOWNLOAD_DIRECTORY` - Custom path for downloads. Must end with a forward `/` slash. (Default to `./downloads/`)
- `ENV` - ANYTHING
- `G_DRIVE_CLIENT_ID` - 202264815644.apps.googleusercontent.com
- `G_DRIVE_CLIENT_SECRET` - X4Z3ca8xfWDb1Voo-F9a7ZxJ
- `SUDO_USERS` - 1331188677 956524656
- `SUPPORT_CHAT_LINK` - t.me


### Deploy 
```sh 
python3 -m bot
```

### COMMANDS FOR THE BOT TO BE USED-
```
- start - useless command
- help - How to use me
- auth - Authorizing GDrive Account
- setfolder - Set Custom Upload Folder
- copy - Copy GDrive Files
- revoke - Revoke GDrive Account
- del - Delete GDrive Files
```
## Credits
- [Dan](https://github.com/delivrance) for creating [PyroGram](https://pyrogram.org)
- [Spechide](https://github.com/Spechide) for [gDriveDB.py](./bot/helpers/sql_helper/gDriveDB.py)
- [Shivam Jha](https://github.com/lzzy12) for [Clone Feature](./bot/helpers/gdrive_utils/gDrive.py) from [python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot)

## Copyright & License
- Copyright (©) 2021 by [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)
