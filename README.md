# OfficeTime Slack Bot 🕒

**OfficeTime** is a lightweight Slack bot that responds to the `/officetime` command by showing current local times across key office locations to the user silently. Requires no API calls, making commands efficient.

It uses Python, Slack Bolt, and emoji-based city icons. Currently, Websocket (persistent) based slack app is supported. (TBA)

![OfficeTime Bot Screenshot](assets/officetimebot.png)

---

## Features

- Slash command `/officetime`
- Timezone-aware via Python’s `zoneinfo`
- Emoji-themed output for each city
- Ephemeral messages (only shown to you)
- Customisable list of cities and emojis

---

## Required scopes (Set these in App Permissions)

Required scopes:
commands – to register /officetime
chat:write – to send ephemeral messages

Slash command setup:
Command: /officetime

## Common Issues
-Ensure that pytho module dependecies are installed
-Ensure that bot and app tokens are correct
-Set /slashcommand in app permissions to 'officetime' to enable decorator function

## Upcoming

- Creation of App Manifest file
- Http based client server based slack app - command on requests