"""Q3(b): abstract Channel and three concrete channels."""
from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def cost(self):
        """Cost of one message in cents."""

    def deliver(self, message):
        print(f"[{self._name}] {message} (cost {self.cost()} cents)")


class Sms(Channel):
    def __init__(self):
        super().__init__("SMS")

    def cost(self):
        return 8


class Email(Channel):
    def __init__(self):
        super().__init__("Email")

    def cost(self):
        return 0


class WhatsApp(Channel):
    def __init__(self):
        super().__init__("WhatsApp")

    def cost(self):
        return 4


def send_all(channels, message):
    """The single loop: works for ANY Channel, present or future."""
    total = 0
    for ch in channels:
        ch.deliver(message)
        total += ch.cost()
    print("Total cost:", total, "cents")
    return total
