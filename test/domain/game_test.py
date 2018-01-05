from domain.game import Seat, Match, Phase, Bid
from domain.card import Suit


PLAYERS = { Seat.NORTH: '1234', Seat.SOUTH: '4321', Seat.EAST: '5678', Seat.WEST: '8765' }

def test_game_start():
    m = Match(PLAYERS)
    m.start()
    
    interactors = [m.interactor(s) for s in Seat]
    
    # All players have a hand of 8 cards
    assert all([len(i.hand()) == 8 for i in interactors])
    # One and only one player may bid
    assert len(list(filter(lambda i: i.can_make_bid(), interactors))) == 1

def test_first_bid():
    m = Match(PLAYERS)
    
    m.phase = Phase.BID
    m.dealer = Seat.NORTH
    m.turn = Seat.EAST
    m.bid = None
    m.bidder = None
    
    i = m.interactor(Seat.EAST)
    
    bid = Bid(100, Suit.HEARTS)
    
    assert i.can_make_bid()
    assert i.can_make_bid(bid)
    
    i.make_bid(bid)
    
    assert not i.can_make_bid()
    assert m.interactor(Seat.SOUTH).can_make_bid()
    
def test_first_pass():
    m = Match(PLAYERS)
    
    m.phase = Phase.BID
    m.dealer = Seat.NORTH
    m.turn = Seat.EAST
    m.bid = None
    m.bidder = None
    
    i = m.interactor(Seat.EAST)
    
    assert i.can_pass_bid()
    
    i.pass_bid()
    
    assert not i.can_make_bid()
    assert m.interactor(Seat.SOUTH).can_make_bid()
    
def test_third_pass_after_bid():
    m = Match(PLAYERS)
    m.phase = Phase.BID
    m.dealer = Seat.NORTH
    m.turn = Seat.EAST
    m.bid = Bid(100, Suit.HEARTS)
    m.bidder = Seat.SOUTH
    
    i = m.interactor(Seat.EAST)

    i.pass_bid()
    
    assert not i.can_make_bid()
    assert i.can_play()

def test_fourth_pass_after_no_bid():
    m = Match(PLAYERS)
    
    m.phase = Phase.BID
    m.dealer = Seat.NORTH
    m.turn = Seat.NORTH
    m.bid = None
    m.bidder = None
    
    i = m.interactor(Seat.NORTH)
    
    i.pass_bid()
    
    assert m.interactor(Seat.SOUTH).can_make_bid()
