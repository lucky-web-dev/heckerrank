def main():
    n=int(input())
    i=0
    f=0
    while f==0:
        if int(2**i)>n:
            f=i-1
        if int(2**i)==n:
            f=i
        i+=1
    f=n-2**(f)
    print(2*f+1)

if __name__=='__main__':
    main()
    
