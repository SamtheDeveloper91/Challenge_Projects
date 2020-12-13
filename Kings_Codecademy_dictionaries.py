import random
#kings
#define the rules, suits, and cards
start_dict = {0:"waterfall", 1:"you", 2:"me", 3:"floor", 4:"guys", 5:"chicks", 6:"heaven", 7:"date", 8:"bust a rhyme", 9:"categories", 10:"nvr hv i evr", 11:"questions", 12:"make a rule"}
suits = ['hearts', 'spades', 'clubs', 'diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

#transform the rules dictionary into a list
rules = [start_dict[i] for i in start_dict]*len(suits)

#create the deck of cards
deck = []
for suit in suits:
    for card in cards:
        deck.append(card + ' of ' + suit)

#create a dictionary that uses the cards as keys. the values are the card, and its corresponding rule
events = {i: (i, j) for i, j in zip (deck, rules)}

#define the nth turn of the game
chosen_cards = []
def kings(turn):
  try:
    if turn < 52:  
        for i in range(turn):
          chosen_cards.append(events.pop(random.choice(list(events.keys()))))
        print(chosen_cards[-1])
    elif turn == 52:
        for i in range(turn):
          chosen_cards.append(events.pop(random.choice(list(events.keys()))))
        print(chosen_cards[-1])
        print("game over")
    print(len(events))
  except IndexError:
    print("game over")
    
kings(1)
kings(1)
print(chosen_cards)
