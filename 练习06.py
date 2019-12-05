def Number_of_tracts(n):
    n2 = str(n)
    return n2  == n2[::-1]

a = int(input("Input:"))
print(list(filter(Number_of_tracts,range(100,a))))
