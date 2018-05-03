def binarySearch(ord, num):
    print(ord, num)
    head = 0
    y = len(ord)
    tail = len(ord)

    while y > 1:
        print(ord[head:tail], head, y)
        y = len(ord[head:tail])
        if num == ord[head:tail][y//2]:
            return True
        if num < ord[head:tail][y//2]:
            tail = tail-y//2
            print("Left   {}:{} y={} {}".format(head,tail,y,y//2))
        else:
            head = head+y//2
            print("Right  {}:{} y={} {}".format(head,tail,y,y//2))

    return False  
            
def main():
    num = 1
    a = [1, 3, 5, 22, 30, 42, 43, 99, 325, 500]
    #if binarySearch(a,num):
    #    print ("found")
    print(binarySearch(a,num))
    
if __name__ == "__main__":
    main()
