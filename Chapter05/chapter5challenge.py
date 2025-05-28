# Tuple of favorite singers
favourite_singers = ("Michael Jackson", "Elvis", "Jon Bon Jovi")
print(favourite_singers)

# Dictionary of places and their coordinates
places = {
    "okinawa": {"latitude": 21.0285, "longitude": 105.8542},
    "fukuoka": {"latitude": 10.8231, "longitude": 106.6297},
    "tokyo":   {"latitude": 16.0471, "longitude": 108.2068},
    "sendai":  {"latitude": 40.7128, "longitude": -74.0060}
}

# Corrected loop to print place coordinates
for city, coords in places.items():
    print(f"{city} => Latitude: {coords['latitude']}, Longitude: {coords['longitude']}")

# Dictionary of key-to-food mappings
key_to_food = {
    "a": {"name": "Pizza", "calories": 285},
    "s": {"name": "Sushi", "calories": 200},
    "d": {"name": "Pho", "calories": 350},
    "f": {"name": "Burger", "calories": 500}
}

# Simulate a key press for food
pressed_key = "d"

if pressed_key in key_to_food:
    food = key_to_food[pressed_key]
    print(f"You selected: {food['name']} 🍜 - {food['calories']} calories")
else:
    print("Unknown food key.")

# Dictionary of key-to-Japanese-musician mappings
key_to_musician = {
    "a": {"musician": "米津玄師 (Kenshi Yonezu)", "song": "Lemon"},
    "s": {"musician": "Aimer", "song": "残響散歌 (Zankyou Sanka)"},
    "d": {"musician": "LiSA", "song": "紅蓮華 (Gurenge)"},
    "f": {"musician": "YOASOBI", "song": "夜に駆ける (Yoru ni Kakeru)"},
    "g": {"musician": "宇多田ヒカル (Utada Hikaru)", "song": "First Love"},
    "h": {"musician": "King Gnu", "song": "白日 (Hakujitsu)"},
    "j": {"musician": "RADWIMPS", "song": "前前前世 (Zenzenzense)"}
}

# Simulate a key press for music
pressed_key = "f"

if pressed_key in key_to_musician:
    artist = key_to_musician[pressed_key]
    print(f"{artist['musician']} 🎤 — 「{artist['song']}」")
else:
    print("No musician assigned to that key.")

