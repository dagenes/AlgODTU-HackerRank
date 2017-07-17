transformable =  {1:2,
                  2:1,
                  1:3,
                  2:3,
                  3:2,
                  2:7,
                  3:7,
                  1:7,
                  7:3,
                  7:2,
                  7:1,
                  3:1,
                  4:5,
                  5:4,
                  6:8,
                  8:6,
                  9:6,
                  6:9,
                  8:9,
                  9:8,
                  10:5,
                  5:10,
                  10:4,
                  4:10}

palindromes = []

#
#for key in transTable:
#    if key in transformable:
#        transformable[transformable[key]] = transTable[key]
#
#    transformable[key] = transTable[key]
#    transformable[transTable] = transTable[key]

def isTransform(frm, to):
    if frm in transformable:
        if transformable[frm] == to:
            return True

    return False



def cutHead(dizi):
    clone = dizi[:]
    del clone[0]
    return clone

def cutTail(dizi):
    clone = dizi[:]
    del clone[-1]
    return clone

def cutHeadTail(dizi):
    clone = dizi[:]
    del clone[0]
    del clone[-1]
    return clone



# dizi: List that will trasformed to palindrome
# isNew: Does that dizi wished to new palindrome, if not that means dizi is middlePart of another palindrome and there must be return
def node(dizi, isNew):
    # First of all our dizi must be greater or equal to 2
    if len(dizi) >= 2:
        if isNew:
            #Check that first element and last element can transform
            if isTransform(dizi[0], dizi[-1]):
                # Ow, we have new palindrome, create single node without first and last elements of dizi
                # process middlePart of our new palindrome
                middlePart = node(cutHeadTail(dizi), False)
                # Since first and last elements are transformable, set last element as first and put middlePart between them
                palindrome = [dizi[0]] + middlePart + [dizi[0]];
                palindromes.append(palindrome)

                # To enjoy a bit :D
                if len(palindrome) > 3:
                    print palindrome

            else:
                # We are trying to create new palindrome but our head and tail doesn't think so, let cut them
                # We have three posible branch: without first, without last and without both
                # Our branches will try to create new palindrome
                node(cutHead(dizi), True) # Without first
                node(cutTail(dizi), True) # Without last
                node(cutHeadTail(dizi), True) # without first and last
        else:
            # It seems that our parent looking for palindrome set, lets give him what he want
            if isTransform(dizi[0], dizi[-1]): # First look that does our dizi can be palindrome
                # Yeah, we can be...
                # continue in our parent way, take first element and process middlePart of palindrome
                middlePart = node(cutHeadTail(dizi), False)
                # Since first and last elements are transformable, set last element as first and put middlePart between them
                palindrome = [dizi[0]] + middlePart + [dizi[0]];
                return palindrome # give our parent what he want
            else:
                # It seems that dizi can not be palindrome, now I will look for longest palindrome from my three branch
                firstPal = node(cutHead(dizi), False)
                secondPal = node(cutTail(dizi), False)
                # check which one is longest
                longest = firstPal if len(firstPal) > len(secondPal) else secondPal

                # get thirdPal
                thirdPal = node(cutHeadTail(dizi), False)

                # get last result of longest palindrome
                longest = longest if len(longest) > len(thirdPal) else thirdPal

                # Give our parent what he want
                return longest;
    else:
        # dizi can be 1 sized list or not, just return it
        return dizi




dizi = [1,4,5,7,9,8,1,3,10,4,5,10,2,7,8]
node(dizi, True) # Let find all palindromes dude
