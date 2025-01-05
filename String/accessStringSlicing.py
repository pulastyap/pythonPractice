
name = "Pulastya"
few_char = name[2:6]            # Output: last (substring from index 2 to 5)
from_first = name[:4]           # Output: Pula
till_last = name[4:]            # Output: stya
few = name[1:7:2]               # Output: uat (alternate char from index 1 to 7)
neg_few_char = name[-2:-5:-1]   # Output: yts (using negative index from back to front)
reversed_name = name[-1::-1]    # Output: aytsaluP
reversed_name1 = name[::-1]      # Output: aytsaluP

print(reversed_name)
print(reversed_name1)

string2 = "A man, a plan, a canal: Panama"
reversed2 = string2[::-1]
print(reversed2)  # Output: amaP :lanac a ,nalp a ,nam A

