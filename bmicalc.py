def bmi(weight,height):
    return weight/(height**2)

w=int(input("enter the persons weight"))
h=int(input("enter the persons height"))
person=bmi(w,h)
print(person)
