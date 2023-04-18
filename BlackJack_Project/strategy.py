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
CARD_VALUES = {'A': 11, "AOther_Value": 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10}


class Hand():

    def __init__(self, card_val1, card_val2):
        self.cards = [] # holds the individual cards of the player (ex: A through K)
        self.card_val1 = card_val1 # string value of the first card
        self.card_val2 = card_val2 # string value of the second card
        self.user_hand = [card_val1, card_val2] # holds the integer value of the cards in the user's hand

    def if_ace_present(self):
        """
        if the hand of the player is an Ace, concatenate the cards together
        """
        if self.card_val1 == 'A':
            self.user_hand[0] = self.card_val1
            self.user_hand[1] = self.card_val2
            """ace_value = CARD_VALUES['A']
            self.user_hand.append(ace_value + CARD_VALUES[self.card_val2])
            self.user_hand[0] = str(self.cards[0]) + str(self.cards[1])"""
        elif self.card_val2 == 'A':
            self.user_hand[0] = self.card_val2
            self.user_hand[1] = self.card_val1
            """ace_value = CARD_VALUES['A']
            self.user_hand.append(ace_value + CARD_VALUES[self.card_val1])
            self.user_hand[0] = str(self.cards[0]) + str(self.cards[1])"""
        else:
            self.cards.append(self.card_val1)
            self.cards.append(self.card_val2)
            self.user_hand.append(CARD_VALUES[self.card_val1] + CARD_VALUES[self.card_val2])

        #self.check_blackjack()

        return ''.join(map(str, self.user_hand))

    def value_ten_cards(self):
        """
        whenever a face card is pulled, change the value to ten and make it into a T
        # if the face cards are duplicates use the duplicate function

        if they are not do original task of making them T in our user hand with a value often

        """
        face_cards = ['10', 'J', 'Q', 'K']
        card_vals = [self.card_val1, self.card_val2]

        """if card_vals[0] == card_vals[1]:
            self.duplicate_cards()
            #return self.user_hand"""

        for i in range(2):
            if card_vals[i] in face_cards:
                card_vals[i] = 'T'

        self.user_hand = ''.join(card_vals) # somehow this outputs a much prettier string without the brackets

        #return self.user_hand

    """def duplicate_cards(self):
        """
        #if the player's cards are the same, put them together

        """
        self.user_hand = self.card_val1 + self.card_val2"""

    def blackjack(self):
        """
        if the player wins the game by getting 21 (I don't really think we need to keep this one but... u got it :)

        """


        pass

    def calculate_score(self):
        """
        calculates the sum of the player's hand (doesn't work yet it only outputs zero when I run it you can edit it)
        """
        total = 0
        for val in self.user_hand:
            if len(val) == 0:
                total += CARD_VALUES[val[1]]
            else:
                total += CARD_VALUES[val]

        return total

    def get_action(self, house_upcard):
        """
        gets the action to take based on the player's hand and the house's upcard (this doesnt work
        one only returns an empty set)

        """
        user_value = ''.join(self.user_hand)
        row = optimal_solution[optimal_solution["value"] == user_value]
        action = row[house_upcard]
        return action


def main():

    hand = Hand("8", "9")


    # run 10 before ace_one, because the ace_one uses the 10
    if ace_one:
        #blackjack()

    elif

    else:
        calculate_score()

    # any duplicate cards will be left as [card_1, card_2]



    #get_action()      this just combines the list in user_hand


    score = hand.calculate_score()
    print(score)

    #hand1 = Hand("8", "9")
    #c = hand1.get_action("A")
    #print(c)

    hand = Hand("8", "9")
    hand.if_ace_present()

    hand = Hand("8", "9")
    hand.duplicate_cards()

    hand = Hand("8", "9")
    hand.blackjack()

    hand = Hand("8", "9")
    score = hand.calculate_score()
    print(score)
    #action = hand.get_action("A")
    #print(f"The player's hand has a value of {score} and should {action}")





if __name__=="__main__":
    main()