import pytest
from algorithm import UserPokemon, EnemyPokemon, Modifier, damage, get_type_damage

def test_exists():
    assert UserPokemon
    assert EnemyPokemon
    assert Modifier
    assert damage
    assert get_type_damage

def test_test_single_type_not_effectiveness():
    assert get_type_damage('normal', ['ghost']) == 0

def test_single_type_regular_effective():
    assert get_type_damage('normal', ['normal']) == 1


@pytest.fixture
def user_marshtomp(UserPokemon):
    marshtomp = UserPokemon()
    return marshtomp

@pytest.fixture
def enemy_charizard(UserPokemon):
    pass


# should test for is A > B, approx damage. Tests for things that are type effective, type ineffective, spec vs physical, pokemon with same level, pokemon with level disparity, 