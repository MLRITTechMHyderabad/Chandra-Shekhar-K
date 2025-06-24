total_heads = 35
total_legs = 94
for r in range(total_heads + 1):
    c = total_heads - r
    legs = 2 * c + 4 * r
    if legs == total_legs:
        print("Chickens:",c)
        print("Rabbits:",r)
        break