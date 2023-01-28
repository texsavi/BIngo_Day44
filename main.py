import random,os,time

def ranNo():
  number=random.randint(1,90)
  return number

def order():
  for row in bingo:
    for item in row:
      print(item,end="\t|\t")
    print()

def createCard():
  global bingo
  bingoNum=[]
  for num in range(8):
    num=ranNo()
    while num in bingoNum:
     num=ranNo()
    bingoNum.append(ranNo())
    
  bingoNum.sort()
  bingo=[ [bingoNum[0],bingoNum[1],bingoNum[2]],
            [bingoNum[3],"GO",bingoNum[4]],
            [bingoNum[5],bingoNum[6],bingoNum[7]]
            ]
  
createCard()
print()
while True:
  order()
  nextNumber=int(input("Enter next number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == nextNumber:
        bingo[row][item]="X"

  xs=0
  for row in bingo:
    for item in row:
      if item=="X":
        xs+=1
  
  if xs==8:
    print("Bingo!!You won!!")
    break

  time.sleep(1)
  os.system("clear")