# write a program to print 1 to n number recursively
"""def rec(n):
    if(n<1):
        return
    else:
        rec(n-1)
        print(n,end="\t")


rec(int(input("Enter a +ve number: ")))"""

# tail recursion for 1 to n number

def recTail(n,k=1):
    if(n<1):
        return
    else:
        print(k,end="\t")
        return recTail(n-1,k+1)


rec(int(input("Enter a +ve number: ")))

