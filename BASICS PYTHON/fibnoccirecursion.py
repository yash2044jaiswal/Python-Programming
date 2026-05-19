def fibnocci(n):
    if(n==1 or n==0):
        return n
    else:
        return fibnocci(n-1)+fibnocci(n-2)

term=5
series=[fibnocci(i) for i in range(term)]
print(series)