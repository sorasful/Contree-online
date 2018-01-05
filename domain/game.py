'''
Game module
'''

from enum import Enum
from domain.card import Rank, Suit, Card, CardKey, Deck
import random

class Phase(Enum):
    BID = 1
    PLAY = 2

class Seat(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    def next(self):
        return Seat((self.value + 1) % 4)

class Bid:
    def __init__(self, points, trump):
        if points % 10 != 0:
            raise ValueError("Points in bids must be multiples of 10")
        if points < 80:
            raise ValueError("Points in bids must be a minimum of 80")
        if points != 250 and points > 160:
            raise ValueError("Points in bids must be 250 or less than or equal to 160")
        self.points = points
        self.trump = trump
        
        def is_slam(self):
            return points == 250

class Match:
    def __init__(self, players):
        self.players = players
        self.dealer = random.choice(list(Seat))
        self.phase = None
        self.turn = None

    def _start_round(self):
        """
        Increment dealer
        Deal cards
        Switch to bid phase
        Set current player
        """
        self.dealer = self.dealer.next()
        self.hands = { seat: [] for seat in Seat }
        
        deck = Deck()
        
        s = self.dealer
        for c in deck:
            self.hands[s].append(c)
            s = s.next()
        
        self.bid = None
        self.bidder = None
        self.phase = Phase.BID
        self.turn = self.dealer.next()
    
    def _next_turn(self):
        self.turn = self.turn.next()
    
    def _start_play(self):
        self.phase = Phase.PLAY
        self.turn = self.dealer.next()
    
    
    def start(self):
        self._start_round()
    
    def interactor(self, seat):
        return MatchInteractor(self, seat)
    
    def can_make_bid(self, seat, bid=None):
        return (self.phase == Phase.BID
            and self.turn == seat
            and (bid == None or self.bid == None or self.bid.points < bid.points)
            )
    
    def make_bid(self, seat, bid):
        if bid == None:
            raise TypeError("bid cannot be None")
        if not self.can_make_bid(seat, bid):
            raise ValueError("Cannot make bid")
        self.bid = bid
        self.bidder = seat
        self._next_turn()
    
    def can_pass_bid(self, seat):
        return self.can_make_bid(seat)
    
    
    def pass_bid(self, seat):
        if not self.can_pass_bid(seat):
            raise ValueError("You shall not pass")
        
        if self.bid == None and self.dealer == seat:
            self._start_round()
        elif self.bid != None and self.bidder == seat.next():
            self._start_play()
        else:
            self._next_turn()
    
    def can_play(self, seat, card=None):
        return (self.phase == Phase.PLAY
                and self.turn == seat
                # TODO
                )
    
class MatchInteractor:
        def __init__(self, match, seat):
            self._match = match
            self.seat = seat
        
        def start(self):
            self._match.start()
        
        def hand(self):
            return self._match.hands[self.seat]
        
        def can_make_bid(self, bid=None):
            return self._match.can_make_bid(self.seat, bid)
        
        def make_bid(self, bid):
            self._match.make_bid(self.seat, bid)
        
        def can_pass_bid(self):
            return self._match.can_pass_bid(self.seat)
        
        def pass_bid(self):
            self._match.pass_bid(self.seat)
        
        def can_play(self, card=None):
            return self._match.can_play(self.seat, card)
        