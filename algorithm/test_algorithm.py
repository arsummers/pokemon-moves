import pytest
from algorithm import UserPokemon, EnemyPokemon, Modifier, damage, get_type_damage

def test_exists():
    assert UserPokemon
    assert EnemyPokemon
    assert Modifier
    assert damage
    assert get_type_damage

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

@pytest.fixture
def user_marshtomp(UserPokemon):
    marshtomp = UserPokemon()
    return marshtomp

@pytest.fixture
def enemy_charizard(UserPokemon):
    pass


# should test for is A > B, approx damage. Tests for things that are type effective, type ineffective, spec vs physical, pokemon with same level, pokemon with level disparity, 