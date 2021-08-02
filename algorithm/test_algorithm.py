from .algorithm import UserPokemon, EnemyPokemon, Modifier, damage

def test_exists():
    assert UserPokemon
    assert EnemyPokemon
    assert Modifier

def test_one():
    pass



@pytest.fixture
def user_charizard(UserPokemon):
    pass

@pytest.fixture
def enemy_charizard(UserPokemon):
    pass


# should test for is A > B, approx damage. Tests for things that are type effective, type ineffective, spec vs physical, pokemon with same level, pokemon with level disparity, 