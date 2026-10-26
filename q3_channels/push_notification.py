"""Q3(d): a NEW file. channels.py and send_all() are not modified."""
from channels import Channel


class PushNotification(Channel):
    def __init__(self):
        super().__init__("Push")

    def cost(self):
        return 0
