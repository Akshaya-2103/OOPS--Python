def reverse_of_list(l,n,i):
    if i == n:
        return l
    l[i],l[-1-i] = l[-1-i],l[i]
    return reverse_of_list(l,n,i+1)

l = [2,3,5,6,7,9,11]
n = (len(l)//2)+1
print(reverse_of_list(l,n,0))



def reverse_of_list(l,n):
    if n < 0:
        return l
    l[n],l[-1-n] = l[-1-n],l[n]
    return reverse_of_list(l,n-1)

l = [2,3,5,6,7,9,11]
n = (len(l)//2)+1
print(reverse_of_list(l,n))


