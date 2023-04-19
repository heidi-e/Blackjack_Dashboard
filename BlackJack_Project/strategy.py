"""
Heidi Eren, Conor Doyle, Kelsey Nihezagirwe, Olivia Mintz
DS3500
Final project dashboard
4/19/23

"""

import pandas as pd

# load the BlackJack optimal solution into a pandas df
optimal_solution = pd.read_csv("BlackJack_Optimal_Solution.csv")


class Hand():

    def __init__(self, card_val1, card_val2):
        self.card_val1 = card_val1 # string value of the first card
        self.card_val2 = card_val2 # string value of the second card
        self.final_hand = [] # holds the final hand to find the suggested action

        # run the functions necessary to find the suggested action
        self.value_ten_cards()
        self.blackjack()
        self.duplicate_cards()
        self.if_ace_present()
        self.calculate_score()

    def if_ace_present(self):
        """
        if a card in the hand is an Ace, concatenate the cards together, A first
        """
        # only concatenate if the hand is not a blackjack
        if self.final_hand != ["You Have Blackjack!"]:
            # re-arrange the hands so that the A is always first
            if self.card_val1 == 'A':
                self.final_hand = [self.card_val1 + self.card_val2]

            elif self.card_val2 == 'A':
                self.final_hand = [self.card_val2 + self.card_val1]


    def value_ten_cards(self):
        """
        this function changes all the face cards to the proper ten values
        """
        face_cards = ['jack', 'queen', 'king', '10']

        # if there are two duplicate face cards, change both to T's
        if (self.card_val1 in face_cards) and (self.card_val2 in face_cards):
            self.card_val1 = "T"
            self.card_val2 = "T"

        # change each card to a 10 if they are a face card
        elif self.card_val1 in face_cards:
            self.card_val1 = "10"
        elif self.card_val2 in face_cards:
            self.card_val2 = "10"


    def duplicate_cards(self):
        """
        if the player's cards are the same, put them together without adding them
        """
        # put the two cards together Ex: 6,6 is 66.
        if self.card_val1 == self.card_val2:
            self.final_hand = [self.card_val1 + self.card_val2]

    def blackjack(self):
        """
        if the player wins the game by getting 21, update the message
        """

        # combine the cards to check for blackjack
        combined_cards = self.card_val1 + self.card_val2

        # check for blackjack and update the message
        if combined_cards == "A10" or combined_cards == "10A":
            self.final_hand = ["You Have Blackjack!"]


    def calculate_score(self):
        """
        calculates the sum of the player's hand if we still don't have a final hand
        """
        # if the final_hand is empty, calcuate the hand value
        if len(self.final_hand) == 0:
            self.final_hand = [str(int(self.card_val1) + int(self.card_val2))]

    def change_recommended(self, output):
        """
        changes the outputted strategy from the optimal_solution to something more user friendly
        """

        # change the abbreviated letter to the full action to give to the dashboard user
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
        gets the action to take based on the player's hand and the house's upcard
        """
        # if the final_hand is blackjack, then output the blackjack message
        if self.final_hand == ["You Have Blackjack!"]:
            return "You Have Blackjack!"

        # get the row in the optimal solution where the value is equal to the player hand
        row = optimal_solution[optimal_solution["value"] == self.final_hand[0]]

        # get the action at the house_upcard column (call change_housecard as well)
        action = row[self.change_housecard(house_upcard)]

        # return action altered by change_recommended
        return self.change_recommended(action.iloc[0])

    def change_housecard(self, house_upcard):
        """
        change the upcard to be compatible with our solution
        """

        face_cards = ["10","jack","queen","king"]

        # if the house_upcard is a face card, then return T, else return the given house upcard
        if house_upcard in face_cards:
            return "T"

        return house_upcard


"""def main():

    hand = Hand("jack", "10")



    #final = hand.get_action("3")

    print(hand.final_hand)





if __name__=="__main__":
    main()"""