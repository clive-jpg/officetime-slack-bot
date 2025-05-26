# OfficeTime Slack Bot — Socket Mode Version
# ------------------------------------------
# A lightweight Slack bot that responds to `/officetime` by showing local time
# across company offices using emojis that reflect local culture or landmarks.
#
# Built with Slack Bolt for Python
# See README.md and requirements.txt for context and setup.
#
# This bot uses .env for slack binding, check the .env.example for required variable format.
#
# Author: Cameron Livingstone
# github.com/clive-jpg | 2025

import os
from datetime import datetime
from zoneinfo import ZoneInfo

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

# Initialize Slack app using Bolt with token from environment
app = App(token=os.environ.get('SLACK_BOT_TOKEN'))

# Office locations and their corresponding IANA timezone identifiers
# Change dict values to customise office locations and timezones
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

# Emojis reflecting each city's personality or symbolism
# Change dict values to customise emojis for each office
emojis = {
    'Edinburgh': '🦄',     # National animal of Scotland
    'Glasgow': '🎸',       # Legendary music scene
    'London': '🎡',        # London Eye
    'Shenzhen': '🏙️',      # Futuristic skyline
    'Singapore': '🦁',     # Merlion
    'Tokyo': '🗼',         # Tokyo Tower
    'Delhi': '🏏',         # Cricket 
    'Miami': '🌴'          # Palm trees
}

# Respond to the slash command `/officetime`
@app.command('/officetime')
def handle_check_timezones(ack, client, command):
    '''
    Responds to the /officetime command with current local times
    in all configured office locations. Output is sent as an ephemeral
    message to the user who invoked the command.
    '''
    ack()  # Required for Slack to acknowledge the command within 3 seconds

    user_id = command['user_id']
    channel_id = command['channel_id']

    # Start building the response lines
    lines = [f'Hey <@{user_id}>! Here\'s the current time in our offices:\n']

    # Iterate through each office, format the time and append to response
    for city, tz in timezones.items():
        emoji = emojis.get(city, '🌍')  # Fallback emoji if no match found
        time_str = datetime.now(ZoneInfo(tz)).strftime('%H:%M')
        lines.append(f'{emoji} *{city}*: {time_str}')

    # Send the response as an ephemeral message (only the user sees it)
    client.chat_postEphemeral(
        channel=channel_id,
        user=user_id,
        text='\n'.join(lines)
    )

# Socket Mode handler for local dev or always-on EC2 instance
if __name__ == '__main__':
    SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()

