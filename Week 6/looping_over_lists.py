list_of_chores = ["Take Out Trash", "Wash Dishes", "Cut Grass", "Dust Coffee Table"]

for chore in list_of_chores:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

#chore can be named anything

print("All chores are done!")

for chore in list_of_chores[0:2]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

#the 0 is optional but recommended, :2 also works

for chore in list_of_chores[1:2]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

for chore in list_of_chores[1:3]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")
