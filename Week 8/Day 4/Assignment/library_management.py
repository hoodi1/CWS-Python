class Library:
    
    def __init__(self) -> None:
        self.title = input("Enter title of the book : ")
        self.author = input("Enter author of the book : ") 
        self.num_copies = int(input("Enter number of copies of the book : "))
        self.borrowers = [] 

    def display_books(self):
        print()
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Number of copies : {self.num_copies}")
        print()

while True:
    print()
    
    print()