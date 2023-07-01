# Displays each word of the sentence on a separate line.

# created a input function for user to input a sentance 
sentance = input("Create a simple sentance: \n")

# created a variable and added the .split string method  
new = sentance.split()

# used a loop to print out each word on a sperate line 
for i in new: 
    print(i)
