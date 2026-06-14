text = input("Enter a sentence or paragraph: ")

characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")
vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("\nText Statistics")
print("---------------")
print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentences)
print("Vowels:", vowels)