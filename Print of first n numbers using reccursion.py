#printing of 5 numbers recursion

'''def countdown(n):
    if n <= 0:
        return 
        
    if n>0:
        print(n)
        countdown(n-1)
        print(n)

countdown(5)'''

def fun(n):
    if n<=0:
        return 
    fun(n-1)
fun(5)

#return 1 to 5
def fun(n,l):
    if n == 6:
        return l
    l.append(n)
    t = fun(n+1,l)
    return t
print(fun(1,[]))

#return 5 to 1
def fun(n,l):
    if n == 0:
        return l
    l.append(n)
    t = fun(n-1,l)
    return t
print(fun(5,[]))

#OR

def fun(n,l):
    if n == 6:
        return l
    t = fun(n+1,l)
    l.append(n)
    return t
print(fun(1,[]))

#Head recursion - first recursion line - than execution
#Tail recursion - first execution - than recursion line

#return sum of first n numbers
def fun(n,sum):
    if n == 6:
        return sum
    sum += n
    t = fun(n+1,sum)
    return t
sum = 0
print(fun(1,sum))

#return sum of the list
def fun(l,i,s):
    if i==len(l):
        return s
    s += l[i]
    return fun(l,i+1,s)
    
l = [1,2,3,4,5]
index = 0
sum = 0
print(fun(l,index,sum))

#print only even numbers of the list
def fun(l,i,even):
    if i==len(l):
        return even
    if l[i] % 2 == 0:
        even.append(l[i])
    return fun(l,i+1,even)
    
l = [1,2,3,4,5]
index = 0
sum = 0
print(fun(l,index,[]))

#print only odd numbers of the list
def fun(l,i,odd):
    if i==len(l):
        return odd
    if l[i] % 2 != 0:
        odd.append(l[i])
    return fun(l,i+1,odd)
    
l = [1,2,3,4,5]
index = 0
sum = 0
print(fun(l,index,[]))

#print sum of only odd numbers of the list
def fun(l,i,s):
    if i==len(l):
        return s
    if l[i] % 2 != 0:
        s += l[i]
    return fun(l,i+1,s)
    
l = [1,2,3,4,5]
index = 0
sum = 0
print(fun(l,index,sum))

#print sum of only even numbers of the list
def fun(l,i,s):
    if i==len(l):
        return s
    if l[i] % 2 == 0:
        s += l[i]
    return fun(l,i+1,s)
    
l = [1,2,3,4,5]
index = 0
sum = 0
print(fun(l,index,sum))

#print sum of even and odd numbers of the list
def fun(l,i,s1,s2):
    if i==len(l):
        return s1,s2
    if l[i] % 2 == 0:
        s1 += l[i]
    elif l[i] % 2 != 0:
        s2 += l[i]
    return fun(l,i+1,s1,s2)
    
l = [1,2,3,4,5]
index = 0
sum1,sum2 = 0,0
print(fun(l,index,sum1,sum2))