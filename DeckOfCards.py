import numpy as np
from collections import defaultdict

class Suit():

    """
    Suit defines a playing card suit, using a name (string) and a rank (integer)

    """

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Suit({0}, {1})'.format(self.name, str(self.rank))

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank



class Pip():
    """
    Pip defines a playing card's pip (value)
    """

    def __init__(self, pip, rank, name=None):
        self.pip = pip
        self.rank = rank
        if name is None:
            self.name = str(pip)
        else:
            self.name = name

    def __repr__(self):
        return 'Pip({0}, {1}, {2})'.format(str(self.pip), str(self.rank), str(self.name))

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Card():

    """
    Card is a playing card object with a suit, integer value and rank.
    The rank is defined based on the game played.
    Face cards have values 11 for Jack, 12 for Queen and 13 for King.

    """

    def __init__(self, suit, pip):

        """
        Initialise a Card object

        suit: a Suit object containing the suit name and suit's rank
        pip: a Pip object containing the the integer value of the card and the pip's rank
        """

        # self.suit is a Suit object
        self.suit = suit
        self.pip = pip

    def __str__(self):
        return str(self.pip) + ' of ' + str(self.suit)

    def __repr__(self):
        return 'Card({0}, {1})'.format(str(self.suit), str(self.pip))


class DeckOfCards():
    """
    DeckOfCards is an object for a deck (pack) of playing cards.
    By default a deck of French playing cards is initialised.
    """

    def __init__(self, suits, pips):

        """
        Initialise the deck of cards

        suits: a list of Suit objects
        pips: a list of Pip objects
        """

        # cards on the deck
        self.cards = list()

        for suit in suits:
            for pip in pips:
                # add to list of cards
                self.cards.append(self.make_card(suit, pip))

    def draw(self):
            # choose a card
            high = self.size()
            if not self.is_empty():
                r = np.random.randint(0, high=high)
                selection = self.cards[r]
                self.cards.remove(selection)
            else:
                selection = None
            return selection

    @classmethod
    def make_card(cls, suit, pip):
        """
        Create a Card object. This method can be over-ridden in sub-classes to
        generate cards with different properties.

        :param suit: a Suit object
        :param pip: a Pip object
        :return: a Card object
        """
        return Card(suit, pip)

    def size(self):
        """
        return the number of cards in the deck
        """
        return len(self.cards)

    def is_empty(self):
        """
        return a boolean to show if the deck is empty (no cards left on the deck)
        """
        if self.size() == 0:
            return True
        else:
            return False


class FrenchDeckOfCards(DeckOfCards):
    """
    A deck of cards using the French suits and pips
    """
    def __init__(self, suit_list=None, pip_list=None):

        if suit_list is None:
            suit_list = self._set_default_suits()

        if pip_list is None:
            pip_list = self._set_default_pips()


        # initialise deck
        super(FrenchDeckOfCards, self).__init__(suit_list, pip_list)

    def _set_default_suits(self):
        """
        Set the default playing card suits for the French card deck

        returns a list of Suit objects
        """
        # set up suits
        suit_types = [('Spades', 1), ('Hearts', 2), ('Diamonds', 3), ('Clubs', 4)]
        # populate the list of suits
        suit_list = list()
        for s in suit_types:
            suit_list.append(Suit(s[0], s[1]))

        return suit_list

    def _set_default_pips(self):
        """
        Set the default playing card pips for the French card deck

        returns a list of Pip objects
        """

        # set up pips
        pip_types = ((1, 1, 'Ace'), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
                   (9, 9), (10, 10), (11, 11, 'Jack'), (12, 12, 'Queen'), (13, 13, 'King'))
        # popular the list of pips
        pip_list = list()
        for p in pip_types:
            if len(p) < 3:
                # if name is not specified
                pip_list.append(Pip(p[0], p[1]))
            else:
                pip_list.append(Pip(p[0], p[1], p[2]))

        return pip_list



if __name__ == '__main__':
    pass
