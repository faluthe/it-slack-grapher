import json
import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# To track who is updating tickets in a channel that prints ticket updates 
class SlackBot:
    def __init__(self):
        self.app = App(token=os.environ["SLACK_BOT_TOKEN"])
        self.known_users = self.read_users()
        self.app.message()(self.add_msg)


    def add_msg(self, message):
        # Search message text for ticket updater
        user = self.get_updater(message["text"])

        if user is None:
            return
        
        self.known_users[user] = self.known_users.get(user, 0) + 1
        self.write_users(self.known_users)

        print("A ticket has been updated by", user.split("\n")[1])
        

    def read_users(self):
        try:
            with open("stats.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


    def write_users(self, users):
        with open("stats.json", "w") as f:
            json.dump(users, f)


    def get_updater(self, msg):
        # Updater is in the format *name* (_username_)
        matches = re.search(r"\*([^*]+)\*\s+\(_([^_]+)_\)", msg)
        
        if matches:
            name = matches.group(1)
            username = matches.group(2)

            # Ignore non-employee accounts (better to add list of known employees and check against that)
            if not username.endswith("rcc"):
                return None

            # Make the last name an intial
            name = name.split(" ")
            name[-1] = name[-1][0]
            name = " ".join(name)

            return f"{name}\n{username}"
        else:
            return None


    def start(self):
        SocketModeHandler(self.app, os.environ["SLACK_APP_TOKEN"]).start()


if __name__ == "__main__":
    bot = SlackBot()
    bot.start()