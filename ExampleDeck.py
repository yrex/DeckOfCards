from DeckOfCards import FrenchDeckOfCards

if __name__ == '__main__':
    deck = FrenchDeckOfCards()
    for i in range(10):
        c = deck.draw()
        print(c)