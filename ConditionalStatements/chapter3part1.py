command = input("Enter your command: ")

match command:
    case "start" | "resume":
        print("Starting or Resuming...")
    case "stop" | "pause":
        print("Stopping or Pausing...")
    case _:
        print("Unknown command.")