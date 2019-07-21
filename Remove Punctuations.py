
punctuations = "!@#$%^&*()_+/.<>'"
my_str = input("Enter a string: ")
nopun = ""
for char in my_str:
   if char not in punctuations:
       nopun = nopun + char


print(nopun)
