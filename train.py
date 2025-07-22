from game import Game
import random
import numpy as np
import pickle
from ai import NeuralNetwork

def game_logic(net:NeuralNetwork,n):
    game = Game()
    
    while not game.game_over:
        if game.count > n:
            break
        states, actions = game.simulate()
        
        best_score = float('-inf')
        best_action = None

        for grid, action in zip(states, actions):
            features = np.array(game.get_features(grid))
            score = net.forward(features)
            
            if score > best_score:
                best_score = score
                best_action = action
        
        if best_action:
            rotation, move = best_action
            for _ in range(rotation):
                game.rotate(0)
            if move < 0:
                for _ in range(abs(move)):
                    game.move_left()
            elif move > 0:
                for _ in range(move):
                    game.move_right()
            while True:
                if not game.move_down(): break
        else:
            break
    return game.score

def genetic_algorithm(population_size,generations,mutation_rate,top_k,elite_k,pieces,game):
    population = [NeuralNetwork(input_size, hidden_size, output_size, hidden_layers) for _ in range(population_size)]

    for generation in range(generations):#run more times, punish variance
        print(f'Generation {generation + 1}')
        fitness_scores = [(game(net,pieces), net) for net in population]
        fitness_scores.sort(key=lambda x: x[0], reverse=True)

        top = [net for _, net in fitness_scores[:top_k]]#parents
        new_population = [clone(net) for _,net in fitness_scores[:elite_k]]#elites
        
        while len(new_population) < population_size:
            x1, x2 = random.sample(top,2)
            child = crossover(x1,x2)
            child.mutate(mutation_rate)
            new_population.append(child)

        population = new_population
        print(f'Best Score: {fitness_scores[0][0]}')#survival rate, average score, death situation
    return fitness_scores[0][1]

def crossover(x1:NeuralNetwork, x2:NeuralNetwork):
    y = NeuralNetwork(x1.input_size, x1.hidden_size, x1.output_size, x1.hidden_layers)
    for i in range(len(x1.weights)):
        mask = np.random.rand(*x1.weights[i].shape) > 0.5
        y.weights[i] = x1.weights[i] * mask + x2.weights[i] * (~mask)
        mask_b = np.random.rand(*x1.biases[i].shape) > 0.5
        y.biases[i] = x1.biases[i] * mask_b + x2.biases[i] * (~mask_b)
    return y

def clone(x:NeuralNetwork):
    y = NeuralNetwork(x.input_size, x.hidden_size, x.output_size, x.hidden_layers)
    for i in range(len(x.weights)):
        y.weights[i] = np.copy(x.weights[i])
        y.biases[i] = np.copy(x.biases[i])
    return y

if __name__ == '__main__':
    input_size = 4
    hidden_size = 10
    output_size = 1
    hidden_layers = 2
    population_size = 100
    generations = 4
    mutation_rate = 0.07  
    top_k = 12
    elite_k = 4
    pieces = 500

    best_net = genetic_algorithm(population_size, generations, mutation_rate, top_k, elite_k, pieces, game_logic)

    with open("models/mynet4", 'wb') as f:
        pickle.dump(best_net, f)