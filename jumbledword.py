import random
def choose():
    words=['beautiful','computer','locket','water','university','sincere','people','psychology']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
def thanks(p1n,p2n,p1p,p2p):
    print("thank you for playing")
    print("the points table is as below")
    print(p1n," has",p1p," points and ",p2n," has ",p2p," points.")
    
def play():
    p1n=input("please enter first player name:")
    p2n=input("please enter second player name:")
    p1p=0
    p2p=0
    turn=0
    while(1):
        picked_word=choose()
        jumble_word=jumble(picked_word)
        print("The word is:",jumble_word)
        if(turn%2==0):
            print("your turn ",p1n)
            chosen=input("give the answer:")
            if(chosen==picked_word):
                print("you are correct")
                p1p=p1p+1
                print(p1n,"your point is:",p1p)
            else:
                print("its wrong i had thought ",picked_word)
                print("better luck next time:")
            n=input("press 1 if you want to continue if not press 0:")
            x=int(n)
            if(x==0):
                thanks(p1n,p2n,p1p,p2p)
                break
        else:
            print("your turn ",p2n)
            chosen=input("give the answer:")
            if(chosen==picked_word):
                print("you are correct")
                p2p=p2p+1
                print(p2n,"your point is:",p2p)
            else:
                print("its wrong i had thought ",picked_word)
                print("better luck next time:")
            n=input("press 1 if you want to continue if not press 0:")
            x=int(n)
            if(x==0):
                thanks(p1n,p2n,p1p,p2p)
                break
        turn=turn+1
play()



