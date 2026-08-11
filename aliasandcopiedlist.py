value_count = int(input())
original_list = []

# Read and store all values using append()
for i in range(value_count):
    original_list.append(int(input()))

# Create an alias and a shallow copy
alias = original_list
copied_list = original_list.copy()

alias_position = int(input()) - 1
alias_value = int(input())
copy_position = int(input()) - 1
copy_value = int(input())

# Update one value through the alias
alias[alias_position] = alias_value

# Update one value in the copied list
copied_list[copy_position] = copy_value
print("Original List:", original_list)
print("Alias List:", alias)
print("Copied List:", copied_list)

if alias is original_list:
    print("Alias Shares Original: Yes")
else:
    print("Alias Shares Original: No")

# Compare both lists position by position
different_positions = 0
for i in range(value_count):
    if original_list[i] != copied_list[i]:
        different_positions += 1

# Display all results
print("Different Positions:", different_positions)
