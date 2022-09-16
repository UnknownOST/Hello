def circumf():
    r=int(input("radius"))
    pie=3.14
    circ=2*pie*r
    area=pie*r**2
    return(circ,area)

ans=circumf()
print("the circumference and area",ans)
