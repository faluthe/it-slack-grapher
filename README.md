# IT Ticket Service Visualization Tools

This repository contains two Python applications designed to work together to monitor IT service ticket updates on a Slack channel and visualize the data through a graph server.

## Expected Behavior
The Slack bot (slackbot.py) will monitor messages that follow the format shown in the following image. When it detects a ticket update, it logs the user's name and the associated username. The bot ignores any usernames that do not end with 'rcc'.
![Slack Channel Screenshot](/docs/example_ticket_updates.png)

The graph server (graphserver.py) reads the accumulated data and displays it in a bar graph, similar to the second provided image. The graph updates in real-time, showing the number of ticket updates per user.
![Graph Server](/docs/example_graph.png)

## Contents
- slackbot.py: A Slack bot that monitors a designated Slack channel for ticket update messages and records the number of updates per user.
- graphserver.py: A Bokeh server application that reads the accumulated data and displays it in a bar graph format, updating in real-time.

## Prerequisites
Before running the applications, you must have Python installed on your system and an active Slack workspace where the bot will monitor ticket updates.

## Installation
Clone the repository to your local machine.
Install the necessary Python packages using pip:
``` 
pip install slack-bolt bokeh
```

## Slack Bot and App Tokens
To use the Slack bot, you need to create a Slack App and install it to your workspace. Follow these steps to get your BOT and APP tokens:
1. Go to Your Apps on the Slack API website.
2. Click "Create New App" and set the name and workspace.
3. Navigate to "OAuth & Permissions" and add the necessary bot scopes (e.g., channels:history, connections:write).
4. Install the app to your workspace.
5. Copy the "Bot User OAuth Access Token" and "App-Level Token" from the "OAuth & Permissions" page.

## Configuration
Set your Slack bot and app tokens as environment variables. On Unix based systems:
```
export SLACK_BOT_TOKEN='your-bot-token-here'
export SLACK_APP_TOKEN='your-app-token-here'
```
On Windows Powershell:
```
$env:SLACK_BOT_TOKEN = 'your-bot-token-here'
$env:SLACK_APP_TOKEN = 'your-app-token-here'
```

## Running the Applications
To run the Slack bot:
``` python slackbot.py ```
To run the Graph server:
``` bokeh serve --show graphserver.py ```
The Slack bot will listen for messages in the designated channel, and the graph server will provide a real-time visualization accessible in your web browser.

## Troubleshooting
- Ensure that your Slack App has the correct permissions and is installed in your workspace.
- Verify that the stats.json file is writable and in the correct directory.
- Check that the environment variables for the Slack tokens are correctly set.

For further questions or support, please open an issue in this repository.
