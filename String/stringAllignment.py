first_name = "Pulastya"

print(first_name.ljust(10))               # Output: "Pulastya  "
print(first_name.rjust(10))               # Output: "  Pulastya"
print(first_name.center(10))              # Output: " Pulastya "
print(first_name.ljust(10, "*"))               # Output: "Pulastya**"
print(first_name.rjust(10, "*"))               # Output: "**Pulastya"
print(first_name.center(10, "*"))              # Output: "*Pulastya*"

print(f"{first_name:<10}")               # Output: "Pulastya  "
print(f"{first_name:>10}")               # Output: "  Pulastya"
print(f"{first_name:^10}")               # Output: " Pulastya "
print(f"{first_name:*<10}")              # Output: "Pulastya**"
print(f"{first_name:*>10}")              # Output: "**Pulastya"
print(f"{first_name:*^10}")              # Output: "*Pulastya*"

print("{:<10}".format(first_name))               # Output: "Pulastya  "
print("{:>10}".format(first_name))               # Output: "  Pulastya"
print("{:^10}".format(first_name))               # Output: " Pulastya "
print("{:*<10}".format(first_name))              # Output: "Pulastya**"
print("{:*>10}".format(first_name))              # Output: "**Pulastya"
print("{:*^10}".format(first_name))              # Output: "*Pulastya*"

