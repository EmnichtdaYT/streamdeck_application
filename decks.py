from StreamDeck import DeviceManager
from StreamDeck.Devices import StreamDeck

loaded_decks = {}

class Deck:
    def __init__(self, p_deck: StreamDeck):
        self.p_deck = p_deck

def load_decks() -> list[Deck]:
    for p_deck in DeviceManager.DeviceManager().enumerate():
        load_decks[p_deck.get_serial_number()] = Deck(p_deck)
    return load_decks

def start_configured_decks() -> list[Deck]:
    for deck in loaded_decks.values():
        pass # TODO implement