count = 0
name = str(input("What is your name?"))

while count < 5:
    print(name, "is awesome!")
    count += 1

for i in range(5, 11):
    print(i)




Names = ["Tadas", "Gary", "Simon", "Will", "Scott"]
for name in Names:
    print(name + " is Awesome!")


word=input("Enter a word: ").lower()
vCount=0
for char in word:
    if char in ("a","e","i","o","u"):
        vCount += 1
print("No. of vowels in the word = ", vCount)
