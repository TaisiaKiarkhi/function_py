number = 4

def say_hi():
    print("Hello user")

print("Top")

say_hi()

print ("Button")

def print_name(name):
    print(name)

print_name("Alex")

def func(name, age, adress):
    surname = name
    data_born = age
    home = adress

    list_data = [surname, age, adress]
    print("Age: "+str(list_data[1]))
    list_data.append("Boy")
    print("Gender: "+ list_data[-1])

func("Ben", 24, "New York 23")

def age_changer(age):
    return age +1

age_ = 21
new_age = age_changer(age_)
print(str(new_age))