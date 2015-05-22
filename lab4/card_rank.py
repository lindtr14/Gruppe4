# -*- coding:utf-8 -*-

rankMapping = (("2", 2),
               ("3", 3),
               ("4", 4),
               ("5", 5),
               ("6", 6),
               ("7", 7),
               ("8", 8),
               ("9", 9),
               ("T", 10),
               ("J", 11),
               ("Q", 12),
               ("K", 13),
               ("A", 14))
               
#cards = ['AS', '4S', '5C', '2D', 'KH']

def card_rank(cards):
    cardList = []
    ranks = [r for r,s in cards]
    for suit, number in rankMapping:
        for card in ranks:
            if card == suit:
                cardList.append(number)
    cardList.sort(reverse=True)
    return cardList
    
    
def test():
    assert card_rank(['AS', '4S', '5C', '2D', 'KH']) == [14, 13, 5, 4, 2]
    return "Test fullført"
#print card_rank(cards)

print test()
