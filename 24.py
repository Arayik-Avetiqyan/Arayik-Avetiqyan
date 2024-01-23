def asa(first, last , city, age = ""):
    person = {"first" : first, "last" : last, "city" : city}
    if age:
        person["age"] = age
    else:
        person = {"first": first, "last" : last, "city" : city}
    return person
b = asa("Arayik", "Avetiqyan", "Vanadzor", "54")
print(b)
c = asa("first", "last", "Vanadzor")
print(c)
d = asa(last = "Avetiqyan", first = "Angelina", city = "Vanadzor")
print(d)


def kas(first, last):
    full_name = first + " " + last
    return full_name.title()
while True:
    f_name =  input("first_name ")
    if f_name == "q":
        break
    l_name =  input("last_name ")
    if l_name == "q":
        break
    d = kas(f_name, l_name)
    print(d)

