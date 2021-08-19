A={1,2,3,8}
B={3,4}

print(1 in A)
print(4 in A)

flag= 4 in A
type (flag)
print(B.issubset(A))

def f_issubset(A,B):
    for e in A:
        if e in B:
            pass
        else:
            return False
    return True
print(f_issubset(B,A))
print(f_issubset({2,3,4},{1,2,3,4,5,6}))            