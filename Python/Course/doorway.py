# program to determine if a box can fit through a door, given both dimensions

# box dimensions
A = int(input())
B = int(input())
C = int(input())

# door dimensions
X = int(input())
Y = int(input())

# check if box can fit through door
if A <= X and B <= Y and C <= Y and C <= X:
    print("The box can be carried")
else:
    print("The box cannot be carried")
    