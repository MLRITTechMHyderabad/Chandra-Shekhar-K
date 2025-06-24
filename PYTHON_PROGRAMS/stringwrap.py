def wrap_text(S, W):
    result = ''
    for i in range(0, len(S), W):
        result += S[i:i+W] + '\n'
    return result.strip()
    
S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
W = 4

result = wrap_text(S, W)
print(result)