from collections import defaultdict, Counter

from flask import Flask, render_template

import random

app = Flask(__name__)


@app.route("/")
def bonjour():
    return render_template("index.html")

@app.route("/regles")
def regles():
    return render_template("regles.html")

@app.route("/partie")
def partie():
    couleurs = ["♠", "♣", "♡", "♢"]
    valeurs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    class Carte:
        def __init__(self, valeur, couleur):
            self.valeur = valeur
            self.couleur = couleur
        def __str__(self):
            return f"{self.valeur}{self.couleur}"
        def show_card(self):
            print(valeurs + couleurs)

    def createDeckObj():
        deckObj = []
        for couleur in couleurs:
            for valeur in valeurs:
                Card = Carte(valeur,couleur)
                deckObj.append(Card)
        random.shuffle(deckObj)
        return deckObj

    deck = createDeckObj()

    def deal(n, deck):
        hand = []
        for i in range(n):
            hand.append(deck.pop())
        return hand

    player1 = deal(2, deck)
    player2 = deal(2, deck)

    def flop():
        cards_flop = []
        deal(1, deck)
        cards_flop.extend(deal(3, deck))
        deal(1, deck)
        cards_flop.extend(deal(1, deck))
        deal(1, deck)
        cards_flop.extend(deal(1, deck))
        return cards_flop

    cards_flop = flop()

    def showdown(player, cards):
        hand_player = []
        hand_player.extend(player)
        hand_player.extend(cards)
        return hand_player

    hand_player1 = showdown(player1, cards_flop)
    hand_player2 = showdown(player2, cards_flop)

    card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
                       "K": 13, "1": 14}

    def is_royal_flush(hand):
        if is_straight_flush(hand):
            values = [i.valeur for i in hand]
            # Check if the highest card is an Ace
            if set(values) == set(["10", "J", "Q", "K", "1"]):
                return True
        else:
            return False

    def is_straight_flush(hand):
        if is_flush(hand) and is_straight(hand):
            return True
        else:
            return False

    def is_four_of_a_kind(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 4 in value_counts.values():
            return True
        return False

    def is_full_house(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 3 in value_counts.values() and 2 in value_counts.values():
            return True
        return False

    def is_flush(hand):
        suits = [i.couleur for i in hand]
        # Initialisez un dictionnaire pour stocker le nombre d'occurrences de chaque couleur
        suit_counts = {}
        # Comptez le nombre d'occurrences de chaque couleur
        for suit in suits:
            suit_counts[suit] = suit_counts.get(suit, 0) + 1
        # Vérifiez s'il y a au moins cinq cartes de la même couleur
        if max(suit_counts.values()) >= 5:
            return True
        else:
            return False

    def is_straight(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        rank_values = [card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range == 4):
            return True
        else:
            # check straight with low Ace
            if set(values) == set(["1", "2", "3", "4", "5"]):
                return True
            return False

    def is_three_of_a_kind(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 3 in value_counts.values():
            return True
        else:
            return False

    def is_two_pairs(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if list(value_counts.values()).count(2) == 2:
            return True
        else:
            return False

    def is_one_pair(hand):
        values = [i.valeur for i in hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 2 in value_counts.values():
            return True
        else:
            return False

    def evaluate_hand(hand):
        if is_royal_flush(hand):
            return 10
        if is_straight_flush(hand):
            return 9
        if is_four_of_a_kind(hand):
            return 8
        if is_full_house(hand):
            return 7
        if is_flush(hand):
            return 6
        if is_straight(hand):
            return 5
        if is_three_of_a_kind(hand):
            return 4
        if is_two_pairs(hand):
            return 3
        if is_one_pair(hand):
            return 2
        return 1

    score_player1 = evaluate_hand(hand_player1)
    score_player2 = evaluate_hand(hand_player2)

    def is_winner(score_player1, score_player2):
        if score_player1 > score_player2:
            return "Vous avez gagné :)"
        elif score_player1 < score_player2:
            return "Vous avez perdu :("
        else:
            high_card_player1 = max((card_order_dict[i.valeur], i.valeur) for i in hand_player1)
            high_card_player2 = max((card_order_dict[i.valeur], i.valeur) for i in hand_player2)
            if high_card_player1 > high_card_player2:
                return "Vous avez gagné :)"
            elif high_card_player1 < high_card_player2:
                return "Vous avez perdu :("
            else:
                return "Égalité !"

    conclusion_partie = is_winner(score_player1,score_player2)

    card_name_dict = {"2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit",
                      "9": "neuf", "10": "dix", "J": "Valet", "Q": "Dame", "K": "Roi", "1": "As"}
    def combinaison_hand(hand):
        score = evaluate_hand(hand)
        if score == 10:
            return "une quinte flush royale"
        if score == 9:
            return "une quinte flush"
        if score == 8:
            return "un carré"
        if score == 7:
            return "un full"
        if score == 6:
            return "une couleur"
        if score == 5:
            return "une quinte"
        if score == 4:
            return "un brelan"
        if score == 3:
            return "une double paire"
        if score == 2:
            return f"une paire"
        else:
            high_card = max(hand, key=lambda card: card_order_dict[card.valeur])
            return f"une carte haute : {card_name_dict[high_card.valeur]} de {high_card.couleur}"

    combinaison_player1 = combinaison_hand(hand_player1)
    combinaison_player2 = combinaison_hand(hand_player2)

    all_cards = {"player1": player1, "player2": player2, "cards_flop": cards_flop,
                 "hand_player1": hand_player1, "hand_player2": hand_player2,
                 "combinaison_player1": f"Vous avez {combinaison_player1}",
                 "combinaison_player2": f"Votre adversaire a {combinaison_player2}",
                 "conclusion_partie": conclusion_partie}

    return render_template("partie.html", cards=all_cards)

if __name__ == '__main__':
    app.run(debug=True)
