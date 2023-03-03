from StreamDeck import DeviceManager

def print_decks():
    for deck in DeviceManager.DeviceManager().enumerate():
        print(f'[{deck.id()}] {deck.deck_type()}')