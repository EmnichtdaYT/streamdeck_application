from StreamDeck import DeviceManager
from StreamDeck.Devices import StreamDeck

class Deck:
    def __init__(self, stream_deck: StreamDeck):
        self.stream_deck = stream_deck
        