# user: Alperen Aydın
# mail: aae.aydin@gmail.com

# HW4

# çiçek isimleri ile adam asmaca oyunu
import random

wordsL = ["nilüfer", "zambak", "gül", "lale", "papatya"]

hak = 3

class Game(object):
  def __init__(self):
    self.word = wordsL[random.randrange(0,len(wordsL))]
    self.true_guesses = []
    self.wrong_guess_num = 0
    print(self.word)
  
  def play(self):

    while self.wrong_guess_num < hak:
      correct = True
      for L in self.word:
        if not L in self.true_guesses:
          correct = False
          break
      if correct:
        print("kazandınız!")
        break          

      guess = input("Harf tahmin edin pls: ")

      if guess in self.word:
        
        if not guess in self.true_guesses:
          print("tebrikler, doğru tahmin! ")
          self.true_guesses.append(guess)
        else:
          print("tekrarlanmış tahmin!! ")          
      else:
        print("yanlış tahmin!")
        self.wrong_guess_num += 1

hanggame = Game()
hanggame.play()
