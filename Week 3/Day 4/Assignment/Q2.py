'''Make your own list of numbers. Ask a start and end position
from User. Make another different list which will contain number
from start to end position. Use slicing logic.'''

a=[10, -5, 8, 3, -1, -9, 7, 2]

start = int(input("Enter start position= "))
end = int(input("Enter end position= "))

result = a[start:end]

print(f"result = {result}")

