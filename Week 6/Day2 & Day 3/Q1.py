def marks(phy,chem,eng,sst):
    Total = phy+chem+eng+sst
    print(f"Total marks : {Total}")
    percentage = (Total/400)*100
    print(f"Percentage : {percentage}% ") 

marks(88,78,90,99)