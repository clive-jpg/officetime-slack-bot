# OfficeTime Slack Bot 🕒 

***OfficeTime*** is a lightweight Slack bot that responds to the slack /officetime command by showing current local times across key office locations.

This was my first project—built to explore Python, get comfortable with GitHub, and try out AWS services like Lambda and EC2, along with the Slack API. It doesn’t use any external web APIs—just Python timezone modules.

Both Socket Mode and AWS Lambda versions are included—check the files to see what’s needed for each.

![OfficeTime Bot Screenshot](assets/officetimebot.png)

---

## Features

- Slash command `/officetime`
- Timezone-aware via Python’s `zoneinfo`
- Emoji-themed output for each city
- Ephemeral messages (only shown to you)
- Customisable list of cities and emojis

---

## Required scopes (Set these in Slack Admin App Permissions)

Required scopes:
- commands – to register /officetime
- chat:write – to send ephemeral messages

Enable Slash command in app permision
- Command: set to /officetime

## Common Issues

- Ensure that python module dependencies are installed
- Ensure that bot and app tokens match on slack admin
- Ensure /slashcommand in app permissions is to 'officetime' to enable app

## Upcoming

- Creation of App Manifest file for easy app creation (Easy setup)

