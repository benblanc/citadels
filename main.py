import random

from pprint import pprint

import card, game


# def draw_card(deck):
#     random_card_index = 0
#     cards_in_deck = len(deck)
#
#     if cards_in_deck > 1:
#         random_card_index = random.randint(1, cards_in_deck - 1)
#
#     drawn_card = deck.pop(random_card_index)
#
#     return deck, drawn_card


if __name__ == '__main__':
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

    for player in game_object.players:
        pprint(player.info)
        # for card in player.cards:
        # pprint(card.info)
        print("------------------------------------------------------------------")

    # start of round

    game_object.temp()

    # start of player turn

    # player_object = player.ClassPlayer(name="John Doe",
    #                                    coins=0,
    #                                    character=[],
    #                                    cards=[],
    #                                    buildings=[],
    #                                    flag_king=False,
    #                                    flag_assassinated=False,
    #                                    flag_stolen=False,
    #                                    flag_protected=False)

    # cards_object = card.ClassCard()
    #
    # deck_characters = cards_object.get_characters()
    #
    # deck_districts = cards_object.get_districts()
    #
    # random.shuffle(deck_characters)  # shuffle character cards
    # random.shuffle(deck_districts)  # shuffle district cards
    #
    # starter_coins = 2
    # starting_hand_amount = 4
    #
    # starting_hand = []
    #
    # print(len(deck_districts))
    #
    # for index in range(0, starting_hand_amount):
    #     deck_districts, drawn_card = draw_card(deck_districts)
    #     starting_hand.append(drawn_card)
    #
    # print(len(starting_hand))
    # print(len(deck_districts))
    #
    # pprint(list(map(lambda x: x.info, starting_hand)))
