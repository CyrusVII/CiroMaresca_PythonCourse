#if base
if(10>0):
  print("its trueeeeeee")
#if else
if(10>0):
  print("its trueeeeeee")
else:
  print("its falseeeeeeee")
#elif
n=101
if(n>10):
  print("its trueeeeeee")
  if(n>100):
    print("e magiore di 100")
elif (n<0):
  print("negative")
else:
  print("e tra 0 e 10")
  
#switch
comando = 1
match comando:
  case 1:
    print("Nipola")
  case 2:
    print("Mattia")
  case _:
    print("default")
