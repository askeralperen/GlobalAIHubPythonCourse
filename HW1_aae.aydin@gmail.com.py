# user: Alperen Aydın
# mail: aae.aydin@gmail.com

# HW1 : generate a 3x3 matrix of 9 random prime numbers using for loop.
# mmax is the upper value of the random values for the matrix which can be input or predefined. 

import random

mmax = int(input("Enter the upper limit for random numbers: "))
#mmax = 20

matrix = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
primes = []

kaçkereçabaladım = 0 #genel random sorgu sayacı

if mmax > 1: #asal alt limiti

  while len(primes) != 9: #3x3 matris doluluk kontrolü

      x = random.randint(2,mmax)
      #x = 2
      #print("x is",x)
      #print("-")

      for i in range(2,x): #asallık sorgusu
        if (x % i) == 0:
          #print("even")
          #print("--")
          break
        
        #else:
          #print("odd")
          #print("--")
      if x - i ==1 or x == 2:
        primes.append(x)
        #print(x, "prime")
      kaçkereçabaladım += 1
  print(" \n primes = ",primes) #elde edilen asalların listesi

  counter = 0 # matris kolon sütun doldurmak için sayaç

  for j in range(3): 
    for k in range(3):
      matrix[j][k] = primes[counter]
      counter += 1
  print(" \n resulting matrix is \n" ,matrix[0],"\n", matrix[1],"\n",matrix[2])
  print(" \n bu iş için",kaçkereçabaladım, "kere çabaladım")

else:
  print("invalid range input")
