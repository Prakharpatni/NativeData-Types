my_str = "ABCDEFFEDCBA"
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
