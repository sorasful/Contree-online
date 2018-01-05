import pytest
from domain.card import Suit, Rank, Card, CardKey, Deck

@pytest.mark.parametrize("c1, c2, trump, lead_suit", [
    (Card(Suit.HEARTS, Rank.ACE), Card(Suit.HEARTS, Rank.TEN), Suit.SPADES, Suit.HEARTS),
    (Card(Suit.SPADES, Rank.TEN), Card(Suit.HEARTS, Rank.ACE), Suit.SPADES, Suit.HEARTS),
    (Card(Suit.HEARTS, Rank.TEN), Card(Suit.CLUBS, Rank.ACE), Suit.SPADES, Suit.HEARTS),
    (Card(Suit.HEARTS, Rank.TEN), Card(Suit.CLUBS, Rank.ACE), Suit.NO_TRUMPS, Suit.HEARTS),
    (Card(Suit.HEARTS, Rank.TEN), Card(Suit.CLUBS, Rank.ACE), Suit.ALL_TRUMPS, Suit.HEARTS),
    (Card(Suit.SPADES, Rank.JACK), Card(Suit.SPADES, Rank.ACE), Suit.SPADES, Suit.HEARTS),
    (Card(Suit.HEARTS, Rank.ACE), Card(Suit.HEARTS, Rank.JACK), Suit.SPADES, Suit.HEARTS),
    (Card(Suit.HEARTS, Rank.JACK), Card(Suit.HEARTS, Rank.ACE), Suit.ALL_TRUMPS, Suit.HEARTS),
    ])
def test_compare(c1, c2, trump, lead_suit):
    
    key = CardKey(trump, lead_suit)
    
    assert key.key()(c1) > key.key()(c2)


def test_deck():
    deck = Deck()
    
    assert Card(Suit.HEARTS, Rank.ACE) in deck
    assert len(deck) == 32
    assert len(set(deck)) == 32