def target_num(targets):
        if targets > 1:
            target_mod = 0.75
        else:
            target_mod = 1

        return target_mod
        
def weather_modifier(weather, move_type):
        if weather == 'rain' and move_type == 'water' or weather == 'harsh sunlight' and move_type == 'fire':
            weather_mod = 1.5
        elif weather == 'rain' and move_type == 'fire' or weather == 'harsh sunlight' and move_type == 'water':
            weather_mod = 0.5
        else:
            weather_mod = 1
        return weather_mod


class UserPokemon:
    # probs gonna have to pass some of these in but will need to think about it.
    def __init__(self, species, species_type, attack, defense, spec_attack, spec_defense, ability, move_type, level):
        self.species = species #str
        self.species_type = species_type #lst
        self.attack = attack
        self.defense = defense
        self.spec_attack = spec_attack
        self.spec_defense = spec_defense
        self.ability = ability
        self.move_type = move_type #move type it is using
        self.level = level

    def print_species(self):
        print(self.species)

charizard = UserPokemon('Charizard', ['fire', 'flying'], 15, 15, 15, 14, 'wut', 'fire', 36)

charizard.print_species()