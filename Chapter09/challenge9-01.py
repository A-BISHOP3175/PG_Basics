import subprocess
import os

# Run a command to list files (works on Windows, Mac, and Linux)
result = subprocess.run(["dir"] if os.name == "nt" else ["ls"], capture_output=True, text=True)

# Print the output from the command
print(result.stdout)

# Ask a question
user_input = input("What's your favorite color? ")

# Save the answer to a file
with open("answer.txt", "w") as file:
    file.write(user_input)

print("Your answer has been saved to 'answer.txt'.")

import csv

# Two lists of movies
tom_cruise_movies = ["top gun", "risky business", "minority report"]
denzel_movies = ["titanic", "the revenant", "inception", "training day", "man on fire", "flight"]

# Combine the lists
all_movies = tom_cruise_movies + denzel_movies

# Write to a CSV file
with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title"])  # Optional header
    for movie in all_movies:
        writer.writerow([movie])

# Print the combined list
print("Combined Movie List:")
for movie in all_movies:
    print(movie)
# Read the file
with open("Top gun", "r", encoding="utf-8") as file:
    content = file.read()

# Replace "Top Gun" with the Japanese version
translated = content.replace("Top Gun", "トップガン")

# Print the result
print(translated)

