def print_alpha_diamond(n):
    for i in range(n - 1):
        line = ''
        # Leading dashes
        line += ' ' * (2 * (n - i - 1))
        
        # Left side letters
        for j in range(i, -1, -1):
            line += chr(ord('a') + n - 1 - j)
            if j != 0:
                line += ' '
        
        # Right side letters
        for j in range(1, i + 1):
            line += ' ' + chr(ord('a') + n - 1 - j)

        # Trailing dashes
        line += ' ' * (2 * (n - i - 1))
        print(line)

    # Middle line
    line = ''
    for j in range(n - 1, -1, -1):
        line += chr(ord('a') + j)
        if j != 0:
            line += ' '
    for j in range(1, n):
        line += ' ' + chr(ord('a') + j)
    print(line)

    # Lower half (mirror of upper half)
    for i in range(n - 2, -1, -1):
        line = ''
        line += ' ' * (2 * (n - i - 1))
        for j in range(i, -1, -1):
            line += chr(ord('a') + n - 1 - j)
            if j != 0:
                line += ' '
        for j in range(1, i + 1):
            line += ' ' + chr(ord('a') + n - 1 - j)
        line += ' ' * (2 * (n - i - 1))
        print(line)
        
        

print_alpha_diamond(7)
