import random

# Define the rules of blackjack
CARD_VALUES = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
DEALER_HIT_THRESHOLD = 17

# Define the parameters of the genetic algorithm
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 20

# Define the initial population of candidate strategies
def generate_population():
    population = []
    for i in range(POPULATION_SIZE):
        strategy = []
        for j in range(12):
            strategy.append(random.choice(['hit', 'stand']))
        population.append(strategy)
    return population

# Evaluate the fitness of a strategy by simulating multiple games
def evaluate_fitness(strategy):
    total_score = 0
    for i in range(100):
        player_score, dealer_score = simulate_game(strategy)
        if player_score > 21:
            total_score -= 1
        elif dealer_score > 21 or player_score > dealer_score:
            total_score += 1
        else:
            total_score -= 1
    return total_score

# Simulate a game using the given strategy
def simulate_game(strategy):
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    while should_hit(player_score, dealer_score, strategy):
        player_hand.append(deck.pop())
        player_score = calculate_score(player_hand)
        if player_score > 21:
            break
    while dealer_score < DEALER_HIT_THRESHOLD:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21:
            break
    return player_score, dealer_score

# Determine whether the player should hit or stand based on the current strategy
def should_hit(player_score, dealer_score, strategy):
    index = min(player_score - 4, 11)
    return strategy[index] == 'hit'

# Calculate the score of a hand
def calculate_score(hand):
    score = 0
    num_aces = 0
    for card in hand:
        if card == 'A':
            num_aces += 1
        score += CARD_VALUES[card]
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1
    return score

# Perform single-point crossover on two parent strategies
def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutate a strategy by randomly changing some of its decisions
def mutate(strategy):
    for i in range(len(strategy)):
        if random.random() < MUTATION_RATE:
            strategy[i] = random.choice(['hit', 'stand'])

# Evolve the population using a tournament selection and single-point crossover
def evolve():
    # Generate the initial population of candidate strategies
    population = generate_population()
    # Evolve the population over multiple generations
    for generation in range(GENERATIONS):
        print("Generation:", generation)
        # Select the parents for the next generation using tournament selection
        parents = []
        for i in range(POPULATION_SIZE // 2):
            tournament = random.sample(population, 5)
            tournament.sort(key=lambda x: evaluate_fitness(x), reverse=True)
            parents += tournament[:2]
        # Create the next generation by performing single-point crossover on the parents
        children = []
        for i in range(POPULATION_SIZE // 2):
            parent1, parent2 = parents[2*i], parents[2*i+1]
            child1 = single_point_crossover(parent1, parent2)
            child2 = single_point_crossover(parent2, parent1)
            children += [child1, child2]
        # Mutate the children of the next generation
        for child in children:
            mutate(child)
        # Combine the parents and children to form the new population
        population = parents + children
        # Sort the population by fitness and keep the top candidates for the next generation
        population.sort(key=lambda x: evaluate_fitness(x), reverse=True)
        population = population[:POPULATION_SIZE]
    # Print the best strategy found by the genetic algorithm
    best_strategy = population[0]
    print("Best strategy found:")
    print(best_strategy)
    print("Fitness:", evaluate_fitness(best_strategy))


def main():



    evolve()



if __name__=="__main__":
    main()


