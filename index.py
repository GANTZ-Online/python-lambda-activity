# List of tuples to be sorted
unsorted_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list using the sorted() function
# lambda function is used to specify that we want to sort by the second element of each tuple
sorted_list = sorted(unsorted_list, key=lambda x: x[1])

# Print the sorted list to see the result
print(sorted_list)  # Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# Define a lambda function that takes a list and cubes each element using list comprehension
cubed = lambda x: [i**3 for i in x]

# Apply the lambda function to the list [3, 6, 9, 2] and print the result
print(cubed([3, 6, 9, 2]))  # Output: [27, 216, 729, 8]

# Problem 3: Determine Whether a Number is Even or Odd
# Define a lambda function that checks if a number is even
# The function returns True if the number is even (x % 2 == 0) and False otherwise
even_odd = lambda x: True if x % 2 == 0 else False

# Use a list comprehension to apply the lambda function to each element in the list [3, 6, 9, 2]
# The list comprehension creates a new list of booleans based on whether each number is even or odd
even_odd_list = [even_odd(x) for x in [3, 6, 9, 2]]

# Print the result for Problem 3
print("Problem 3 - Even or Odd List:", even_odd_list)

# Problem 4: Create a List of Numbers from 1 to 100
# Use a list comprehension to create a list of numbers from 1 to 100 (inclusive)
# range(1, 101) generates numbers from 1 to 100
nums = [i for i in range(1, 101)]

# Print the result for Problem 4
print("Problem 4 - Numbers from 1 to 100:", nums)

# Problem 5: Count the Length of Each Word in a Sentence
# Define the sentence to process
sent = "The quick brown fox jumped over the fence."

# Use a dictionary comprehension to create a dictionary where each key is a word and the value is the length of that word
# sent.split() splits the sentence into a list of words based on whitespace
# {word: len(word) for word in sent.split()} creates a dictionary from the words and their lengths
word_lengths = {word: len(word) for word in sent.split()}

# Print the result for Problem 5
print("Problem 5 - Word Lengths:", word_lengths)
