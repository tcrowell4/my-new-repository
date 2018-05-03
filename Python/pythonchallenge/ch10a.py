"""
"what are you looking at"

len(a[30])? == len(a[30]) = 5808

http://www.pythonchallenge.com/pc/return/5808.html

sequence.txt

x = [1, 2,  3,  5,    8,      13
a = [1, 11, 21, 1211, 111221,
    [1, 11, 21, 2111, 221111, 2221111111,   <== "2111" + "221111"
This seemed the logical progession.  it appeared the order didn't matter just add the previous characters to current
one.

This is a "speak and say" sequence"

"""
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

    a = ['1', '11', '21', '1211', '111221']
    
    
    for xx in range(len(a)-1,31):
        #print(xx, a[xx-1] + ax[x])
        nxt = nextseq(a[xx])
        a.append(nxt)
        #print("Next seq =  %s" % nxt)

    entry = 30

    print("entry = %d   len(a[%d]) = %d" % (entry, entry, len(a[entry])))

if __name__ == "__main__":
    main()
