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


class EnemyPokemon:
    def __init__(self, species, enemy_type, level):
        self.species = species
        self.enemy_type = enemy_type
        self.level = level


# unsure if I want to keep this as a simple function, or keep it as a class with smaller functions within
class Modifier:


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


    # this syntax is wrong
    def stab_mod(move_type, stab):
        if move_type in UserPokemon.type and UserPokemon.ability == 'adaptability':
            stab = 2.0
        if move_type in UserPokemon.type:
            stab = 1.5
        else:
            stab = 1
        return stab

    
    # type stuff goes here - should make it a dictionary. Will match type of move against type(s) of enemy pokemon. Defaults to 1 for regular effective. resistant -->, weak against --> .5, or .25 if doubled, strong against --> 2, or 4 if double

    # using a more repetive set up for this dictionary, to keep time complexity down.

    # I need to think about how I'm going to access this to match everything up. To access the right type effectiveness multiplier: match the move type with the first key. Check each type for the enemy pokemon via the nested dict key, then store them in 2 variables. Second variable will default to 1. The multiple of those variables will the be type bonus multiplier.
    type_chart = {
        'normal' : {'ghost': 0, 'rock' : 0.5, 'steel': 0.5,}, 
        'fire': {'rock': 0.5, 'steel': 0.5, 'grass': 2, 'ice': 2, 'bug': 2, 'steel': 2},
        'water' : {'fire': 2, 'water': 0.5, 'grass': 0.5, 'ground': 2, 'rock': 2, 'dragon': 0.5},
        'electric': {'water': 2, 'flying': 2, 'electric': 0.5, 'grass': 0.5, 'ground': 0, 'dragon': 0.5},
        'grass': {'fire': 0.5, 'water': 2, 'grass': 0.5, 'poison': 0.5, 'ground': 2, 'flying': 0.5, 'bug': 0.5, 'rock': 2, 'dragon': 0.5, 'steel': 0.5},
        'ice' : {'fire': 0.5, 'water': 0.5, 'grass': 2, 'ice': 0.5, 'ground': 2, 'flying': 2, 'dragon': 2, 'steel': 0.5},
        'fighting' : {'normal': 2, 'ice': 2, 'poison': 0.5, 'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'rock': 2, 'ghost': 0, 'dark': 2, 'steel': 2, 'fairy': 0.5},
        'poison': {'grass': 2, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'ghost': 0.5, 'steel': 0, 'fairy': 2},
        'ground': {'fire': 2, 'electric': 2, 'grass': 0.5, 'poison': 2, 'flying': 0, 'bug': 0.5, 'rock': 2, 'steel': 2},
        'flying': {'electric': 0.5, 'grass': 2, 'fighting': 2, 'bug': 2, 'rock': 0.5, 'steel': 0.5},
        'psychic': {'fighting': 2, 'posion': 2, 'psychic': 0.5, 'dark': 0, 'steel': 0.5},
        'bug': {'fire': 0.5, 'grass': 2, 'fighting': 0.5, 'poison': 0.5, 'flying': 0.5, 'psychic': 2, 'ghost': 0.5, 'dark': 2, 'steel': 0.5, 'fairy': 0.5},
        'rock': {'fire': 2, 'ice': 2, 'fighting': 0.5, 'ground': 0.5, 'flying': 2, 'bug': 2, 'steel': 0.5},
        'ghost': {'normal': 0, 'psychic': 2, 'ghost': 2, 'dark': 0.5},
        'dragon': {'dragon': 2, 'steel': 0.5, 'fairy': 0},
        'dark': {'fighting': 0.5, 'psychic': 2, 'ghost': 2, 'dark': 0.5, 'fairy': 0.5},
        'steel': {'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'ice': 2, 'rock': 2, 'steel': 0.5, 'fairy': 2},
        'fairy': {'fire': 0.5, 'fighting': 2, 'poison': 0.5, 'dragon': 2, 'dark': 2, 'steel': 0.5},
    }

    # this will need some ironing out too
    def calculate_type_effectiveness():
        type_effectiveness_multiplier = 1
        for type in type_chart:
            if UserPokemon.move_type == type:
                for key in type.values():
                    if EnemyPokemon.pokemon_type == key:
                        type_effectiveness_multiplier *= key[1]





    # phys_or_spec denotes the type of move used
    def is_burned():
        if burned == True and ability != 'guts' and phys_or_spec == 'physical':
            burn_mod = 0.5
        else:
            burn_mod = 1
        return burn_mod



    

    def damage(level, power, attack, defense):

        level_mod = ((2 * level) / 5) + 2
        
        attack_def_mod = attack / defense

        dmg = (((level_mod * power * attack_def_mod) / 50) + 2) * modifier

        return f'overall approximate damage: {dmg}'