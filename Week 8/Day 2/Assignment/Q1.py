'''Write a Python class named Book with a constructor that takes
a title, an author, and a price as arguments and initializes three
instance variables, title, author, and price. Write a method named
discount that applies a discount to the price and returns the
discounted price.'''

class Book:
    title = ""
    author = ""
    price = 0

    def __init__(self,t,a,p):
        self.title = t
        self.author = a
        self.price = p

    def discount(self,percentage):
        self.discount_amount = self.price*(percentage/100)
        self.discount_price = self.price - self.discount_amount
        print(f"Discounted price is : ${self.discount_price}")

b1 = Book("Ikigai","Makoto",400)   
b1.discount(10)     # taking 10% discount
         

