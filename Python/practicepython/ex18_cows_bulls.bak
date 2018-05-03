import random


def randN(n):
    assert n <= 10
    l = list(range(10)) # compat py2 & py3
    #print(l)
    while l[0] == 0:
        random.shuffle(l)
    #print(l)
    return ''.join(str(d) for d in l[:n])

def checkGuess(g,x):
    bulls = 0
    cows = 0
    #print("g = {} x = {}  type {}".format(g,x,type(x)))
    for i in range(len(x)):
        #print(x[i:i+1])
        for j in range(len(x)):
            #print("\t{}".format(g[j:j+1]))
            if x[i:i+1] == g[j:j+1] :
                #print("match")
                if i == j :
                    bulls += 1
                else:
                    cows += 1
    print("Guess = {}  Bulls {}  Cows {}".format(g,bulls,cows))
    return(bulls)
            
def main():
    x = randN(4)
    while True:
        n = input("\n\nEnter 4 digit guess: ")
        if len(n) == 4:
            bulls = checkGuess(n,x)
            if bulls == 4:
                print("Congratulations!!!")
                break
        elif len(n) < 4:
            print ('Thanks for playing ... Number was {}'.format(x))
            break

if __name__ == "__main__":
    main()
