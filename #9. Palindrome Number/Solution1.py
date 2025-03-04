# convert x to string: time: O(n)  space:O(n)

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


x1 = 121 # True
x2 = -121 # False
x3 = 10 # False

print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
