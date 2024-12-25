choice_number = 2

match choice_number:
    case 1:
        print("You choose One.")
    case 2:
        print("You choose Two.")
    case _:
        print("You didn't choose One or Two.")

point = (1, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Point on X-axis at {x}")
    case (0, y):
        print(f"Point on Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

numbers = [1, 4, 3]

match numbers:
    case [1, 2, 3]:
        print("Exact match!")
    case [1, *rest]:
        print(f"Starts with 1 and the rest are {rest}")
    case _:
        print("No match")

command = "resume"

match command:
    case "start" | "resume":
        print("Starting or Resuming...")
    case "stop" | "pause":
        print("Stopping or Pausing...")
    case _:
        print("Unknown command.")

value = 42

match value:
    case x if x > 0:
        print(f"Positive number: {x}")
    case x if x < 0:
        print(f"Negative number: {x}")
    case 0:
        print("Zero")
