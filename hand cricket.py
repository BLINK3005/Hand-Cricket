import random,time
pa=input("Enter Player 1 Name:")
pb=input("Enter Player 2 Name:")
sa=0
sb=0
print("")
print(pa,"Score:",pb,"Score:")
while True:
    a=random.randrange(0,7)
    b=random.randrange(0,7)
    sa+=a
    sb+=b
    time.sleep(0.3)
    print(" ",sa)
    time.sleep(0.3)
    print("            ",sb)
    if sa >=100:
        print(pa,"Won!")
        break
    if sb>=100:
        print(pb,"Won!")
        break

    
    
    
    





