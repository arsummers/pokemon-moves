class UserPokemon(type, attack, defense, spec_attack, spec_defense, ability):
    pass

def modifier(targets, weather, random, stab, move_type, phys_or_spec, burned, other):
     if targets > 1:
         target_mod = 0.75
    else:
        target_mod = 1

    if weather == 'rain' and move_type == 'water' or weather == 'harsh sunlight' and move_type == 'fire':
        weather_mod = 1.5
    elif weather == 'rain' and move_type == 'fire' or weather == 'harsh sunlight' and move_type == 'water':
        weather_mod = 0.5
    else:
        weather_mod = 1

    # this syntax is wrong
    if move_type in UserPokemon_type and UserPokemon_ability == 'adaptability':
        stab = 2.0
    if move_type in UserPokemon_type:
        stab = 1.5
    else:
        stab = 1

    
    # type stuff goes here - should make it a dictionary. Will match type of move against type(s) of enemy pokemon. Defaults to 1 for regular effective. resistant -->, weak against --> .5, or .25 if doubled, strong against --> 2, or 4 if double
    type_chart = [
        resistant_to = {'normal': 'ghost',},
        weak_against = {'normal': ['rock', 'steel'],},
        strong_against = {'normal': '',},
    ]
    




    if burned == True and ability != 'guts' and phys_or_spec == 'physical':
        burn_mod = 0.5
    else:
        burn_mod = 1



    

def damage(level, power, attack, defense):

    level_mod = ((2 * level) / 5) + 2
    
    attack_def_mod = attack / defense

    dmg = (((level_mod * power * attack_def_mod) / 50) + 2) * modifier

    return f'overall approximate damage: {dmg}'