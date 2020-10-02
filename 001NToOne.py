# write a program to print n to 1 numbers recursively

def rec(n):
    if(n<1):
        return
    else:
        print(n,end="\t")
        return rec(n-1)


rec(int(input("Enter a +ve number: ")))
