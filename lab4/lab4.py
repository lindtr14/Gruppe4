def poker(hands):
  return allmax(hands, key=hand_rank)
  
def hand_rank(hand):
  groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
  counts, ranks = unzip(groups)
  if ranks == (14, 5, 4, 3, 2):
    ranks = (5, 4, 3, 2, 1) 
  straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
  flush = len(set([s for r, s in hand])) == 1
  return max(count_rankings[counts], 4*straight + 5*flush), ranks
  
  count_rankings = {(5,):10, (4,1):7, (3,2):6, (3,1,1):3, (2,2,1):2, (2,1,1,1):1, (1,1,1,1,1):0}

def group(items):
  groups = [(items.count(x), x) for x in set(items)]
  return sorted(groups, reverse=True)
  
def unzip(pairs): return zip(*pairs)
  
def card_ranks(hand):
  ranks = ["--23456789TJQKA".index(r) for r,s in hand]
  ranks.sort(reverse=True)
  return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
  
def straight(ranks):
  return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
  
def flush(hand):
  suits = [s for r, s in hand]
  return len(set(suits)) == 1
  
def kind(n, ranks):
  for r in ranks:
    if ranks.count(r) == n: return r
  return None
    
def two_pair(ranks):
  pair = kind(2, ranks) # Finding two cards that has the same value. Give them the name "pair". 
                        # This will pick out the highest pair first
  lowpair = kind(2, list(reversed(ranks))) # Finding two cards that has the same value, but in a reversed list. 
                                           # Since its reversed, this will pick out the lowest pair
  if pair and lowpair != pair: # Checking if pair and lowpair is NOT the same
    return (pair, lowpair) # If the "if" is true, then return their values
  else:
    return None # Else return None
  
def allmax(iterable, key=(lambda x: x)):
  result, maxval = [], None
  for x in iterable:
    xval = key(x)
  if not result or xval > maxval:
    result, maxval = [x], xval
  elif xval == maxval:
    result.append(x)
  return result 
  
# importing the module random to help us pick out random cards from the deck
import random

# numhands are the input. You insert how many players/hands you want in game
# n=5 will be how many cards each player/hand will have
# deck=[r+s for r in '23456789TJQKA' for s in ‘SHDC'] is defining our deck as a list to have cards with r’s and s’s. 
# Every card is a combination with one r and one s

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
  
# This method is picked out from our random module
# It shuffles our deck in a random order
  random.shuffle(deck)
  
# returns a hand for a player. The hands consists of 5 cards that are randomly picked out of the shuffled deck.
# Since n is 5, and i is 0, we put those numbers instead of the characters and get
# deck[5*0:n*(0+1)]
# deck[0:5]
# This will pick out the first five cards in our deck 
# If we have more than one player we move on to the next player
# and our program will do the same mathematic expression, but this time i = 1 and not i = 0
# The line will stop when we have reached the number of players as defined in numhands

  return [deck[n*i:n*(i+1)] for i in range(numhands)]
