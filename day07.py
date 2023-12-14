# Advent of Code 2023 day 7
# 12/12/2023
# Author: Max Mayer

# !! THIS IS SET UP FOR PART 2. FOR PART 1, SOME THINGS MUST BE COMMENTED OUT (see comments) !!

# class to hold the poker hand
class PokerHand:

    def __init__(self, hand, bet):
        # set the bet
        self.bet = bet

        # convert the hand to a list
        hand = list(hand)

        # replace the face cards with their corresponding numbers
        for i in range(len(hand)):
            if hand[i] == 'A':
                hand[i] = 14
            elif hand[i] == 'K':
                hand[i] = 13
            elif hand[i] == 'Q':
                hand[i] = 12
            elif hand[i] == 'J':
                hand[i] = 0 # FOR PART 1 IT IS 11, NOT 0
            elif hand[i] == 'T':
                hand[i] = 10
            else:
                hand[i] = int(hand[i])
        self.hand = hand

        # set the high card (we dont even need this)
        self.high_card = max(hand)

        # then, set the hand type
        # the higher the type, the more powerful
        # five of a kind = 6
        # four of a kind = 5
        # full house = 4
        # three of a kind = 3
        # two pair = 2
        # one pair = 1
        # high card = 0

        #  vvv FOR PART 2 ONLY vvv
        # since zeros are wildcards, we will replace the zero with the most common number
        index_of_cards_changed = []
        if 0 in hand:
            for i in range(len(hand)):
                if hand[i] == 0:
                    hand[i] = self.most_common()
                    index_of_cards_changed.append(i)
        # ^^^ FOR PART 2 ONLY ^^^

        # if we have 5 of a kind, only one type of card
        if len(set(hand)) == 1:
            self.hand_type = 6
        # else, we have two, we either have a full house or four of a kind
        elif len(set(hand)) == 2:
            # if a card appears 1 or 4 times, we know we have four of a kind
            if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
                self.hand_type = 5
            # otherwise, we have a full house
            else:
                self.hand_type = 4
        # else, we have three, we either have three of a kind, or two pair
        elif len(set(hand)) == 3:
            # if the first and second (or second and third or first and third) appear twice in the hand, we have two pair
            if hand.count(hand[0]) == 2 and hand.count(hand[1]) == 2 or hand.count(hand[1]) == 2 and hand.count(hand[2]) == 2 or hand.count(hand[0]) == 2 and hand.count(hand[2]) == 2:
                self.hand_type = 2
            # if a card appears 3 or 2 times, we know we have three of a kind
            elif hand.count(hand[0]) == 3 or hand.count(hand[0]) == 2 or hand.count(hand[0]) == 1:
                self.hand_type = 3
            # otherwise, we have two pair
            else:
                self.hand_type = 2
        # else, we have four, we one pair
        elif len(set(hand)) == 4:
            self.hand_type = 1
        # else, we have five, we have a high card
        else:
            self.hand_type = 0

        # vvv FOR PART 2 ONLY vvv
        # set card we changed back to zero
        for i in index_of_cards_changed:
            hand[i] = 0
        # ^^^ FOR PART 2 ONLY ^^^

    def __str__(self):
        switcher = {
            0: "High Card",
            1: "One Pair",
            2: "Two Pair",
            3: "Three of a Kind",
            4: "Full House",
            5: "Four of a Kind",
            6: "Five of a Kind"
        }
        hand_type = switcher.get(self.hand_type, "Invalid Hand Type")
        return str(self.hand) + ': ' + str(self.high_card) + ', ' + hand_type + ', ' + str(self.bet)

    def __lt__(self, other):
        # if self has a lower hand type, it is "less than" (loses to) other
        if self.hand_type < other.hand_type:
            return True
        # if the hand types are the same, compare high cards in order from left to right
        elif self.hand_type == other.hand_type:
            # make sure you dont compare if they are same value
            num1 = self.hand[0]
            num2 = other.hand[0]
            i = 1
            while num1 == num2:
                num1 = self.hand[i]
                num2 = other.hand[i]
                i += 1
            # if the first number is less than the second, self loses to other
            return num1 < num2


        # otherwise, self does not lose to other
        return False

    def __eq__(self, other):
        # two hands are equal if they have the same hand type and high card
        return self.hand_type == other.hand_type and self.high_card == other.high_card

    def get_bet(self):
        return self.bet

    def most_common(self):
        # ignore the 0s in the hand
        hand = self.hand
        hand = [x for x in hand if x != 0]
        # find the most common number
        most_common = max(set(hand), key=hand.count) if hand else 14
        return most_common


# read the card inputs
with open("day07.txt", "r") as file:
    cards = file.readlines()

# strip the new lines from the entry
cards = [card.strip() for card in cards]

# go through all the cards and make a hand for each
hands = []
for card in cards:
    values = card.split(' ')
    hand = PokerHand(values[0], int(values[1]))
    hands.append(hand)

# sort the hand
hands = sorted(hands)

# for hand in hands:
#     print(hand)

# get the scores (bet * index + 1)
scores = []
for i in range(len(hands)):
    scores.append(hands[i].get_bet() * (i + 1))

# print the sum of the scores
print("Part 2 answer: " + str(sum(scores)))
