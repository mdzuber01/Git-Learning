#water_gun_snake game
import random
import string
lis=['gun','snake','water']
print(lis)
count=0
tie=0
try:
    a=int(input("How many times do you want to play this game : "))
except:
    print("!!..Invalid Input..!! Please enter an integer value ")
    
for i in range(a):
    gen=''.join(random.choices(lis,k=1))

    try:
        out=input("Enter any of these three (Gun, Water, Snake) : ")
        if out.lower() in lis:
            pass
        else:
            print("please check your spelling of entered item (snake, gun, water)")
            print("\n You loose one chance because of your spelling mistakes\n")
        
    except:
        print("please check your spelling of entered item (snake, gun, water) ")
    if gen == out:
        print("gen=",gen)
        print(f"!!..Game is tie..!!, because you both choose {gen}")
        tie+=1
    elif gen=='gun' and out.lower()=='water':
        print("gen=",gen)
        print("You won..!! because your water destroy gun")
        count+=1
    elif gen=='gun' and out.lower()=='snake':
        print("gen=",gen)
        print("You loose..!! because your snake got killed by gun")
    elif  gen=='water' and out.lower()=='snake':
        print("gen=",gen)
        print("You won!! because your snake drink water")
        count+=1
    elif  gen=='water' and out.lower()=='gun':
        print("gen=",gen)
        print("You loose..!! because your gun get destroyed by water")
    elif  gen=='snake' and out.lower()=='gun':
        print("gen=",gen)
        print(f"You won..!! because your {out} kill {gen}")
        count+=1
    elif  gen=='snake' and out.lower()=='water':
        print("gen=",gen)
        print(f"You loose..!! because your {out} killed by {gen}")
print(f"\n you got win {count} times, got tie {tie} times, while playing {a} times")
print(f"\nyou win {(count/(a-tie))*100} % of the game")
