import collections

#  we use namedtuple to construct a simple class to represent individual cards.
#  it builds classes of objects - essentially they are bundle of attributes with no
#  custom methods
Card = collections.namedtuple("Card", ["rank", "suit"])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    """
    Ace - 1
    2-10 cards of type (J)ack, (Q)ueen, (K)ing, (A)ce

    sorting:
        highest rank: ace
        highest suit by order: spades, hearts, diamonds, clubs

    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
