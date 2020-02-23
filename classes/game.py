import random

from classes import player


class ClassGame:
    def __init__(self):
        self.__settings = {
            "min_players": 2,
            "max_players": 7,
            "amount_starting_hand": 4,
            "amount_starting_coins": 2
        }

        self.__players = []
        self.__amount_players = 0

        # less than 4 players
        self.__characters_unused = 2
        self.__characters_per_player = 2

        self.__deck_characters = []
        self.__deck_districts = []
        self.__discard_pile = []

    @property
    def settings(self):
        return self.__settings

    @property
    def amount_players(self):
        return self.__amount_players

    @amount_players.setter
    def amount_players(self, value):
        if isinstance(value, int):
            if self.__settings["min_players"] <= value <= self.__settings["max_players"]:
                self.__amount_players = value

    @property
    def characters_unused(self):
        return self.__characters_unused

    @property
    def characters_per_player(self):
        return self.__characters_per_player

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    @property
    def deck_characters(self):
        return self.__deck_characters

    @deck_characters.setter
    def deck_characters(self, value):
        self.__deck_characters = value

    @property
    def deck_districts(self):
        return self.__deck_districts

    @deck_districts.setter
    def deck_districts(self, value):
        self.__deck_districts = value

    @property
    def discard_pile(self):
        return self.__discard_pile

    @discard_pile.setter
    def discard_pile(self, value):
        self.__discard_pile = value

    def create_players(self):
        for index in range(self.__amount_players):
            self.__players.append(player.ClassPlayer(index=index, name="Player %s" % (index + 1)))

        # randomly choose a king
        index_king = random.randint(0, self.__amount_players - 1)
        self.__players[index_king].flag_king = True

    def set_unused_cards_per_player(self):
        if self.__amount_players == 4:
            self.__characters_unused = 2
            self.__characters_per_player = 1

        elif self.__amount_players == 5:
            self.__characters_unused = 1
            self.__characters_per_player = 1

        elif self.__amount_players == 6:
            self.__characters_unused = 0
            self.__characters_per_player = 1

        elif self.__amount_players == 7:
            self.__characters_unused = 0
            self.__characters_per_player = 1

    def __draw_card(self, deck, card_index=None):  # draw card from deck
        if isinstance(card_index, int):
            cards_in_deck = len(deck)

            if cards_in_deck > 1:
                drawn_card = deck.pop(card_index)

            else:  # last car in deck
                drawn_card = deck.pop(0)

            return deck, drawn_card

        else:
            random_card_index = 0
            cards_in_deck = len(deck)

            if cards_in_deck > 1:
                random_card_index = random.randint(1, cards_in_deck - 1)

            drawn_card = deck.pop(random_card_index)

            return deck, drawn_card

    def draw_card_deck_characters(self, index):
        self.__deck_characters, drawn_card = self.__draw_card(self.__deck_characters, index)
        return drawn_card

    def draw_card_deck_districts(self):
        self.__deck_districts, drawn_card = self.__draw_card(self.__deck_districts)
        return drawn_card

    def set_starting_coins_per_player(self):
        for player in self.__players:
            player.coins = self.__settings['amount_starting_coins']

    def set_starting_hand_per_player(self):  # give each player a card for the amount of players there are
        for index in range(self.__amount_players):
            for player in self.__players:
                drawn_card = self.draw_card_deck_districts()
                player.cards.append(drawn_card)

    def __remove_characters_for_round(self, characters):  # remove characters for this round
        characters_removed = []

        for index in range(self.__characters_unused):
            random.shuffle(characters)  # shuffle deck
            characters, drawn_card = self.__draw_card(characters)
            characters_removed.append(drawn_card)

        return characters_removed

    def __prepare_pickable_characters(self):
        # remove king from deck with characters
        characters = list(filter(lambda x: x.name != "King", self.__deck_characters))
        character_king = list(filter(lambda x: x.name == "King", self.__deck_characters))[0]

        # get removed characters for this round
        characters_removed = self.__remove_characters_for_round(characters)

        # add king back to pickable characters
        characters.append(character_king)

        return characters, characters_removed

    def __get_index_character(self, order_number):
        for index_character in range(len(self.__deck_characters)):  # go through each character
            if self.__deck_characters[index_character].order == order_number:  # find character with given order number
                return index_character  # return character index

    def set_character_per_player(self):
        from pprint import pprint

        # prepare character picking
        self.__deck_characters, characters_removed = self.__prepare_pickable_characters()

        print("Characters removed for this round:")
        for character in characters_removed:
            pprint(character.info)

        # check who is king at the moment
        current_king = list(filter(lambda x: x.flag_king == True, self.__players))[0]

        # establish choosing order
        choosing_order_normal = list(range(0, self.__amount_players))
        choosing_order = choosing_order_normal[current_king.index:] + choosing_order_normal[:current_king.index]

        # distribute character(s)
        for index in range(self.__characters_per_player):  # 2-3 players allows more characters per player
            for index_choosing_order in choosing_order:  # let each player pick (king starts)
                print("Hello player ", index_choosing_order + 1)
                print("Characters the players can choose from:")
                for character in self.__deck_characters:
                    pprint(character.info)

                order_number = int(input("Pick a character for this round by entering the order number: "))

                index_character = self.__get_index_character(order_number)

                drawn_card = self.draw_card_deck_characters(index_character)

                self.__players[index_choosing_order].character.append(drawn_card)

    def remove_character_per_player(self):
        for player in self.__players:
            player.character = []
