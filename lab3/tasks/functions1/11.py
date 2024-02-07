def palindrome(s):
    t = s[::-1]

    if t == s:
        print("yes, this string is palindrome")

    else:
        print("no, it is not palindrome")

palindrome(input("type your word:"))