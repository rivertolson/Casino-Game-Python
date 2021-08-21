import random

# The Deck of cards
deck = [['Ace of Hearts', 1, 11], ['Two of Hearts', 2], ['Three of Hearts', 3],
        ['Four of Hearts', 4], ['Five of Hearts', 5], ['Six of Hearts', 6],
        ['Seven of Hearts', 7], ['Eight of Hearts', 8], ['Nine of Hearts', 9],
        ['Ten of Hearts', 10], ['Jack of Hearts', 10], ['Queen of Hearts', 10],
        ['King of Hearts', 10], ['Ace of Spades', 1, 11], ['Two of Spades', 2],
        ['Three of Spades', 3],['Four of Spades', 4], ['Five of Spades', 5],
        ['Six of Spades', 6], ['Seven of Spades', 7], ['Eight of Spades', 8],
        ['Nine of Spades', 9], ['Ten of Spades', 10], ['Jack of Spades', 10],
        ['Queen of Spades', 10], ['King of Spades', 10], ['Ace of Diamonds', 1, 11],
        ['Two of Diamonds', 2], ['Three of Diamonds', 3], ['Four of Diamonds', 4],
        ['Five of Diamonds', 5], ['Six of Diamonds', 6], ['Seven of Diamonds', 7],
        ['Eight of Diamonds', 8], ['Nine of Diamonds', 9], ['Ten of Diamonds', 10],
        ['Jack of Diamonds', 10], ['Queen of Diamonds', 10], ['King of Diamonds', 10],
        ['Ace of Clubs', 1, 11], ['Two of Clubs', 2], ['Three of Clubs', 3],
        ['Four of Clubs', 4], ['Five of Clubs', 5], ['Six of Clubs', 6],
        ['Seven of Clubs', 7], ['Eight of Clubs', 8], ['Nine of Clubs', 9],
        ['Ten of Clubs', 10], ['Jack of Clubs', 10], ['Queen of Clubs', 10],
        ['King of Clubs', 11]]

# This is like pulling one random card from a shuffled deck.
def draw():
    i = random.randint(0,len(deck)-1)
    card = deck[i][0]
    value = deck[i][1]
    deck.pop(i)
    return (card, value)

# Simulates drawing two cards
card1 = draw()
card2 = draw()

# adding the totalls together
value = card1[1] + card2[1]

# Showing results
print('%s\n%s' % (card1[0],card2[0]))
print('Score: %s' % value)
