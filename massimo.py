i=0
n=input('valore iniziale:')
n= int(n)
max=n

while i<9:
   n=input('valori:')
   n= int(n)
   if n>max:
      max=n
   i+=1

print('il massimo è: ' + str(max))
  