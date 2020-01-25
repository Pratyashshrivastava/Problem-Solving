import math
import string

# lisStr = '217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053'
lisStr = '3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543'
if __name__ == "__main__":
    lisStrSplit = lisStr.split(' ')
    lis = [int(i) for i in lisStrSplit]
    #Successfully obtained a list of integers. preprocessing done.
    seq = []
    p = int(math.gcd(lis[0],lis[1]))
    for i in range(len(lis)-1):
        p = int(math.gcd(lis[i],lis[i+1]))
        seq.append(int(lis[i]/p))
    p = int(math.gcd(lis[-1],lis[-2]))
    seq.append(p)
    seq.append(int(lis[-1]/p))
    print(seq)
    sseq = sorted(set(seq))
    print(sseq)
    alphabets = list(string.ascii_lowercase)
    zipped = dict(zip(sseq,alphabets))
    ret = ''
    for i in seq:
        ret += str(zipped[i])
        
    print(ret)

    
