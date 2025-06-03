tvShows = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for show in tvShows:
    print(show)

for i in range(25, 51):
    print(i)

colors = {"green": "grass",
          "blue": "sky",
          "yellow": "sun",
         }

for objects in colors:
    print(objects)


correct_numbers = [5, 23, 12, 49, 8]

while True: 
    user_input = input("Guess a number (or 'q' to quit): ")
     
    if user_input.lower() == 'q':
        break

    if user_input.isdigit():
        guess = int(user_input)
        if guess in correct_numbers:
            print("Correct!")
        else:
            print("Incorrect!")
        break

    else:
        print("Enter a number or q to exit")


list1 = [8, 19, 148, 4] 
list2 = [9, 1, 33, 83]

added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)        
