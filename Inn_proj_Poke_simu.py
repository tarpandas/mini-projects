import random
print("---------Pokemon - Ultimate Showdown----------\n")

def main():
    print("Available Pokemon for each party:\n1 : Venusaur\n2 : Blastoise\n3 : Charizard\n")
    print("Note:\n->Venusaur is Grass type\n->Blastoise is Water type\n->Charizard is Fire type\nChoose your Pokemon wisely\n")
    argument1=int(input("Player 1 choose a pokemon(Enter 1 through 3):"))
    if argument1==1 or argument1==2 or argument1==3:
        print("Player 1 chooses ",pokemon1(argument1))
    else:
        print("So, you decided not to fight!")
        re_match()
    print("\n")

    argument2=int(input("Player 2 choose a pokemon(Enter 1 through 3):"))
    if argument2==1 or argument2==2 or argument2==3:
        print("Player 2 chooses ",pokemon2(argument2))
    else:
        print("So, you decided not to fight!")
        re_match()
    print("\n")

    b=0
    d=0

    if argument1==1 and argument2==2:
        adv1(b,d, argument1, argument2)
    elif argument1==2 and argument2==3:
        adv1(b,d, argument1, argument2)
    elif argument1==3 and argument2==1:
        adv1(b,d, argument1, argument2)
    elif argument2==1 and argument1==2:
        adv2(b,d, argument1, argument2)
    elif argument2==2 and argument1==3:
        adv2(b,d, argument1, argument2)
    elif argument2==3 and argument1==1:
        adv2(b,d, argument1, argument2)
    else:
        equ(b,d, argument1, argument2)
    
def adv1(b,d, argument1, argument2):
    for i in range(1,11,+1):
            print("Attack set:",i,"------------------")
            a= random.randint(1,10)
            b=a+b
            print(" Damage by ", pokemon1(argument1), ": ", a)
            if a >= 8 and a<10:
                print(" ~~~~~~~~~~Super Effective")
            elif a==10:
                print(" ~~~~~~~~~~Critical Hit!")
           
            c= random.randint(1,6)
            d=c+d
            print(" Damage by ", pokemon2(argument2), ": ", c)
            
    print("\n")
    print("Total Damage by", pokemon1(argument1), ": ", b)
    print("Total Damage by", pokemon2(argument2), ": ", d)
    print("\n")
    
    if b>d:
        print( "Player 1's",pokemon1(argument1),"wins")
    elif b==d:
        print( pokemon1(argument1),"and",pokemon2(argument2),"drew")
    else:
        print( "Player 2's",pokemon2(argument2),"wins")

    re_match()
    print("\n")

    
def adv2(b,d, argument1, argument2):
    for i in range(1,11,+1):
            print("Attack set:",i,"------------------")
            a= random.randint(1,6)
            b=a+b
            print(" Damage by ", pokemon1(argument1), ": ", a)
            
            c= random.randint(1,10)
            d=c+d
            print(" Damage by ", pokemon2(argument2), ": ", c)
            if c >= 8 and c<10:
                print(" ~~~~~~~~~~Super Effective")
            elif c==10:
                print(" ~~~~~~~~~~Critical Hit!")
    print("\n")
    print("Total Damage by", pokemon1(argument1), ": ", b)
    print("Total Damage by", pokemon2(argument2), ": ", d)
    print("\n")
    
    if b>d:
        print( "Player 1's",pokemon1(argument1),"wins")
    elif b==d:
        print( pokemon1(argument1),"and",pokemon2(argument2),"drew")
    else:
        print( "Player 2's",pokemon2(argument2),"wins")

    re_match()
    print("\n")

def equ(b,d, argument1, argument2):
    for i in range(1,11,+1):
            print("Attack set:",i,"------------------")
            a= random.randint(1,8)
            b=a+b
            print(" Damage by ", pokemon1(argument1), ": ", a)
           
            c= random.randint(1,8)
            d=c+d
            print(" Damage by ", pokemon2(argument2), ": ", c)
            
    print("\n")
    print("Total Damage by", pokemon1(argument1), ": ", b)
    print("Total Damage by", pokemon2(argument2), ": ", d)
    print("\n")
  
    if b>d:
        print( "Player 1's",pokemon1(argument1),"wins")
    elif b==d:
        print( pokemon1(argument1),"and",pokemon2(argument2),"drew")
    else:
        print( "Player 2's",pokemon2(argument2),"wins")

    re_match()
    print("\n")

def pokemon1(argument1):
    my_pokemon = {
        1 : "Venusaur_1",
        2 : "Blastoise_1",
        3 : "Charizard_1"
        }
    return my_pokemon.get(argument1)

def pokemon2(argument2):
    my_pokemon = {
        1 : "Venusaur_2",
        2 : "Blastoise_2",
        3 : "charizard_2"
        }
    return my_pokemon.get(argument2)

def re_match(): 
    fight = input("\nWant to fight again? (Y/N): ")
    if fight == 'y' or fight =='Y':
        main()
        re_match()
    else:
        print("\nOK, I get it, your Pokemons need to rest too, Right?")
        exit()

if __name__=="__main__":
    main() 
