# DeckOfCards Package

This package contains classes for creating a generic deck of playing cards, for use in games or anything else.
The generic class `DeckOfCards` can be used as the basic building block of a deck of cards. A specific class `FrenchDeckOfCards` is also provided which the French playing cards.

Each `Card` is made from a `Suit` and a `Pip` object which denotes its suit and numeric value, as well as their rank comapred to other cards.

The `HiLowCardGame` is built using a custom sub-class of the `FrenchDeckOfCards` and allows for a simple implementation of the High/Lo 1-player card game.
By initialising the game using `card_count=True`, game statistics will be reported at each round.

```python
Current Card: 4 of Hearts

Chance of a getting a lower card: 29.79%
Chance of getting a higher card: 70.21%

Is the next card [H]igher or [L]ower?
```

An example game and example deck of cards usage, as well as a unittest are provided.

### Todo
Expand the unittests.