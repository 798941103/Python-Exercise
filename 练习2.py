def yang(n):
    i,j,a = 1,0,1
    while i<=n:
        while j <= (n-j)/2:
            print(" ")
            j = j + 1
        j = 0
        while j < i:
            yield a

            j = j + 1
        i=i+1