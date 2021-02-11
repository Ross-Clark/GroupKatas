def valid_anagram(s, t):
    return "".join(sorted(s)) == "".join(sorted(t))
