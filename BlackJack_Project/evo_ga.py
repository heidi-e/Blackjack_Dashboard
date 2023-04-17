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

def simple_strategy_agent(player_hand, dealer_upcard):
    player_total = sum(player_hand)
    if player_total >= 17:
        return "stand"
    if player_total <= 11:
        return "hit"
    if player_total == 12:
        if dealer_upcard in [4, 5, 6]:
            return "stand"
        else:
            return "hit"
    if player_total in [13, 14, 15, 16]:
        if dealer_upcard in [2, 3, 4, 5, 6]:
            return "stand"
        else:
            return "hit"
    return "stand"

def run_blackjack_evo():
    # Set up the Evo framework
    evo = Evo()
    evo.add_fitness_criteria("win_pct", blackjack_objective())
    evo.add_agent("simple_strategy_agent", simple_strategy_agent, k=2)

    # Initialize the population with random solutions
    for i in range(100):
        evo.add_solution(random_agent())

    # Run the evolution process
    evo.evolve(n=1000, dom=50, status=50)

    # Get the best solution and its fitness score
    best_solution, best_score = max(evo.pop.items(), key=lambda x: x[0][1])

    # Print the best solution and its fitness score
    print("Best Solution:")
    print(best_solution)
    print("Fitness Score:")
    print(best_score[1])

# Run the blackjack evolution process
run_blackjack_evo()


def main():
    run_blackjack_evo()

if __name__ == "__main__":
    main()


