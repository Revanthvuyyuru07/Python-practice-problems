def is_palindrome(s):
    return s == s[::-1]

def main():
    string = input("Enter a string: ").strip()
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
