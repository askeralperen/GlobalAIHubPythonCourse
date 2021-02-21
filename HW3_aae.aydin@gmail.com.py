# user: Alperen Aydın
# mail: aae.aydin@gmail.com

# HW3

nums = list(range(1000))

def prime_first(x):
    if x < 500:
      if x == 2:
        print(x)
      if x > 2:  
        for i in range(2,x): #asallık sorgusu
          if (x % i) == 0:
            #print("even")
            #print("--")
            break
        
          #else:
            #print("odd")
            #print("--")
        if x - i ==1 or x == 2:
          print(x)

def prime_second(x):
    if x > 500:
      for i in range(2,x): #asallık sorgusu
        if (x % i) == 0:
          #print("even")
          #print("--")
          break
      
        #else:
          #print("odd")
          #print("--")
      if x - i ==1 or x == 2:
        print(x)

print("1st Func.: ")
for i in nums:

  prime_first(i)

print("2nd Func.: ")
for i in nums:
  prime_second(i)
  
