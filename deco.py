def wrapper(f):
    def fun(l):
        le=len(l)
        for i in range(le):
            a=l[i]
            s=str(a)
            s="+91", s[-10:-5],s[-5:-1]+s[len(s)-1]


    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
