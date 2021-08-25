import pytest
from algorithm import UserPokemon, EnemyPokemon, MoveUsed, Modifier, damage, get_type_damage

def test_exists():
    assert UserPokemon
    assert EnemyPokemon
    assert Modifier
    assert damage
    assert get_type_damage

# tpe effectiveness tests

def test_test_single_type_not_effective():
    assert get_type_damage('normal', ['ghost']) == 0

def test_single_type_regular_effective():
    assert get_type_damage('normal', ['normal']) == 1

def test_single_type_not_very_effective():
    assert get_type_damage('fire', ['rock']) == 0.5

def test_single_type_super_effective():
    assert get_type_damage('rock', ['fire']) == 2

def test_dual_type_not_effective():
    assert get_type_damage('ground', ['fire', 'flying']) == 0

def test_dual_type_regular_effective_common():
    assert get_type_damage('ghost', ['fire', 'ground']) == 1

def test_dual_type_regular_effective_uncommon():
    assert get_type_damage('ghost', ['dark', 'psychic']) == 1

def test_dual_type_not_very_effective():
    assert get_type_damage('ghost', ['dark', 'grass']) == 0.5

def test_dual_type_extra_not_very_effective():
    assert get_type_damage('flying', ['rock', 'steel']) == 0.25

def test_dual_type_super_effective():
    assert get_type_damage('ground', ['electric', 'normal']) == 2

def test_dual_type_extra_super_effective():
    assert get_type_damage('grass', ['water', 'ground']) == 4

# same type attack bonus tests

def test_gets_basic_stab(mud_shot, user_marshtomp):

    assert Modifier.stab_mod(mud_shot.type, user_marshtomp.species_type, user_marshtomp.ability) == 1.5

def test_no_stab(ice_punch, user_marshtomp):
    assert Modifier.stab_mod(ice_punch.type, user_marshtomp.species_type, user_marshtomp.ability) == 1

def test_stab_with_adaptability(strength, user_eevee):
    assert Modifier.stab_mod(strength.type, user_eevee.species_type, user_eevee.ability) == 2

# weather tests
def test_weather_boost_water():
    pass

def test_weather_boost_fire():
    pass

def test_weather_negate_water():
    pass

def test_weather_negate_fire():
    pass

def test_weather_rain_no_move_buff():
    pass

def test_weather_sunlight_no_move_buff():
    pass

def test_weather_no_special_effect():
    pass

def test_full_damage(user_marshtomp, enemy_charizard):
    pass

@pytest.fixture
def user_marshtomp():
    marshtomp = UserPokemon('Marshtomp', ['water', 'ground'], 52, 54, 52, 51, 'torrent', 'water', 29)
    return marshtomp

@pytest.fixture
def user_eevee():
    eevee = UserPokemon('Eevee', ['normal'], 25, 26, 24, 23, 'adaptability', 'normal', 15)
    return eevee


@pytest.fixture
def enemy_charizard():
    charizard = EnemyPokemon('Charizard', ['fire', 'flying'], 36)
    return charizard

@pytest.fixture
def mud_shot():
    mud_shot = MoveUsed('Mud shot', 55, 'ground', 'physical')
    return mud_shot

@pytest.fixture
def ice_punch():
    ice_punch = MoveUsed('Ice punch', 75, 'ice', 'special')
    return ice_punch

@pytest.fixture
def strength():
    strength = MoveUsed('Strength', 80, 'normal', 'physical')
    return strength

@pytest.fixture
def surf():
    surf = MoveUsed('Surf', 90, 'water', 'special')
    return surf



# should test for is A > B, approx damage. Tests for things that are type effective, type ineffective, spec vs physical, pokemon with same level, pokemon with level disparity, 