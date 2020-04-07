# wxteams-welcome-bot
A simple Webex Teams Bot that welcomes people upon joining any space the bot is in. 

## Installation

You can modify the message you want to display in the `bot.py` file. 

Either use the provided docker file or run it on your machine using the `entrypoint.sh`. 

**Environment Variables**

* `WEBEX_TEAMS_ACCESS_TOKEN` the access token of your webex teams bot
* `REMOTE_PREFIX` the publically reachable adress of your webex teams bot

If you specify the remote prefix you can use [webhooksimple](https://github.com/CiscoSE/webhooksimple) to automatically
create the webhooks for you. 
