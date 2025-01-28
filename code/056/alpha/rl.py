import pygame as pg
import sys
import random
import neat
import os
import pickle

pg.init()

WIDTH, HEIGHT = 800, 600
REZ = 100

class Tile:
    def __init__(self, i, j, plate=False):
        self.x = i
        self.y = j
        self.rect = pg.Rect(self.x, self.y, REZ, REZ)
        self.plate = plate

    def draw(self, screen):
        pg.draw.rect(screen, "white", self.rect, 1)
        if self.plate:
            pg.draw.rect(screen, "green", self.rect)

class Map:
    def __init__(self):
        self.grid = []
        self.plate_x = random.randint(0, (WIDTH // REZ - 1))
        self.plate_y = random.randint(0, (HEIGHT // REZ - 1))

        for i in range(HEIGHT // REZ):
            row = []
            for j in range(WIDTH // REZ):
                if i == self.plate_y and j == self.plate_x:
                    row.append(Tile(j * REZ, i * REZ, True))
                else:
                    row.append(Tile(j * REZ, i * REZ))
            self.grid.append(row)

    def draw(self, screen):
        for row in self.grid:
            for tile in row:
                tile.draw(screen)

    def set_plate(self):
        self.grid[self.plate_y][self.plate_x].plate = False
        self.plate_x = random.randint(0, (WIDTH // REZ - 1))
        self.plate_y = random.randint(0, (HEIGHT // REZ - 1))
        self.grid[self.plate_y][self.plate_x].plate = True

class Agent:
    def __init__(self, map):
        self.pos_x = random.randint(0, (WIDTH // REZ - 1))
        self.pos_y = random.randint(0, (HEIGHT // REZ - 1))
        self.map = map.grid
        self.w_map = map
        self.tile = map.grid[self.pos_y][self.pos_x]
        self.draw_x = self.tile.x
        self.draw_y = self.tile.y
        self.rect = pg.Rect(self.draw_x, self.draw_y, REZ, REZ)
        self.counter = 0
        self.alive = True

    def draw(self, screen):
        pg.draw.rect(screen, "orange", self.rect)

    def move_up(self):
        if self.pos_y != 0:
            self.pos_y -= 1
            self.update_position()

    def move_down(self):
        if self.pos_y != (HEIGHT // REZ - 1):
            self.pos_y += 1
            self.update_position()

    def move_left(self):
        if self.pos_x != 0:
            self.pos_x -= 1
            self.update_position()

    def move_right(self):
        if self.pos_x != (WIDTH // REZ - 1):
            self.pos_x += 1
            self.update_position()

    def update_position(self):
        self.tile = self.map[self.pos_y][self.pos_x]
        self.draw_x = self.tile.x
        self.draw_y = self.tile.y
        self.rect = pg.Rect(self.draw_x, self.draw_y, REZ, REZ)

    def update(self, screen):
        self.counter += 1
        if self.counter > 600:
            self.alive = False

        if self.tile.plate:
            self.counter = 0
            self.w_map.set_plate()

        self.draw(screen)

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        w_map = Map()
        player = Agent(w_map)
        fitness = 0
        while player.alive:
            # Define your inputs to the neural network (e.g., agent's position and target's position)
            inputs = [player.pos_x, player.pos_y, player.tile.x, player.tile.y]
            action = net.activate(inputs)
            max_action = max(action)
            if action.index(max_action) == 0:
                player.move_up()
            elif action.index(max_action) == 1:
                player.move_down()
            elif action.index(max_action) == 2:
                player.move_left()
            elif action.index(max_action) == 3:
                player.move_right()

            fitness += 1  # Reward for staying alive

        genome.fitness = fitness

def run_neat(config):
    # Create the population, which is the top-level object for a NEAT run
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 50 generations
    winner = p.run(eval_genomes, 50)
    
    # Save the winner
    with open('winner.pkl', 'wb') as f:
        pickle.dump(winner, f)

    print('\nBest genome:\n{!s}'.format(winner))

def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    w_map = Map()
    player = Agent(w_map)

    # Load NEAT configuration
    config_path = os.path.join(os.path.dirname(__file__), 'config-feedforward')
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    # Run NEAT algorithm
    run_neat(config)

    while player.alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    player.move_up()
                if event.key == pg.K_s:
                    player.move_down()
                if event.key == pg.K_a:
                    player.move_left()
                if event.key == pg.K_d:
                    player.move_right()

        screen.fill("black")
        w_map.draw(screen)
        player.update(screen)

        clock.tick(60)
        pg.display.update()

if __name__ == "__main__":
    main()

