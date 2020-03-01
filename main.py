import random, traceback

from pprint import pprint

from copy import deepcopy

from classes import card, game

if __name__ == '__main__':
    try:
        # preparation of game

        game_object = game.ClassGame()

        game_object.amount_players = 4

        cards_object = card.ClassCard()

        deck_characters = cards_object.get_characters()

        deck_districts = cards_object.get_districts()

        game_object.deck_characters = deepcopy(deck_characters)

        game_object.deck_districts = deepcopy(deck_districts)

        random.shuffle(game_object.deck_characters)  # shuffle character cards
        random.shuffle(game_object.deck_districts)  # shuffle district cards

        # start of game

        game_object.create_players()

        game_object.set_unused_cards_per_player()

        game_object.set_starting_coins_per_player()

        game_object.set_starting_hand_per_player()

        while not game_object.eight_districts_built:  # while win condition is not met

            print("\n\n")
            print("=========================================\n"
                  "================ ROUND %s ================\n"
                  "=========================================" % game_object.round)
            print("\n\n")

            # start of round

            game_object.set_character_per_player()

            # for player in game_object.players:
            #     pprint(player.info)
            #
            #     for character in player.character:
            #         pprint(character.info)
            #
            #     print("------------------------------------------------------------------")

            # for character in game_object.deck_characters:
            #     pprint(character.info)

            # start of player turn

            # for index in range(len(deck_characters)):
            #     for player in game_object.players:

            print("\n\n\n\n\n")

            for character in deck_characters:
                for player in game_object.players:
                    for player_character in player.character:
                        if player_character == character:
                            print("%s is the %s" % (player.name, player_character.name))
                            game_object.start_player_turn(player.index, character)

            print("END OF THE ROUND!")

            # end of round

            game_object.remove_character_per_player()

            game_object.deck_characters = deepcopy(deck_characters)  # reset deck characters

            game_object.removed_characters = []  # reset removed characters for this round

            game_object.possible_characters = []  # reset possible characters for this round

            game_object.round += 1  # increase round counter

    except Exception:
        pprint(traceback.format_exc())
