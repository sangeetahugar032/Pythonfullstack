opening_stock=[50,30,20,40]
closing_stock=[45,35,15,50]
for i in range(len(opening_stock)):
    if closing_stock[i]>opening_stock[i]:
        print("product",i+1,"stock increased")
    elif closing_stock[i]<opening_stock[i]:
        print("product",i+1,"stock reduced")
    else:
        print("product",i+1,"stock unchanged")
        
    
