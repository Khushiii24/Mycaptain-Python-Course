def most_frequent(string):
    char_frequency = {}

    # Count the frequency of each character
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Sort the characters based on frequency in descending order
    sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the characters and their frequencies
    for char, freq in sorted_chars:
        print(char, '=', freq)

# Prompt the user to enter a string
input_string = input("Please enter a string: ")

# Call the most_frequent function with the input string
most_frequent(input_string)
