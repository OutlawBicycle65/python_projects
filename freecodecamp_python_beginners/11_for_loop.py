friends = ["jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

print("\n")

for index in range(3, 10):
    print(index)

print("\n")

for index in range(len(friends)):
    print(friends[index])

print("\n")

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")
