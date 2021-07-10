# Paulie Bot
A Reddit Bot based on Paulie 'Walnuts' Gualtieri from The Sopranos.

![](https://media2.giphy.com/media/4UHVCPKYeWHYY/giphy.gif?cid=ecf05e47hhuj0e3gl486sxv9rk7rrki48jcbt03g0nb0gojk&rid=giphy.gif&ct=g)

## Prerequisites
* Reddit Account
* Generate a [Reddit Application](https://www.reddit.com/prefs/apps/) to generate client token and secret.
* *Note:* Ensure you select the 'script' type.

## Setup
* Replace `CLIENT_ID`, `CLIENT_SECRET`, `USERNAME` and `PASSWORD` fields in `secrets.py` with your details.
* Replace `SUBREDDIT` & `USER_AGENT` in `bot.py` to your desired subreddit and user agent respectively.
* *Optional*: Change the `INTERVAL` field to modify how often the bot should reply to comments.

## Run
To run locally, use `python bot.py`
