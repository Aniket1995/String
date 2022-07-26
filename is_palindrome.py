def isPal2(s):

    if(s is None): 
        return True
        
    l=len(s)
    
    if(l == 0 or l == 1):
        return True
    
    for i in range(0,l//2):
        if(s[i] != s[(i+1)*-1]):
            return False
            
    return True



def main(s):
    print(s+" -> "+str(isPal2(s)))


# main("abcd")
# main("abcba")
# main("a")
# main("aba")
main("dddbddd")
main("abccba")
main("abcdcba")
main("abcdscba")
