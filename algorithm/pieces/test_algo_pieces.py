import pytest
from algo_pieces import *

def test_2_targets():
    targets = 2
    expected = 0.75
    actual = target_num(targets)
    assert expected == actual

def test_1_target():
    targets = 1
    expected = 1
    actual = target_num(targets)
    assert expected == actual

@pytest.fixture
def user_pokemon_one():
    u_poke = UserPokemon()
    u_poke.species = 'bulbasaur'
    u_poke.species_type = ['', '']
    u_poke.attack = 1
    u_poke.defense = 1
    u_poke.spec_attack = 1
    u_poke.spec_defense = 1
    u_poke.ability = 'no'
    u_poke.move_type = 'grass'
    u_poke.level = 5


    

    pass