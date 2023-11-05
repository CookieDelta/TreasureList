#      A    B     C
# 1 ["⬜️","️⬜️","️⬜️"]
# 1 ["⬜️","⬜️","️⬜️"]
# 1 ["⬜️","⬜️","⬜️️"]

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️","⬜️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print(line1)
print(line2)
print(line3)
position = input("Where do you want to put the treasure?\n") #
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

l=list(position)

if l[0].lower() == "a":
    col = "0"
elif l[0].lower() == "b":
    col = "1"
elif l[0].lower == "c":
    col = "2"

if l[1] == "1":
    row = "0"
elif l[1] == "2":
    row = "1"
elif l[1] == "3":
    row = "2"

map[int(row)][int(col)] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
