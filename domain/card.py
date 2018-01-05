'''
Card classes
'''
from enum import Enum
import random


class Suit(Enum):
    ALL_TRUMPS = "T"
    NO_TRUMPS = "\u27c2"
    CLUBS = "\u2663"
    DIAMONDS = "\u2662"
    HEARTS = "\u2661"
    SPADES = "\u2660"

    def is_real_suit(self):
        return self != self.ALL_TRUMPS and self != self.NO_TRUMPS
    
    def __str__(self):
        return self.value
    
    __repr__ = __str__


class _RankEnum:
    def __init__(self, display_name, trump_rank, rank, points, trump_points, no_trump_points, all_trump_points):
        self.display_name = display_name
        self.trump_rank = trump_rank*8
        self.rank = rank
        self.points = points
        self.trump_points = trump_points
        self.no_trump_points = no_trump_points
        self.all_trump_points = all_trump_points
    
    def __str__(self):
        return self.display_name
    
    __repr__ = __str__


class Rank(Enum):
    ACE   = _RankEnum( "A", 5, 7, 11, 11, 19,  7)
    TEN   = _RankEnum("10", 4, 6, 10, 10, 10,  5)
    KING  = _RankEnum( "K", 3, 5,  4,  4,  4,  3)
    QUEEN = _RankEnum( "Q", 2, 4,  3,  3,  3,  2)
    JACK  = _RankEnum( "J", 7, 3,  2, 20,  2, 14)
    NINE  = _RankEnum( "9", 6, 2,  0, 14,  0,  9)
    EIGHT = _RankEnum( "8", 1, 1,  0,  0,  0,  0)
    SEVEN = _RankEnum( "7", 0, 0,  0,  0,  0,  0)
    
    def __str__(self):
        return str(self.value)
    
    __repr__ = __str__


class Card:
    def __init__(self, suit, rank):
        if not suit.is_real_suit():
            raise ValueError("Cards must have a real suit")
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return "{}{}".format(self.rank, self.suit)
    
    __repr__ = __str__
    
    def __eq__(self, other):
        return (self.__class__ == other.__class__
            and self.rank == other.rank
            and self.suit == other.suit)
    
    def __hash__(self):
        return hash((self.rank, self.suit))

    def points(self, trump):
        """
        Return the points of the card depending on the trump.
        """
        if trump == Suit.ALL_TRUMPS:
            return self.rank.value.all_trump_points
        elif trump == Suit.NO_TRUMPS:
            return self.rank.value.no_trump_points
        elif trump == self.suit:
            return self.rank.value.trump_points
        else:
            return self.rank.value.points


class CardKey:
    def __init__(self, trump, lead_suit):
        """
        :param trump:
        :param lead_suit: Color of the first card played.
        """
        if not lead_suit.is_real_suit():
            raise ValueError("The lead suit must be real")
        self._trump = trump
        self._lead_suit = lead_suit
    
    def key(self):
        def k(card):
            if card.suit == self._trump:
                return card.rank.value.trump_rank
            elif card.suit == self._lead_suit:
                if self._trump == Suit.ALL_TRUMPS:
                    return card.rank.value.trump_rank
                else:
                    return card.rank.value.rank
            else:
                return -1
        return k


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in [Suit.CLUBS, Suit.DIAMONDS, Suit.HEARTS, Suit.SPADES] for r in Rank]
        random.shuffle(self.cards)
    
    def __iter__(self):
        return self.cards.__iter__()
    
    def __len__(self):
        return len(self.cards)