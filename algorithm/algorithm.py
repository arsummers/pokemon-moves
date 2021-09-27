class MoveUsed:
    """
    the move your pokemon will use. Fields: name, power, type, phys_or_spec
    """
    def __init__(self, name, power, type, phys_or_spec):
        self.name = name
        self.power = power
        self.type = type
        self.phys_or_spec = phys_or_spec

    def print_move(self):
        print(self.name, self.power, self.type, self.phys_or_spec)

class UserPokemon:
    """
    User's pokemon. All stats should be visible. Fields: species, species_type, attack, defense, spec_attack, spec_defense, ability, move_type, level
    """
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
        print(self.species, self.species_type, 'Attack:', {self.attack})

class EnemyPokemon:
    """
    Enemy pokemon. Necessary but hidden fields have been approximated. Fields: species, enemy_type, level
    """
    def __init__(self, species, enemy_type, level):
        self.species = species
        self.enemy_type = enemy_type
        self.level = level
        self.defense = self.level * 1.5

    def print_species(self):
        print(self.species, self.enemy_type, self.defense)



class Modifier:


    def target_num(targets=1):
        """
        The number of targets. Defaults to 1. 
        """
        if targets > 1:
            target_mod = 0.75
        else:
            target_mod = 1

        return target_mod


    def weather_modifier( move_type, weather='other'):
        """
        weather modifier. Defaults to no special weather. Fields: move_type, weather='other'
        """
        if weather == 'rain' and move_type == 'water' or weather == 'harsh sunlight' and move_type == 'fire':
            weather_mod = 1.5
        elif weather == 'rain' and move_type == 'fire' or weather == 'harsh sunlight' and move_type == 'water':
            weather_mod = 0.5
        else:
            weather_mod = 1
        return weather_mod


    def stab_mod(move_type, user_type, ability):
        """
        calculates same type move effectiveness. Fields: move_type, user_type, ability
        """
        if move_type in user_type and ability == 'adaptability':
            stab = 2.0
        elif move_type in user_type:
            stab = 1.5
        else:
            stab = 1
        return stab

    
    # type stuff goes here - should make it a dictionary. Will match type of move against type(s) of enemy pokemon. Defaults to 1 for regular effective. resistant -->, weak against --> .5, or .25 if doubled, strong against --> 2, or 4 if double

    # using a more repetive set up for this dictionary, to keep time complexity down.

    # I need to think about how I'm going to access this to match everything up. To access the right type effectiveness multiplier: match the move type with the first key. Check each type for the enemy pokemon via the nested dict key, then store them in 2 variables. Second variable will default to 1. The multiple of those variables will the be type bonus multiplier.
    type_matchup_chart = {
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

    # phys_or_spec denotes the type of move used
    def is_burned(burned, ability, phys_or_spec):
        """
        is your pokemon burned? fields: burned, ability, phys_or_spec. Burned is a boolean
        """
        if burned == True and ability != 'guts' and phys_or_spec == 'physical':
            burn_mod = 0.5
        else:
            burn_mod = 1
        return burn_mod



  # main damage algorithm  

def get_type_damage(move_type, enemy_type):
    """
    type damage calculator.
    """
    type_damage = 1


    type_chart = Modifier.type_matchup_chart
    move_type_access = type_chart[move_type]

    for i in enemy_type:
        if i not in move_type_access.keys():
            type_damage *= 1
        else:
            move_type_effectiveness = move_type_access[i]
            type_damage *= move_type_effectiveness

    print(type_damage)
    return type_damage

# power is the number power of the moved used
def damage(level, move_power, attack, defense, weather, stab, type, targets=1, burn=1):

    level_mod = ((2 * level) / 5) + 2
    
    attack_def_mod = attack / defense

    other_modifier = targets * weather * stab * type * burn

    dmg = (((level_mod * move_power * attack_def_mod) / 50) + 2) * other_modifier

    return int(dmg)


if __name__ == "__main__":

    mud_shot = MoveUsed('Mud shot', 55, 'ground', 'special')

    mud_shot.print_move()


    marshtomp = UserPokemon('Marshtomp', ['water', 'ground'], 52, 54, 52, 51, 'torrent', 'water', 29)

    linoone = EnemyPokemon('Linoone', ['normal'], 21)

    marshtomp.print_species()
    linoone.print_species()

    weather = Modifier.weather_modifier(mud_shot.type, 'rain', )
    print(f'The weather modifier: {weather}')

    stabby = Modifier.stab_mod(mud_shot.type, marshtomp.species_type, marshtomp.ability)
    print(f'The STAB modifier is: {stabby}')


    approx_dmg = damage(marshtomp.level, mud_shot.power, marshtomp.attack, linoone.defense, Modifier.weather_modifier('rain', mud_shot.type), Modifier.stab_mod(mud_shot.type, marshtomp.species_type, marshtomp.ability), get_type_damage(mud_shot.type, linoone.enemy_type))
    
    print(f'Approximate damage: {approx_dmg}')
