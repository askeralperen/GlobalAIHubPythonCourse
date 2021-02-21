# user: Alperen Aydın
# mail: aae.aydin@gmail.com

# HW Final

class Recipe():                    # parent class
  def __init__(self,products):
    self.products = products       # products and their usage times are entered manually.

  def cook(self):                  
    #time = self.calc_time()
    for product in self.products:     
      print(product[0],"kullanılıyor")        #cooking sequence printing
      for i in range(product[1]):
        print(i+1,"dk geçti")
    time = self.calc_time()
    print("yemeğiniz ",time, "dakikada hazırlandı.. Afiyet olsun: ")      # overall report
    
  def calc_time(self):              # cooking time calculator
    time = 0
    for product in self.products:
      time += product[1]
    return time

class Recipe1(Recipe):                #child classes
  def __init__(self,products):
    super().__init__(products)

class Recipe2(Recipe):
  def __init__(self,products):
    super().__init__(products)

class Recipe3(Recipe):
  def __init__(self,products):
    super().__init__(products)


Products =[["Yumurta",3],["Süt",1],["Tereyağı",1],["Tuz",1],["Un",12]]

recipe1 = Recipe1(Products)    #  parent >>> recipe1 = Recipe(Products)

recipe1.cook()

recipe2 = Recipe2(Products[2:])    #  parent >>> recipe1 = Recipe(Products)

recipe2.cook()

recipe3 = Recipe3(Products[:3])    #  parent >>> recipe1 = Recipe(Products)

recipe3.cook()
