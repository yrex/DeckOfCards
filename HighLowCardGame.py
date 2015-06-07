from DeckOfCards import FrenchDeckOfCards, Card
from collections import defaultdict


class HiLowCard(Card):
    """
    HiLowCard is a subclass of Card which adds card comparison operators suitable for a HighLow card game.
    """
    def __init__(self, suit, pip):
        super(HiLowCard, self).__init__(suit, pip)

    def __lt__(self, other):
        return self.pip < other.pip

    def __le__(self, other):
        return self.pip <= other.pip

    def __eq__(self, other):
        return self.pip == other.pip

    def __ne__(self, other):
        return self.pip != other.pip

    def __gt__(self, other):
        return self.pip > other.pip

    def __ge__(self, other):
        return self.pip >= other.pip


class HiLowCardDeck(FrenchDeckOfCards):
    def __init__(self, suit_list=None, pip_list=None):

        super(HiLowCardDeck, self).__init__(suit_list, pip_list)

        # create a registry of all cards and initialise it
        # the register is a dictionary, with the pip ranks as the keys
        self._init_register()

    @classmethod
    def make_card(cls, suit, pip):
        """
        override the default card method, to return a HiLowCard object.

        :param suit: a Suit object
        :param pip: a Pip object
        :return: a HiLowCard object (a Card sub-class)
        """

        return HiLowCard(suit, pip)

    def draw(self):
        """
        Update the registry of cards and return the randomly drawn card
        """

        chosen_card = super(HiLowCardDeck, self).draw()
        self.update_register(chosen_card.pip.rank, -1)
        return chosen_card

    def _init_register(self):
        """
        Initialise the registry of cards in the deck
        """

        self.register = defaultdict(int)

        for c in self.cards:
            self.update_register(c.pip.rank, 1)

    def update_register(self, pip_to_update, amount=0):
        self.register[pip_to_update] += amount


class HiLowCardGame():

    GUESS_TYPES = ('H', 'L')

    def __init__(self, card_count=False):
        # create a deck of cards
        self.deck = HiLowCardDeck()

        # set initial score to zero
        self.score = 0

        # enable card-counting
        self.card_count = card_count

    def play_game(self):

        play_next_round = True

        # continue playing the game until the user decides to quit,
        # or the cards on the deck are depleted.
        while play_next_round and (self.deck.size() > 0):

            print('~'*30)
            print('SCORE: {score}'.format(score=self.score))
            print('\n')
            # play a round of the game
            self.play_round()

            if self.deck.size() == 0:
                print('No more cards! Your final score is: {0}'.format(self.score))
                return True
            # ask if user wants to play again
            play_again = input('Play another round? [Y/N]')

            while play_again.upper() not in ('Y', 'N'):
                print('Invalid input. type [Y/N]')
                play_again = input('Play another round? [Y/N]')

            if play_again.upper() == 'Y':
                play_next_round = True
            elif play_again.upper() == 'N':
                play_next_round = False
                print('Thanks for playing! Your final score is {0}'.format(self.score))
                return True
            else:
                print('Invalid input. type [Y/N]')
                return False

    def play_round(self):

        first_card = self.deck.draw()
        print('Current Card: {0}\n'.format(first_card))

        # give information on best choice, if card-counting is enabled
        if self.card_count:
            current_stats = self.game_stats(first_card)
            self.process_game_stats(*current_stats)

        user_guess = input('Is the next card [H]igher or [L]ower?')

        while user_guess not in HiLowCardGame.GUESS_TYPES:
            print('Not a valid guess! type [H/L]')
            user_guess = input('Is the next card [H]igher or [L]ower?')

        # draw the second card
        second_card = self.deck.draw()

        if self.is_guess_correct(first_card, second_card, user_guess):
            print('Good Guess! The card was {card}\n'.format(card=second_card))
            self.score += 1
        else:
            print('Bad Guess :( The card was {card}\n'.format(card=second_card))
            self.score -= 1

    def is_guess_correct(self, old_card, new_card, guess):
        """
        Check if the user's guess was correct

        :param guess: a single character string 'H' or 'L'
        :return: boolean on whether the guess was correct or not
        """

        if guess.upper() == HiLowCardGame.GUESS_TYPES[0]:
            # user selects 'H'
            if new_card > old_card:
                return True
            else:
                self.score -= 1
                return False
        elif guess.upper() == HiLowCardGame.GUESS_TYPES[1]:
            # user selects 'L'
            if new_card < old_card:
                return True
            else:
                return False
        else:
            # user selects anything else
            print('Not a valid guess! type [H/L]')

    def game_stats(self, current_card):
        """
        game_stats calculates the probability of getting a higher/lower card on the next draw

        :param current_card: the current card drawn
        :return: returns a tuple as (proba_lower, proba_higher) where values are in the range [0, 1]
        """

        current_card_rank = current_card.pip.rank

        cards_less = 0
        for k, v in self.deck.register.items():
            if k <= current_card_rank:
                cards_less += v

        cards_higher = self.deck.size() - cards_less

        # get the probability of getting a higher or lower card
        proba_lower = cards_less / self.deck.size()
        proba_higher = cards_higher / self.deck.size()

        return proba_lower, proba_higher

    def process_game_stats(self, proba_lower, proba_higher):
        """
        process the game stats and present to user
        :return: a string with the output stats
        """
        print('Chance of a getting a lower card: {0:.2f}%\n'\
              'Chance of getting a higher card: {1:.2f}%\n'
              .format(proba_lower*100, proba_higher*100))




if __name__ == '__main__':
    pass