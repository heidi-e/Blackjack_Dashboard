from evo import Evo
import random as rnd


def blackjack_objective(hand):
    value = sum(hand)
    if value > 21:
        return -100  # penalty for going over 21
    else:
        return -abs(value - 21)


def random_agent(hand):
    action = rnd.choice(['hit', 'stand'])
    if action == 'hit':
        hand.append(rnd.randint(1, 10))
    return hand

def simple_strategy_agent(hand, dealer_upcard):
    value = sum(hand)
    if value >= 17:
        return hand  # stand if value is 17 or higher
    elif value <= 11:
        hand.append(10)  # hit if value is 11 or lower
    elif dealer_upcard >= 7:
        hand.append(rnd.randint(1, 3))  # hit with 1/3 probability if dealer's upcard is 7 or higher
    else:
        hand.append(rnd.randint(1, 4))  # hit with 1/4 probability if dealer's upcard is 6 or lower
    return hand





def main():
    blackjack_evo = Evo()

    # add objective function
    blackjack_evo.add_fitness_criteria('blackjack', blackjack_objective)

    # add agents
    blackjack_evo.add_agent('random', random_agent, k=1)
    blackjack_evo.add_agent('simple', simple_strategy_agent, k=2)

    # run the optimization for 10000 iterations
    blackjack_evo.evolve(n=10000, dom=100, status=1000)

    # print the best solution
    best_solution = max(blackjack_evo.pop, key=lambda x: x[1]['blackjack'])
    print("Best solution:", best_solution[0], "with objective value:", best_solution[1]['blackjack'])


if __name__ == "__main__":
    main()


