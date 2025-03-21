# Count the number of moves
moves = 0

def tower_of_hanoi(n, source, target, auxiliary):
    global moves
    if n == 1:
        print(f"Move disk {n} from {source} to {target}")
        moves += 1
    else:
        # Step 1: Move smaller disks to the auxiliary rod
        tower_of_hanoi(n - 1, source, auxiliary, target)
        # Step 2: Move the largest disk to the target rod
        print(f"Move disk {n} from {source} to {target}")
        moves += 1
        # Step 3: Move the smaller disks to the target rod
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Get the number of disks from the user
num_disks = int(input("Enter the number of disks: "))
tower_of_hanoi(num_disks, "A", "B", "C")
print(f"Total moves: {moves}")
