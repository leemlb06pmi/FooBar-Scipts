ans = 0

def genID(n,b):
    length = len(n)
    x = ''.join(sorted(n))
    y = ''.join(sorted(n, reverse=True))
    xb = int(x,b)
    yb = int(y,b)
    z = abs(xb - yb)
    zB = toBaseB(z,b)
    if len(zB) != length:
        diff = abs(len(zB)-length)
        return'0'*diff+zB
    return zB #as a string

def toBaseB(n,b):
    s = ""
    while n:
        s = str(n % b) + s
        n /= b
    return s

def assign(a,n,b):
    global ans
    z = genID(n, b)
    if z in a:
        ans = ((len(a)-1)+1) - a.index(z)
        return
    else:
        a.append(z)
        assign(a,z,b)

def answer(n,b):
    totalArr = []
    totalArr.append(n)
    assign(totalArr,n,b)
    return ans

print answer('210022',3)
