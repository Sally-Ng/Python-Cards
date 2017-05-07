# I acknowledge the assistance of Marc Mares and Ethan Dixon
from random import shuffle

# Make a Card calss
class Card:
  
  # set the instance's attributes
  def __init__(self, value = "" , suit = ""):
    self.value = value
    self.suit = suit
  
  # return the numerical value of a card
  def int_value(self):
    if self.value == "A":
      self.value = 1
    elif self.value =="T":
      self.value = 10
    elif self.value =="J":
      self.value = 11
    elif self.value =="Q":
      self.value = 12
    elif self.value == "K":
      self.value = 13
    else:
      self.value = int(self.value)
    return self.value
    
  # return a two character string (the value and the suit)
  def __str__(self):
    return str(self.int_value()) + self.suit
  
# Make a Deck class  
class Deck:
  
  # initialize the cards attribute to a shuffled list of Card objects
  def __init__(self):
    self.cards = []
    value = ("A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K")
    suit = ("H", "D", "S", "C")
    for i in value:
      for j in suit:
        card = Card(i,j)
        self.cards.append(card)
    shuffle(self.cards)
    
  # remove and return the zeroth Card object from the cards attribute    
  def deal_card(self):
    dealt_card = self.cards[0]
    self.cards.remove(dealt_card)
    return dealt_card 
