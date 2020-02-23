import random, traceback

from pprint import pprint

from classes import card, game

if __name__ == '__main__':
    try:
        # preparation of game

        game_object = game.ClassGame()

        game_object.amount_players = 4

        cards_object = card.ClassCard()

        game_object.deck_characters = cards_object.get_characters()

        game_object.deck_districts = cards_object.get_districts()

        random.shuffle(game_object.deck_characters)  # shuffle character cards
        random.shuffle(game_object.deck_districts)  # shuffle district cards

        # start of game

        game_object.create_players()

        game_object.set_unused_cards_per_player()

        game_object.set_starting_coins_per_player()

        game_object.set_starting_hand_per_player()

        # start of round

        game_object.set_character_per_player()

        for player in game_object.players:
            pprint(player.info)

            for character in player.character:
                pprint(character.info)

            print("------------------------------------------------------------------")

        # start of player turn

        # end of round

        game_object.remove_character_per_player()

        game_object.deck_characters = cards_object.get_characters()  # reset deck characters

    except Exception:
        pprint(traceback.format_exc())
