# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’

def removevowels(x):
    for i in range(len(x)):
        vowels = 'aeiouAEIOU'
        return (x(i) if x not in vowels)

removevowels('Hello my name is Ian')