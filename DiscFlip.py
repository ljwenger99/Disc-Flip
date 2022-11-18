#Lucas Wenger
#5/9/2022
#Disc Flip Problem

'''
Built to solve special cases of a problem a friend (Cameron Byer) came up with:

Given n distinct objects, if we flip the top one, then a stack of the top two,
then a stack of the top 3, etc. (looping back to 1 after reaching n), how many
flips until we get back to our beginning arrangement? 
'''

def switch(lyst,n):
    '''
Reverses the first n elements of a list and turns them on/off.
    '''
    lyst_1 = lyst[:n]
    lyst_1.reverse()
    lyst_2 = lyst[n:]
    lyst = lyst_1+lyst_2
    for i in range(n):
        lyst[i] = (lyst[i]+1)%2
    return lyst
    

def flip(n):
    '''
Tests the flip procedure on n discs and counts how many flips it takes.
    '''
    n = int(n)
    disclist = [0 for disc in range(n)] #list of n discs
    print(disclist)
    back_to_start = False
    counter = 0
    while back_to_start == False:
        for numflips in range(1,n+1):
            disclist = switch(disclist,numflips)
            counter += 1
            print(disclist)
            if disclist == [0 for disc in range(n)]:
                back_to_start = True
                break
            else:
                continue
    print("With",n,"discs, it takes",counter,"flips to complete a cycle.")
    return
