# pokemon-moves
## App to help you decide which pokemon move to use in battles

# Problem Domain
- I often find myself deliberating over which pokemon attack to use in a given situation
  - weighing the differences between type effectiveness, vs type boosts, vs stats, vs raw power
  
# Goals
- User acct
- Ability to enter, save, and edit pokemon party's moves and stats\
- Ability to switch between calcuations for different generations
- if I can't get a reliable RESTful API for pokemon moves, at the bear minimum I will need:
  - moves model
    - type (water, grass, etc)
    - category (special/physical)
    - power
    - accuracy
    - name - for easier saving
    - types it's super effective against
    - type it's weak against
    - types it's normal effective against
  - pokemon model
    - name
    - type 1
    - type 2 (default Null)
    - moves (foreign key to moves?)
    - stats
        - attack
        - spec attack
        - defense
        - spec defense
        - speed
   - other modifiers - make these optional bc they can be a lot --> default all these to a X1 multiplier
      - terrain
      - weather
      
## Sources:
(Bulbapedia)[https://bulbapedia.bulbagarden.net/wiki/Damage]
(Type chart)[https://pokemondb.net/type]


Goal is to have a decent, deployable API that I can either feed into a flask templating front end, or deploy and feed to a react front end.

Testing goals:
- set up fixtures for a few different pokemon with various levels and typings
- test for a few different weather scenarios
- test for a a few different abilities

Testing brownout for https