"""
Code will sum the cards unless

If one is an Ace -> lookup "AOther_Value"
 string + string

If the same card, attach them together but don't add them

Change 10's to T's
If user has a 10 card then change it to a T

If user gets A + T then print user wins no action needed


"""
"""
def funciton:
    one_card = 10
    two_card = 5

    if ace:
        
    elif same_card:
    
    elif:
        lookup(one_card+two_card, house_upcard)"""




def basic_strategy(player_total, dealer_value, soft):
    """ This is a simple implementation of Blackjack's
        basic strategy. It is used to recommend actions
        for the player. """

    if 4 <= player_total <= 8:
        return 'hit'
    if player_total == 9:
        if dealer_value in [1,2,7,8,9,10]:
            return 'hit'
        return 'double'
    if player_total == 10:
        if dealer_value in [1, 10]:
            return 'hit'
        return 'double'
    if player_total == 11:
        if dealer_value == 1:
            return 'hit'
        return 'double'
    if soft:
        #we only double soft 12 because there's no splitting
        if player_total in [12, 13, 14]:
            if dealer_value in [5, 6]:
                return 'double'
            return 'hit'
        if player_total in [15, 16]:
            if dealer_value in [4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 17:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 18:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            if dealer_value in [2, 7, 8]:
                return 'stand'
            return 'hit'
        if player_total >= 19:
            return 'stand'

    else:
        if player_total == 12:
            if dealer_value in [1, 2, 3, 7, 8, 9, 10]:
                return 'hit'
            return 'stand'
        if player_total in [13, 14, 15, 16]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            return 'hit'

        if player_total >= 17:
            return 'stand'