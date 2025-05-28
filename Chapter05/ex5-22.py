countries = {"1": "Japan", 
             "2": "Korea",
             "3": "Taiwan", 
             "4": "Vietnam",
             "5": "Germany",
             "6": "France",
             "7": "Italy",
             "8": "Hong Kong",
             "9": "New Zealand",
             "10": "Canada"}

n = input("数字を入力してください:")
if n in countries:
    country = countries[n]
    print country
else:
    print("見つかりません”)



