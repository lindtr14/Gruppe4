# -*- coding: utf-8 -*-

# This module represents a game of poker with players. 
# It is possible to deal out cards to players. A hand consists of 
# 5 cards. There will be ranking lists, so the system can compare hands
# and pick out a winner

def poker(hands):
  """ Picks up the hands ingame and compare them to eachother. 
      Returns the highest hand
  """
  return allmax(hands, key=hand_rank)
  
def hand_rank(hand):
  """ Takes a hand and returns the highest rank representing
      the hand
  """
  groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
  counts, ranks = unzip(groups)

  if ranks == (14, 5, 4, 3, 2):
    ranks = (5, 4, 3, 2, 1) 

  straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4

  flush = len(set([s for r, s in hand])) == 1
  count_rankings = {(5,):10, (4,1):7, (3,2):6, (3,1,1):3, 
  			            (2,2,1):2, (2,1,1,1):1, (1,1,1,1,1):0}
  return max(count_rankings[counts], 4*straight + 5*flush), ranks

def group(items):
  """ Takes a hand as decimal and returns the hand sorted by
      counts
  """
  groups = [(items.count(x), x) for x in set(items)] 
  return sorted(groups, reverse=True) 
  
def unzip(pairs): 
  """ Takes a list and returns it as two lists """
  return zip(*pairs)
  
def card_ranks(hand):
  """ Takes a hand and returns it as decimal """

  ranks = ["--23456789TJQKA".index(r) for r,s in hand]
  ranks.sort(reverse=True)

  return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def kind(n, ranks):
  """ Takes a hand and check if it is any kind of 
      kind-rank 
  """

  for r in ranks:
    if ranks.count(r) == n: return r
  return None
    
def two_pair(ranks):
  """ Takes a hand and check if it has two pairs """
  pair = kind(2, ranks)
  
  lowpair = kind(2, list(reversed(ranks))) 
  
  if pair and lowpair != pair: 
    return (pair, lowpair)
  else:
    return None 
  

def allmax(iterable, key=(lambda x: x)):
  """ Compares all hands in a list of lists (hands) and 
      finds the one with the maximum value or rank. 
      If there is a tie, both hands will be returned.
  """
  result, maxval = [], None
  for x in iterable:
    xval = key(x)
    if not result or xval > maxval:
      result, maxval = [x], xval
    elif xval == maxval:
      result.append(x)
  return result 
  
import random

def deal(numhands, n=5, 
          deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
  """ Deals hands for players. Each hand consist of 5 cards 
      that are randomly picked out of the shuffeled deck. 
      Numhands refer to number of hands.
  """
  random.shuffle(deck)
  return [deck[n*i:n*(i+1)] for i in range(numhands)]
  
  
def test():
	
	a = [2, 2, 2, 3, 3]
	b = [2, 2, 3, 3, 7]
	test_hands = [['6S', 'JD', 'TD', 'QS', '5H'], 
	              ['7D', '2S', 'AC', '8D', '4H'],
                ['7C', '7H', 'KD', 'KS', '2D'], 
                ['5S', '8C', 'AD', 'AS', '4D'], 
                ['5D', 'KC', 'JS', '9S', '8H']]
        hand_values = [(0, (12, 11, 10, 6, 5)), (0, (14, 8, 7, 4, 2)), 
                (2, (13, 7, 2)), (1, (14, 8, 5, 4)), 
                (0, (13, 11, 9, 8, 5))]
	
	assert card_ranks(['AS', '4S', '5C', '2D', 'KH']) == 
			  [14, 13, 5, 4, 2]
	assert allmax(hand_values) == [(2, (13, 7, 2))]
  	assert allmax(test_hands, key=hand_rank) == 
  	                [['7C', '7H', 'KD', 'KS', '2D']]
	assert poker(test_hands) == [['7C', '7H', 'KD', 'KS', '2D']]
	assert hand_rank(['7C', '7H', 'KD', 'KS', '2D']) == (2, (13, 7, 2))
	assert kind(1, a) == None
	assert kind(2, a) == 3
	assert kind(3, a) == 2
	assert kind(4, a) == None
	assert two_pair(b) == (2, 3)
	assert unzip([(3, 2), (1, 5), (1, 3)]) == [(3, 1, 1), (2, 5, 3)]
	assert group([2, 14, 5, 12, 5]) == 
	              [(2, 5), (1, 14), (1, 12), (1, 2)]
	
	return "The test was a success"

print test()

