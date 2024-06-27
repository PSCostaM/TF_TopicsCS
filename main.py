# /mnt/data/pokemon_simulation.py

from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.visualization.modules import CanvasGrid, TextElement
from mesa.visualization.ModularVisualization import ModularServer
import random

type_advantages = {
    'agua': {'ventaja': ['fuego'], 'desventaja': ['eléctrico']},
    'fuego': {'ventaja': ['planta'], 'desventaja': ['agua']},
    'eléctrico': {'ventaja': ['agua'], 'desventaja': ['planta']},
    'planta': {'ventaja': ['agua'], 'desventaja': ['fuego']}
}

class Pokemon(Agent):
    def __init__(self, unique_id, model, tipo, name):
        super().__init__(unique_id, model)
        self.tipo = tipo
        self.name = name
        self.active = True

    def step(self):
        if not self.active:
            return
        if self.model.chasing_mode:
            self.chase()
        else:
            self.move()
        self.fight()

    def move(self):
        target = self.find_target()
        if target:
            self.model.grid.move_agent(self, target)
        else:
            possible_steps = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False
            )
            valid_steps = [step for step in possible_steps if self.model.grid.is_cell_empty(step)]
            if valid_steps:
                new_position = random.choice(valid_steps)
                self.model.grid.move_agent(self, new_position)

    def chase(self):
        opponent = self.find_opponent()
        if opponent:
            self.model.grid.move_agent(self, opponent)
        else:
            possible_steps = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False
            )
            valid_steps = [step for step in possible_steps if self.model.grid.is_cell_empty(step)]
            if valid_steps:
                new_position = random.choice(valid_steps)
                self.model.grid.move_agent(self, new_position)

    def find_target(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=5)
        for neighbor in neighbors:
            if neighbor.active:
                return neighbor.pos
        return None

    def find_opponent(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=5)
        for neighbor in neighbors:
            if neighbor.active:
                return neighbor.pos
        return None

    def fight(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            opponent = random.choice(cellmates)
            if opponent != self and opponent.active:
                winner = self.battle(opponent)
                loser = opponent if winner == self else self
                self.model.grid.remove_agent(loser)
                self.model.schedule.remove(loser)

    def battle(self, opponent):
        if self.tipo in type_advantages and opponent.tipo in type_advantages:
            if opponent.tipo in type_advantages[self.tipo]['ventaja']:
                return self
            elif opponent.tipo in type_advantages[self.tipo]['desventaja']:
                return opponent
        return random.choice([self, opponent])

class PokemonWorld(Model):
    def __init__(self, N):
        self.num_pokemons = N
        self.grid = MultiGrid(50, 50, False)  # Set torus to False to make the grid non-toroidal
        self.schedule = RandomActivation(self)
        self.running = True
        self.chasing_mode = False
        self.winning_pokemon = None
        types = list(type_advantages.keys())

        for i in range(self.num_pokemons):
            tipo = random.choice(types)
            name = f"Pokemon_{i+1}"
            pokemon = Pokemon(i, self, tipo, name)
            self.schedule.add(pokemon)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(pokemon, (x, y))

    def step(self):
        self.schedule.step()
        if self.check_winner():
            self.running = False

    def check_winner(self):
        active_pokemons = [agent for agent in self.schedule.agents if agent.active]
        if len(active_pokemons) == 1:
            winning_pokemon = active_pokemons[0]
            self.winning_pokemon = winning_pokemon
            print(f"The winning Pokémon is {winning_pokemon.name} of type {winning_pokemon.tipo}!")
            return True
        elif len(active_pokemons) == 2:
            self.chasing_mode = True
            print("Chasing mode activated!")
        else:
            self.chasing_mode = False
        return False

class ChasingModeIndicator(TextElement):
    def render(self, model):
        if model.chasing_mode:
            return "Chasing Mode: ACTIVE"
        else:
            return "Chasing Mode: INACTIVE"

class WinningPokemonIndicator(TextElement):
    def render(self, model):
        if model.winning_pokemon:
            return f"Winning Pokémon: {model.winning_pokemon.name} (Type: {model.winning_pokemon.tipo})"
        else:
            return "Winning Pokémon: NONE"

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    if agent.tipo == 'agua':
        portrayal["Color"] = "blue"
    elif agent.tipo == 'fuego':
        portrayal["Color"] = "red"
    elif agent.tipo == 'eléctrico':
        portrayal["Color"] = "yellow"
    elif agent.tipo == 'planta':
        portrayal["Color"] = "green"
    portrayal["Layer"] = 0
    return portrayal

# Adjust the CanvasGrid to center in the default view
grid = CanvasGrid(agent_portrayal, 50, 50, 1000, 1000)
chasing_mode_indicator = ChasingModeIndicator()
winning_pokemon_indicator = WinningPokemonIndicator()
server = ModularServer(PokemonWorld, [grid, chasing_mode_indicator, winning_pokemon_indicator], "Pokemon World", {"N": 2500})
server.port = 8521
server.launch()
