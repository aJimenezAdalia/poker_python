

import yaml
from pathlib import Path
from utils.logger import Logger


filename = Path(__file__).stem
logger = Logger(filename).build_logger()


class Hands:
    def __init__(self) -> None:
        self.hands_values = self.hands().get('values')
        self.straights = self.hands().get('straights')
        self.pairs = self.hands().get('pairs')
        self.strengths = self.hands().get('strengths')

    @staticmethod
    def hands() -> dict:
        with open('../config/game_config.yaml', 'r') as stream:
            config_file = yaml.safe_load(stream)
        hands = config_file.get('hands')
        return hands

    def calculate_hand_value(self, common_cards: list, player_cards: list):
        """Calculate the best possible hand with seven given cards:
        Five common cards (flop, turn and river) and two player cards.
        Each common cards and player cards are expected in the following format:
        {name: card_name, strength: card_strength, code: card_type}.
        """
        full_cards = common_cards + player_cards
        cards_strengths = [card.get('strength') for card in full_cards]
        cards_codes = [card.get('code') for card in full_cards]

        # Building best possible hands, from top to bottom

        # 1. Flushes -> straight, regular flush
        exist_flush = self.exists_flush(seven_cards=full_cards)
        if exist_flush:
            return {'Hand': 'Flush', 'Value': self.hands_values.get('flush'),
                    'Strength': exist_flush.get('flush_force')}

        # 2. Poker - Four of a Kind
        exist_poker = self.exists_poker(seven_cards=full_cards)
        if exist_poker:
            return {'Hand': 'Poker', 'Value': self.hands_values.get('poker'), 'Strength': self.pairs.get(exist_poker)}

        # 3. Full-House
        # TODO: method to evaluate full-house hands

        # 4. Straights
        # TODO: method to evaluate straight hands

        # 5. Three of a Kind
        # TODO: method to evaluate three-of-a-kind hands

        # 6. Pairs - Double Pairs
        # TODO: method to evaluate pairs hands

        # 7. Top Card - High Card
        # TODO: method to evaluate high card hands
        #  if above methods doesn't return anything, top card/high card is the only remaining possible hand.

    def exists_flush(self, seven_cards: list):
        """Determines if exists Flush in the seven given cards.
        If exists, call the function 'evaluate_flush'."""
        # TODO: finish docstring
        spades = []
        clubs = []
        hearts = []
        diamonds = []

        for card in seven_cards:
            card_name = list(card.keys())[0]
            code = card[card_name].get('code')
            if code == 1:
                spades.append(card)
            elif code == 2:
                clubs.append(card)
            elif code == 3:
                hearts.append(card)
            else:
                diamonds.append(card)

        if len(spades) >= 5:
            flush_details = self.evaluate_flush(flush_cards=spades)
            return flush_details
        elif len(clubs) >= 5:
            flush_details = self.evaluate_flush(flush_cards=clubs)
            return flush_details
        elif len(hearts) >= 5:
            flush_details = self.evaluate_flush(flush_cards=hearts)
            return flush_details
        elif len(diamonds) >= 5:
            flush_details = self.evaluate_flush(flush_cards=diamonds)
            return flush_details

        return False

    def evaluate_flush(self, flush_cards: list) -> dict:
        """Evaluates a known flush hand, to determine flush nature [Regular, Straight]."""
        # TODO: finish docstring
        strengths = []
        for card in flush_cards:
            strength = card[list(card.keys())[0]]['strength']
            strengths.append(strength)

        sorted_strengths = sorted(strengths)
        if sorted_strengths in self.straights:
            flush_force = sorted_strengths[-1]
            flush_kind = 'Straight'
            return {'flush_kind': flush_kind, 'flush_force': flush_force}

        flush_force = sum(sorted_strengths)
        flush_kind = 'Regular'
        return {'flush_kind': flush_kind, 'flush_force': flush_force}

    def exists_poker(self, seven_cards: list) -> [dict, bool]:
        for card in seven_cards:
            card_name = list(card.keys())[0]
            card_strength = card[card_name].get('strength')
            equivalence = self.strengths.get(card_strength)
            self.pairs[equivalence] += 1

        any_poker = False
        poker_kind = ''

        for card_type, card_number in self.pairs.items():
            if len(card_number) == 4:
                any_poker = True
                poker_kind = card_type
                break

        if any_poker:
            return poker_kind
        return any_poker

    def exists_full_house(self, seven_cards: list) -> [dict, bool]:
        pass

    def exists_straight(self, seven_cards: list) -> [dict, bool]:
        pass

    def exists_three_of_a_kind(self, seven_cards: list) -> [dict, bool]:
        pass

    def exists_pairs(self, seven_cards: list) -> [dict, bool]:
        pass
