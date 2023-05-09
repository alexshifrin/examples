from collections import Counter


with open("input.txt", "r") as file:
    file_text = file.read().splitlines()

print(file_text)

text = ""

for line in file_text:
    print(line)
    text += line + " "

word_counts = Counter(text.split())

print(word_counts)