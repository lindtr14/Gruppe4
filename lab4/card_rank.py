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
            #   Hvordan sjekke verdien til en string (lavere enn 10)?
            if card == suit:
                cardList.append(number)
    cardList.sort(reverse=True)
    return cardList
                
                
#print card_rank(cards)
