# for loop eg. finding the sum of something
total = 0
for i in range(5):
  total += 8

print(total)

vowels = ['a', 'e', 'i', 'o', 'u']
word = input()
count = 0
for letter in word: 
  if letter in vowels:
    count += 1 
print(count)

# alternative 
for i in range(len(word)):
  if word[i] in vowels:
    count += 1
print(count)
