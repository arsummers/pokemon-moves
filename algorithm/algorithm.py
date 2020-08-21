def modifier(targets, weather, badge, critical, random, stab, move_type, burn, other):
     if targets > 1:
         target_mod = 0.75
    else:
        target_mod = 1

    if weather == 'rain' and move_type == 'water' or weather == 'harsh sunlight' and move_type == 'fire':
        weather_mod = 1.5

    

def damage(level, power, attack, defense):

    level_mod = ((2 * level) / 5) + 2
    
    attack_def_mod = attack / defense

    dmg = (((level_mod * power * attack_def_mod) / 50) + 2) * modifier

    return f'overall approximate damage: {dmg}'