# empty dictionary
product = {}

# infinite loop for Inventory only breaks when user asks to exit
while True:
    print("1 -> Add a product ")
    print("2 -> Update a product ")
    print("3 -> Delete a product ")
    print("4 -> View all product ")
    print("5 -> Exit ")

    a = int(input("Please choose an option (1-5): "))

    # Add a product
    if a == 1:
        print("Add a product")
        name = input("Enter product name: ")
        pid = input("Enter product ID: ")
        quant = input("Enter quantity: ")
        price = input("Enter price: ")
     
        product[pid] = {"Name": name, "Quantity": quant, "Price": price}    
        print("Product added succesfully!\n")

    # update a product
    elif a == 2:
        print("Update a product")
        pid = input("Enter Product ID: ")
        if pid in product:
            print("Product found!")
            name = input("Enter new product name (Leave blank to keep the value same): ")
            quant = input("Enter new quantity (Leave blank to keep the value same): ")
            price = input("Enter new price (Leave blank to keep the value same): ")
            if name:
                product[pid]["Name"] = name
            if quant:
                product[pid]["Quantity"] = quant
            if price:
                product[pid]["Price"] = price
            print("Product Updated successfully")
        else:
            print("Product not found.\n")
  
    # Delete a product
    elif a == 3:
        print("Delete a product")
        pid = input("Enter product id: ")
        if pid in product:
            del product[pid]
            print("Product deleted successfully")
        else:
            print("Product not found.")

    # View all products
    elif a == 4:
        print("View all product")
        print()
        if product:
            for k,v in product.items():
                print("Product ID:",k)
                print("Product Name:",v["Name"])
                print("Product Quantity:",v["Quantity"])
                print("Product Price:",v["Price"])
                print()
        else:
            print("No Product found")
            print()

    # exit
    elif a == 5:
        print()
        print("Exiting the app... ")
        print()
        break
    
    else:
        print("Invalid choice. Please select a valid option.\n")