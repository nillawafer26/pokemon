import random

class Move:
    def __init__(self, name, power, accuracy, move_type):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.move_type = move_type

    def use(self, attacker, defender):
        if random.random() <= self.accuracy:
            damage = self.calculate_damage(attacker, defender)
            defender.health -= damage
            print(f"{attacker.name} used {self.name}!")
            print(f"It dealt {damage:.2f} damage to {defender.name}.")
        else:
            print(f"{attacker.name}'s attack missed!")

    def calculate_damage(self, attacker, defender):
        base_damage = self.power * (attacker.attack / defender.defense)
        type_effectiveness = self.get_type_effectiveness(self.move_type, defender)
        base_damage *= type_effectiveness
        if random.random() < 0.1:
            print("Critical hit!")
            base_damage *= 1.5
        return base_damage

    def get_type_effectiveness(self, move_type, defender):
        type_chart = {
            ('Fire', 'Grass'): 2.0,
            ('Fire', 'Water'): 0.5,
            ('Water', 'Fire'): 2.0,
            ('Water', 'Grass'): 0.5,
            ('Grass', 'Water'): 2.0,
            ('Grass', 'Fire'): 0.5,
            ('Electric', 'Water'): 2.0, 
            ('Electric', 'Electric'): 1.0,  
            ('Electric', 'Ground'): 0.0,  
            ('Ground', 'Electric'): 2.0,  
            ('Ground', 'Fire'): 2.0,  
            ('Ground', 'Water'): 0.5,  
            ('Ground', 'Grass'): 0.5,  
            ('Ground', 'Flying'): 0.0,
        }
        return type_chart.get((move_type, defender.type), 1.0)

class Pokemon:
    def __init__(self, name, health, attack, defense, speed, type_, moves):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = type_
        self.moves = moves
    
    def is_alive(self):
        return self.health > 0

    def choose_move(self):
        print("Choose a move:")
        for i, move in enumerate(self.moves, 1):
            print(f"{i}. {move.name} (Power: {move.power})")
        choice = int(input(f"Select move (1 to {len(self.moves)}): ")) - 1
        return self.moves[choice]

def battle(pokemon1, pokemon2):
    print(f"A battle begins between {pokemon1.name} and {pokemon2.name}!")
    first, second = (pokemon1, pokemon2) if pokemon1.speed >= pokemon2.speed else (pokemon2, pokemon1)

    while pokemon1.is_alive() and pokemon2.is_alive():
        print(f"\n{first.name}'s Turn:")
        move = first.choose_move()
        move.use(first, second)
        if second.is_alive():
            print(f"{second.name} has {second.health:.2f} HP left.\n")
            print(f"{second.name}'s Turn:")
            move = second.choose_move()
            move.use(second, first)
            if first.is_alive():
                print(f"{first.name} has {first.health:.2f} HP left.\n")
        else:
            print(f"{second.name} has fainted!\n")
            break
        first, second = second, first

    winner = pokemon1 if pokemon1.is_alive() else pokemon2
    print(f"{winner.name} wins the battle!")

def main():
    tackle = Move("Tackle", power=40, accuracy=1.0, move_type='Normal')
    ember = Move("Ember", power=40, accuracy=0.9, move_type='Fire')
    water_gun = Move("Water Gun", power=40, accuracy=1.0, move_type='Water')
    vine_whip = Move("Vine Whip", power=45, accuracy=1.0, move_type='Grass')
    scratch = Move("Scratch", power=40, accuracy=1.0, move_type='Normal')
    flamethrower = Move("Flamethrower", power=90, accuracy=1.0, move_type='Fire')
    bubble = Move("Bubble", power=40, accuracy=1.0, move_type='Water')
    razor_leaf = Move("Razor Leaf", power=55, accuracy=0.95, move_type='Grass')
    stomping_tantrum = Move("Stomping Tantrum", power=75, accuracy=1.0, move_type='Ground')
    bonemerang = Move("Bonemerang", power=50, accuracy=0.9, move_type='Ground')
    thunderbolt = Move("Thunderblot", power=90, accuracy=1.0, move_type='Electric')
    thunder_punch = Move("Thunder Punch", power=75, accuracy=1.0, move_type='Electric')
    
    charmander = Pokemon(name="Charmander", health=100, attack=52, defense=43, speed=65, type_='Fire', moves=[ember, flamethrower, scratch, tackle])
    squirtle = Pokemon(name="Squirtle", health=100, attack=48, defense=65, speed=43, type_='Water', moves=[water_gun, bubble, tackle, ember])
    bulbasaur = Pokemon(name="Bulbasaur", health=100, attack=49, defense=49, speed=45, type_='Grass', moves=[vine_whip, razor_leaf, tackle, scratch])
    cubone = Pokemon(name="Cubone", health=100, attack=50, defense=95, speed=35, type_='Ground', moves=[stomping_tantrum, tackle, scratch, bonemerang])
    pikachu = Pokemon(name="Pikachu", health=100, attack=55, defense=40, speed=90, type_='Electric', moves=[thunderbolt, tackle, scratch, thunder_punch])

    pokemon_list = [charmander, squirtle, bulbasaur, cubone, pikachu]

    player_pokemon = random.choice(pokemon_list)
    opponent_pokemon = random.choice(pokemon_list)
    while player_pokemon == opponent_pokemon:
        opponent_pokemon = random.choice(pokemon_list)

    print(f"You are fighting with {player_pokemon.name}!")
    print(f"Your opponent is {opponent_pokemon.name}!\n")
    
    battle(player_pokemon, opponent_pokemon)

if __name__ == "__main__":
    main()