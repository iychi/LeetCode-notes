# not converting to string: time: O(log(n))  space:O(1)
def isPalindrome(x: int) -> bool:
    # false: negative number
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    # if only 1 digit
    if x // 10 == 0: 
        return True
    # reverse last half
    last_half = 0
    while x > last_half:
        last_digit = x % 10
        last_half = last_half * 10 + last_digit
        x //= 10
    # checking last half == first half  considering even-length & odd-length
    return x == last_half or x == last_half // 10


x1 = 121 # True
x2 = -121 # False
x3 = 10 # False

print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))