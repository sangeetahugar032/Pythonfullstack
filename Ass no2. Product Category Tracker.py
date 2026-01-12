products={
    "Laptop":"Electronic",
    "Chair":"Furniture",
    "Mobile":"Electronic"
    }
print("Product Names:")
for product in products.keys():
    print(product)

print("/ncategegories:")
for categeory in set(products.values()):
    print(categeory)
    
total_products=len(products)
print("\nTotal number of products:",total_products)
