def sqr_num(num):
    return num ** 16

def print_string(potato):
    print(potato)

def describe_person(name, age, country, hobby="reading", pet="none"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print(f"Hobby: {hobby}")
    print(f"Pet: {pet}")

def divide_by_two(number):
    return number // 2

def print_result(value):
    print(f"The final result is: {value}")

input_number = 50
half = divide_by_two(input_number)
print_result(half)

def abc(s):
    try:
        return float(s)
    except ValueError:
        print("Error: Cannot convert to float.")
        return None

def print_random_message():
    """
    Prints a random, fun message.
    """
    print("Bananas are blue on Jupiter!")

print_string("Hello, world!")
describe_person("Aiden", 25, "New Zealand", "Programming", "Cat and Dog")
print(f"2 to the power of 16 is: {sqr_num(2)}")
print(f"Converted float: {abc('3.14')}")
print(f"Try bad float: {abc('abc')}")
print_random_message()






