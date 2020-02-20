
import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def loadImages(cardImages):
    suits = ['heart', 'club', 'diamond', 'spade']
    facecards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'


    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number of cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            cardImages.append((card, image,))

        # next the face cards
        for card in facecards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            cardImages.append((10, image,))


def dealCard(frame):
    # Pop the next card off the top of the deck use .pop(0) to do so
    nextCard = deck.pop(0)
    # Add the card back to the end of the deck
    deck.append(nextCard)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=nextCard[1], relief='raised').pack(side='left')
    # now return the card's face value
    return nextCard


def scoreHand(hand):
    # Calculate the total score of all cards in the list.
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for nextCard in hand:
        cardValue = nextCard[0]
        if cardValue == 1 and not ace:
            ace = True
            cardValue = 11
        score += cardValue
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def dealDealer():

    dealerScore = scoreHand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(dealCard(dealerCardFrame))
        dealerScore = scoreHand(dealerHand)
        dealerScoreLabel.set(dealerScore)

    playerScore = scoreHand(playerHand)
    if playerScore > 21:

        checkwin(1)

    elif dealerScore > 21 or dealerScore < playerScore:

        checkwin(2)

    elif dealerScore > playerScore:

        checkwin(1)

    else:
        checkwin(3)


def dealPlayer():

    playerHand.append(dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)

    playerScoreLabel.set(playerScore)
    if playerScore > 21:
        # resultText.set('Dealer Wins!')
        checkwin(1)

    # global playerScore
    # global playerAce
    #
    # cardValue = dealCard(playerCardFrame)[0]
    # if cardValue == 1 and not playerAce:
    #     playerAce = True
    #     cardValue = 11
    # playerScore += cardValue
    # # If we would bust, check if there is an ace and subtract
    # if playerScore > 21 and playerAce:
    #     playerAce = False
    #     playerScore -= 10
    # playerScoreLabel.set(playerScore)
    # if playerScore > 21:
    #     resultText.set("Dealer Wins!")
    #
    # print(locals())


def newGame():

    global deck
    global dealerCardFrame
    global playerCardFrame
    global playerHand
    global dealerHand
    dealerWins.config(fg='black')
    playerWins.config(fg='black')
    playerCardFrame.destroy()
    dealerCardFrame.destroy()

    playerCardFrame = tkinter.Frame(cardFrame, background='green')
    playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    dealerCardFrame = tkinter.Frame(cardFrame, background='green')
    dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

    resultText.set("")
    dealerHand = []
    playerHand = []
    dealPlayer()
    dealerHand.append(dealCard(dealerCardFrame))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()


def shuffleDeck():
    random.shuffle(deck)


def checkwin(score):

    global dealerTally
    global playerTally
    global dealerWins
    global playerWins
    if score is 1:
        resultText.set('Dealer Wins')
        dealerTally += 1
        dealerText.set(dealerTally)
        dealerWins.config(fg='red')
        dealerWins.update()
    elif score is 2:
        resultText.set('Player Wins')
        playerTally += 1
        playerText.set(playerTally)
        playerWins.config(fg='red')
        playerWins.update()
    else:
        resultText.set('Draw!')


playerTally = 0
dealerTally = 0

def play():

    dealPlayer()
    dealerHand.append(dealCard(dealerCardFrame))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()


    mainWindow.mainloop()


mainWindow = tkinter.Tk()
# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

resultText = tkinter.IntVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background='green', fg='white').grid(row=1, column=0)

# embedded frame to hold the card images
dealerCardFrame = tkinter.Frame(cardFrame, background='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tkinter.IntVar()

tkinter.Label(cardFrame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background='green', fg='white').grid(row=3, column=0)

# embedded frame to hold the card images

playerCardFrame = tkinter.Frame(cardFrame, background='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tkinter.Button(buttonFrame, text='Dealer', command=dealDealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text='Player', command=dealPlayer)
playerButton.grid(row=0, column=1)

resetGame = tkinter.Button(buttonFrame, text='New Game', command=newGame)
resetGame.grid(row=0, column=2)

shuffle = tkinter.Button(buttonFrame, text='Shuffle', command=shuffleDeck)
shuffle.grid(row=0, column=3)

dealerText = tkinter.IntVar()
dealerWins = tkinter.Label(buttonFrame, textvariable=dealerText)
dealerWins.grid(row=1, column=0, columnspan=1)

playerText = tkinter.IntVar()
playerWins = tkinter.Label(buttonFrame, textvariable=playerText)
playerWins.grid(row=1, column=1, columnspan=1)

# load cards
cards = []
loadImages(cards)

# Create the list ot store the dealer's and player's hands
dealerHand = []
playerHand = []

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# newGame()



if __name__ == "__main__":
    play()