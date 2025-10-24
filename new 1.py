import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K"
}


def build_deck():
    return [(rank, suit) for rank in range(1, 14) for suit in SUITS]


def shuffle_cards(deck):
    random.shuffle(deck)


def draw_card(deck):
    if len(deck) < 2:
        deck[:] = build_deck()
        shuffle_cards(deck)
    return deck.pop()


def format_card(card):
    rank, suit = card
    rank_label = RANKS.get(rank, str(rank))
    return f"{rank_label}{suit}"


def card_value(card):
    return card[0]


playername = input("Enter your name: ").strip() or "Player"
compname = "Computer"
print(f"Hello {playername}, you are playing against {compname}. Good luck!")

comp_guess = random.randint(1, 13)
print(f"{compname} guesses the card value {comp_guess}.")

while True:
    try:
        player_guess = int(input("Guess a card value (1-13): "))
        if 1 <= player_guess <= 13:
            break
    except ValueError:
        pass
    print("Invalid guess, try again.")

deck = build_deck()
shuffle_cards(deck)

while True:
    player_card = draw_card(deck)
    comp_card = draw_card(deck)

    print(f"{playername} draws {format_card(player_card)}.")
    print(f"{compname} draws {format_card(comp_card)}.")

    if player_card == comp_card:
        print("Both drew the same card, reshuffling and drawing again...\n")
        deck.extend([player_card, comp_card])
        shuffle_cards(deck)
        continue
    break

player_diff = abs(card_value(player_card) - player_guess)
comp_diff = abs(card_value(comp_card) - comp_guess)

if player_diff < comp_diff:
    result = f"{playername} wins!"
elif comp_diff < player_diff:
    result = f"{compname} wins!"
else:
    result = "It's a tie!"

print(result)
