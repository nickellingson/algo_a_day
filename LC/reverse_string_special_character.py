def reverse_str(s):
    res_string = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] >= 'a' and s[i] <= 'z' or s[i] >= "A" and s[i] <= "Z":
            res_string += (s[i])
        else:
            res_string += (s[len(s) - i - 1])
    
    return res_string


s = "a,b$cHOUF?RE"
print(reverse_str(s))