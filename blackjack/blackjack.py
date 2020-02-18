
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
        resultText.set("Dealer Wins!")
    elif dealerScore > 21 or dealerScore < playerScore:
        resultText.set('Player Wins!')
    elif dealerScore > playerScore:
        resultText.set("Dealer Wins!")
    else:
        resultText.set('Draw!')


def dealPlayer():

    playerHand.append(dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)

    playerScoreLabel.set(playerScore)
    if playerScore > 21:
        resultText.set('Dealer Wins!')
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


def resetGame():

    global deck
    global dealerCardFrame
    global playerCardFrame
    global playerHand
    global dealerHand
    playerCardFrame.destroy()
    dealerCardFrame.destroy()

    playerCardFrame = tkinter.Frame(cardFrame, background='green')
    playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    dealerCardFrame = tkinter.Frame(cardFrame, background='green')
    dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

    resultText.set("")

    dealPlayer()
    dealerHand.append(dealCard(dealerCardFrame))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()


mainWindow = tkinter.Tk()
# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

resultText = tkinter.StringVar()
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

resetGame = tkinter.Button(buttonFrame, text='New Game', command=resetGame)
resetGame.grid(row=0, column=2)

# load cards
cards = []
loadImages(cards)
# print(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# Create the list ot store the dealer's and player's hands
dealerHand = []
playerHand = []

dealPlayer()
dealerHand.append(dealCard(dealerCardFrame))
dealerScoreLabel.set(scoreHand(dealerHand))
dealPlayer()


mainWindow.mainloop()