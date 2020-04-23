from itertools import permutations
#import psyco

def answer(L):
    length = len(L)
    L.sort(reverse=1)
    #print "Hello"
    for i in xrange(length,0,-1):
        #print "Hello"
        hold = (int(''.join(map(str,subset))) for subset in permutations(L,i))
        #ret= (r for r in hold if r%3==0)
        #print "Hello"
        #yield next(ret)
        for i in hold:
            if i%3==0:
                yield i
                break
            #ret(i)
            #break
        #for i in ret:
            #print i
        #return ret
    yield 0

#from itertools import permutations
#
# def answer(l):
#     length = len(l)
#     print length
#     #l.sort(reverse=1)
#     #list.sort(l)
#     #hold = []
#     #hold.append(int(''.join(map(str,sub)))for sub in permutations(l))
#
#     for i in xrange(length,0,-1):
#         for subset in permutations(l,i):
#             # print subset
#             # hold = int(''.join(map(str,subset)))
#             hold = int(''.join(map(str,subset)))
#             if hold%3==0:
#                 return hold
#     # for j in hold:
#
#     #         if hold%3==0:
#     #             return hold
#     return 0
#
# def perms(l,len,holds):
#     #holds = []
#     #l.sort(reverse=1)
#     while (len>0):
#         for i in permutations(l,len):
#             holds.append(int(''.join(map(str,i))))
#             #print i
#             perms(l,len-1,holds)
#     return holds
# def answer(l):
#     holds = []
#     length = len(l)
#     holds.append(perms(l,length,holds))
#     for i in holds:
#         print i
l = [3,1,4,1,5,9,3,8,7]
print answer(l)
