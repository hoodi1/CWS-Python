#a = ["even" if i%2 == 0 else "odd" for i in range(1,11)]
#a = [f"even - {i}" if i%2 == 0 else f"odd - {i}" for i in range(1,11)]
#print(a)

print(sum([i for i in range(int(input("Enter start no: ")), int(input("Enter end no: ")) + 1)]))

#print even numbers
print([i for i in range(1,11) if i%2 == 0])