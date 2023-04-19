"""

this file is where we're implementing the actual project helper strategy

"""

import pandas as pd

optimal_solution = pd.read_csv("BlackJack_Optimal_Solution.csv")
"""
print(optimal_solution)
row = optimal_solution[optimal_solution["value"] == '13']
print(row["7"])

"""

# sample card inputs you would input the user inputs and those should work, (I havent implemented face cards as T)
# update: I have done it
# Aother_value is supposed to be used for when you can use A as either 11 or 1
"""CARD_VALUES = {'A': 11, "AOther_Value": 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10}"""


class Hand():

    def __init__(self, card_val1, card_val2):
        #self.cards = [] # holds the individual cards of the player (ex: A through K)
        self.card_val1 = card_val1 # string value of the first card
        self.card_val2 = card_val2 # string value of the second card
        self.final_hand = [] # holds the final hand to find the suggested action

        self.value_ten_cards()
        self.blackjack()
        self.duplicate_cards()
        self.if_ace_present()
        self.calculate_score()

    def if_ace_present(self):
        """
        if the hand of the player is an Ace, concatenate the cards together
        """
        if self.final_hand != ["You Have Blackjack!"]:
            if self.card_val1 == 'A':
                self.final_hand = [self.card_val1 + self.card_val2]
                """ace_value = CARD_VALUES['A']
                self.user_hand.append(ace_value + CARD_VALUES[self.card_val2])
                self.user_hand[0] = str(self.cards[0]) + str(self.cards[1])"""
            elif self.card_val2 == 'A':
                self.final_hand = [self.card_val2 + self.card_val1]
                """ace_value = CARD_VALUES['A']
                self.user_hand.append(ace_value + CARD_VALUES[self.card_val1])
                self.user_hand[0] = str(self.cards[0]) + str(self.cards[1])"""


        #self.check_blackjack()

        #return ''.join(map(str, self.user_hand))

    def value_ten_cards(self):
        """
        if the hand has a pair of face cards, change them both to T's and update final
        otherwise, change the face cards to 10's


        """
        face_cards = ['jack', 'queen', 'king']

        if (self.card_val1 in face_cards) and (self.card_val2 in face_cards):
            #print("Test")
            self.card_val1 = "T"
            self.card_val2 = "T"
        elif self.card_val1 in face_cards:
            self.card_val1 = "10"
        elif self.card_val2 in face_cards:
            self.card_val2 = "10"


        #self.user_hand = ''.join(card_vals) # somehow this outputs a much prettier string without the brackets

        #return self.user_hand

    def duplicate_cards(self):
        """
        if the player's cards are the same, put them together
        basically just put them together and add this to the list one element

        """
        if self.card_val1 == self.card_val2:
            self.final_hand = [self.card_val1 + self.card_val2]

    def blackjack(self):
        """
        if the player wins the game by getting 21 (I don't really think we need to keep this one but... u got it :)

        """

        combined_cards = self.card_val1 + self.card_val2
        if combined_cards == "A10" or combined_cards == "10A":
            self.final_hand = ["You Have Blackjack!"]




    def calculate_score(self):
        """
        calculates the sum of the player's hand (doesn't work yet it only outputs zero when I run it you can edit it)
        """
        if len(self.final_hand) == 0:
            self.final_hand = [str(int(self.card_val1) + int(self.card_val2))]

    def change_recommended(self, output):
        """
        changes the outputted strategy from the optimal_solution to something more user friendly
        """

        if output == "S":
            return "Stand"
        elif output == "H":
            return "Hit"
        elif output == "D":
            return "Double-Down"
        elif output == "P":
            return "Split"


    def get_action(self, house_upcard):
        """
        gets the action to take based on the player's hand and the house's upcard (this doesnt work
        one only returns an empty set)

        """
        # if blackjack, don't lookup and return the action

        #user_value = ''.join(self.final_hand)
        row = optimal_solution[optimal_solution["value"] == self.final_hand[0]]
        action = row[self.change_housecard(house_upcard)]
        return self.change_recommended(action.iloc[0])
        #return self.change_recommended(action)

    def change_housecard(self, house_upcard):
        """
        change the upcard to be compatible with our solution
        """
        face_cards = ["10","jack","queen","king"]
        if house_upcard in face_cards:
            return "T"

        return house_upcard


def main():

    hand = Hand("4", "8")

    final = hand.get_action("3")

    print(final)





if __name__=="__main__":
    main()