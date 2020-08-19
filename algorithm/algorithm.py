def modifier():
    pass

def damage(level, power, attack, defense):

    level_mod = ((2 * level) / 5) + 2
    
    attack_def_mod = attack / defense

    dmg = (((level_mod * power * attack_def_mod) / 50) + 2) * modifier