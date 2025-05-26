# OfficeTime Slack Bot — Socket Mode Version
# ------------------------------------------
# A lightweight Slack bot that responds to `/officetime` by showing local time
# across company offices using emojis that reflect local culture or landmarks.
#
# Built with Slack Bolt for Python
# See README.md and requirements.txt for context and setup.
#
# Author: Cameron Livingstone
# github.com/clive-jpg | 2025

import os
from datetime import datetime
from zoneinfo import ZoneInfo

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler


# Slack Bolt app
app = App(token=os.environ["SLACK_BOT_TOKEN"], signing_secret=os.environ["SLACK_SIGNING_SECRET"])
handler = SlackRequestHandler(app)

# Office data
timezones = {
    'Edinburgh': 'Europe/London',
    'Glasgow': 'Europe/London',
    'London': 'Europe/London',
    'Shenzhen': 'Asia/Shanghai',
    'Singapore': 'Asia/Singapore',
    'Tokyo': 'Asia/Tokyo',
    'Delhi': 'Asia/Kolkata',
    'Miami': 'America/New_York'
}

emojis = {
    'Edinburgh': '🦄',
    'Glasgow': '🎸',
    'London': '🎡',
    'Shenzhen': '🏙️',
    'Singapore': '🦁',
    'Tokyo': '🗼',
    'Delhi': '🏏',
    'Miami': '🌴'
}

# Respond to the slash command `/officetime`
@app.command("/officetime")
def handle_officetime(ack, respond, command):
    ack()

    user_id = command['user_id']
    lines = [f'Hey <@{user_id}>! Here\'s the current time in our offices:\n']

    for city, tz in timezones.items():
        emoji = emojis.get(city, '🌍')
        time_str = datetime.now(ZoneInfo(tz)).strftime('%H:%M')
        lines.append(f'{emoji} *{city}*: {time_str}')

    respond('\n'.join(lines))

# Lambda entry point
def lambda_handler(event, context):
    return handler.handle(event, context)
