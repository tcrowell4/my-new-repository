def nextseq(current):
    hold = ""
    last = " "
    next = ""
    for counter, value in enumerate(current,0):
        #print(a, value, counter)
        if value == last:
            hold = hold+value
        elif last != " ":
            #print("number consecutive: %d digit= '%s' " % (len(hold), last))
            next = next + str(len(hold)) +last
            last = value  # reinit
            hold = value
        else:
            hold = value
            last = value
    #print("number consecutive: %d digit= '%s' " % (len(hold), last))
    next = next + str(len(hold)) + last
            
    #print("Next seq =  %s" % next)
    return(next)

def main():
    # my code here
    a = "111221"
    nxt = nextseq(a)
    print("Next seq =  %s" % nxt)
    
if __name__ == "__main__":
    main()
    
