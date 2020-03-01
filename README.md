# Citadels
A python application which simulates the game called "Citadels".

:::info
At the moment, this game can only be played by one player controlling all players.
:::

:::warning
This game is still in development.
:::

## How to run this game
This game runs on python 3.7, which you can install by following this [tutorial](https://medium.com/@itylergarrett.tag/how-to-install-python-3-7-on-windows-10-pc-the-non-developer-version-b063e1913b39).

Navigate in cmd to the folder where you downloaded this game:
``` bash
cd path/to/citadels
```

Run the script:
``` bash
python main.py
```

## Rules

### Goal
To win this game you have to build 8 districts in your city.

### Preparation
Each player gets 4 districts and 2 coins. The oldest player starts as the king, which makes him able to pick a character first during a round.

### Cards

#### Districts
The goal of this game is to build 8 districts in your city. The more they cost, the more they are worth at the end of the game.

Each district has a color, which gives a bonus effect depending on the character you picked for the round:
* Yellow => king earns extra gold
* Blue => Bishop earns extra gold
* Green => Merchant earns extra gold
* Red => Warlord earns extra gold
* Purple => No extra gold, but they have a special effect

#### Characters
There are 8 characters that represent a player turn with each one having a special effect:
1. Assassin
2. Thief
3. Magician
4. King
5. Bishop
6. Merchant
7. Architect
8. Warlord

##### Assassin
Chooses a character whom will be killed. The player with that character skips a turn.

##### Thief
Chooses a character whom will be robbed this round. The assassin or the assassin's victim cannot be robbed. The player with the robbed character gives all money to the player with the thief character at the beginning of the turn. The robbed character keeps the money received during the income phase.

##### Magician
May either:
* trade all district cards in hand with another player (even at 0 cards), or
* discard a few district cards to the discard pile and draw the same amount from the deck with district cards

##### King
Gets the king status, making him able to pick a character first during a round. Gets a coin for each yellow district built. If killed by the assassin this round, the current king keeps his status.

##### Bishop
Built districts are protected from the warlord. Gets a coin for each blue district built.

##### Merchant
Gets a coin. Gets a coin for each green district built.

##### Architect
Draws 2 cards from the deck with district cards. May build up to 3 building this turn. Can have more than 8 buildings.

##### Warlord
Destroys another player's built district by paying one coin less than that player did; may only do this once during the turn. May not destroy a district in a city with 8 or more districts. Gets a coin for each red district built. 

### Round

#### Picking a character
...

#### Player turn
...

### End of the game
The game ends at the end of the round where a player has 8 or more built districts.

Each player counts his score:
* point for the value of the buildings within the city
* extra points from purple district effects
* 3 extra points if the player has districts of all 5 colors within the city
* 4 points for the player who was the first one to have 8 or more districts
* 2 points for each player having 8 or more districts after the first player to acheive that

The player with the most points wins. If there is a draw, the player whose districts, including lila district effects, have the biggest combined value wins.