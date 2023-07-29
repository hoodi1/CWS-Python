#a = ["aeroplane", "car", "boat"]
a = [12,23,45,67,889]

b = " | ".join(str(i) for i in a)
print(b)
print(type(b))