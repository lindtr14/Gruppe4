#   Takes all the hands made by the deal function. The hands comes as
#   a list of lists (hands). Then every hand will be sorted and given
#   a rank (hand_rank) in turn, one after the other.
#   The allmax function will then find wich one is the highest ranking
#   hand or hands if there is a tie.
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

def group(items): # Takes a list of items and returns a list of "counts" of items and the list itself
  groups = [(items.count(x), x) for x in set(items)] # Goes through set(items) and returns pairs of the "count" and set and sorts them in reversed order so that the highest comes first
  return sorted(groups, reverse=True) 
  
def unzip(pairs): return zip(*pairs) # Converts a list of pairs into a pair of lists 
  
def card_ranks(hand):
  ranks = ["--23456789TJQKA".index(r) for r,s in hand]
  ranks.sort(reverse=True)
  return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
  
def straight(ranks):
  return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
  
def flush(hand):
  suits = [s for r, s in hand]
  return len(set(suits)) == 1
  
# n is the input for what kind of rank «kind» we want to find. 2 for two of a kind (1pair), 
# 3 for three of a kind, 4 for four of a kind
# ranks will be our hand or the list of card we got

def kind(n, ranks):
  
# this for expression will check in our ranks/list if it can count how many r are alike, depending on what number we defined in n
# if we said n = 3, the for expression will try to find if it can find 3 r’s that are the same. 
# If it is, it will return that r value. If not it will return none
# count is a method in lists

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
  
#   Compares all the hands in a list of lists (hands) and finds the one
#   with the maximum value or rank. If there is a tie, both hands will
#   be returned.
#   The key=(lambda x: x) means that key(x) will take the next hand in 
#   the loop and assign it to the variable xval. Lambda does the same as a
#   function, only it takes less space and return a value without any
#   return statement. The first x is the paramenter.
def allmax(iterable, key=(lambda x: x)):
  """The result will be a list of hands, initially empty. The maxval will
  be the maximum value in the iterable, initially none."""
  result, maxval = [], None
  """For each hand in iterable, apply the lambda key to x and put it in
  xval."""
  for x in iterable:
    xval = key(x)
  """ If there is no result (the first time in the loop), then make
  result have the value of that hand in a list. Or if xval (current
  hand), is greater than the value of maxval (the best hand), make
  maxval to be the value of xval (a new best hand)."""
  if not result or xval > maxval:
    result, maxval = [x], xval
  """ If the value of xval (the next hand) is equal to the maxval (the
  best hand), then append that hand to the result variable. This
  means that result will now have at least two identical hands in its
  list of hands."""
  elif xval == maxval:
    result.append(x)
  """ Return the result, which could be a list of one hand, or more if
  there is a tie."""
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
