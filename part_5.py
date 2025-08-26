x = 25 // 2
y = x
x = 25 / 2
print(y)

# Swapping two variables (incorrect)
# step 1 = Initialize two variables
a = 7.5  # float
b = -12  # integer

# step 2 = Swap the variables
a = b
b = a

print(a)

# Swapping two variables (correct)
# Step 1 = Initialize two variables
c = 7.5  # float
d = -12  # integer

# Step 2 = Swap them using a temporary variable
temp = c
c = d
d = temp

print(temp)

# Swap them without using a temporary variable
c, d = d, c

print(c)
