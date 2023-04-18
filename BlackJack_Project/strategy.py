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

import pandas as pd

optimal_solution = pd.read_csv("BlackJack_Optimal_Solution.csv")

print(optimal_solution)
row = optimal_solution[optimal_solution["value"] == '13']
print(row["7"])


def if_ace_present():
    """
    if the hand of the player is an Ace, concatenate the cards together
    """
    pass

def value_ten_cards():
    """
    whenever a face card is pulled, change the value to ten and make it into a T
    # if they are dupplicates do sumthing

    if they are not do something else

    """
    pass


def duplicate_cards():
    """
    if the player's cards are the same, put them together


    :return:
    """
    pass


def blackjack():
    """
    if the player wins the game by getting 21

    """
    pass

def calculate_score(hand):
    """
    calculates the sum of the player's hand
    """
    pass


def get_action():
    """

    :return:
    """