#love calculator
name1 = input("Your name: ")
name2 = input("Her or His name: ")
name1 = name1.lower()
name2 = name2.lower()
combined_string = name1 + name2
logic = "true love"
#True Love
a = 0
b = 0
for i in combined_string:
    a = a + "true".count(i)
    b = b + "love".count(i)
score = int(str(a)+str(b))
if score < 40:
    print("You guys will be like coke and mentos!:0")
    print(f"Your score is {score}%")
elif score < 60:
    print("Well you guys are okay, but maybe you shoud rethink before to date?")
    print(f"Your score is {score}%")
elif score < 80:
    print("Congrats you guys will be a great couple!")
    print(f"Your score is {score}%")
elif score < 100:
    print("Wow you guys are more than couples!!")
    print(f"Your score is {score}%")
else:
    print("Ups something went wrond re-run program again!")
