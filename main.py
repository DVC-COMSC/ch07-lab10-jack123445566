Product = list(map(int, input().split( )))
print(Product)
for i in range(len(Product)):
    smallest = 0
    for j in range(0,len(Product)-i):
        crrnt_index = i+j
        if smallest == 0:
            smalles = Product[crrnt_index]
            ind = crrnt_index
        if Product[crrnt_index] < smallest:
            smallest = Product[crrnt_index]
            ind = crrnt_index
    Product[i],Product[ind] = Product[ind],Product[i]
    print(Product)

