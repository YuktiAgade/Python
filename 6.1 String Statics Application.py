# Lab Assignment-1: String Statistics Application

def get_string_statistics(text):
    """Function to calculate various string statistics"""
    
    # Initialize counters
    vowels = 0
    consonants = 0
    spaces = 0
    lowercase = 0
    
    # Define vowels set
    vowel_set = set('aeiouAEIOU')
    
    # Analyze each character in the string
    for char in text:
        # Count vowels
        if char in vowel_set:
            vowels += 1
        
        # Count consonants (letters that are not vowels)
        elif char.isalpha() and char not in vowel_set:
            consonants += 1
        
        # Count spaces
        elif char.isspace():
            spaces += 1
        
        # Count lowercase letters
        if char.islower():
            lowercase += 1
    
    return vowels, consonants, spaces, lowercase

def display_statistics(text):
    """Function to display statistics in formatted way"""
    
    print("\n" + "="*50)
    print("STRING STATISTICS")
    print("="*50)
    print(f"Original string: \"{text}\"")
    print("-"*50)
    
    # Get statistics
    vowels, consonants, spaces, lowercase = get_string_statistics(text)
    
    # Display results
    print(f"a) Number of Vowels: {vowels}")
    print(f"b) Number of Consonants: {consonants}")
    print(f"c) Number of Spaces: {spaces}")
    print(f"d) Number of Lowercase Letters: {lowercase}")
    
    # Additional statistics
    print("-"*50)
    print("Additional Information:")
    print(f"   Total characters: {len(text)}")
    print(f"   Uppercase letters: {sum(1 for c in text if c.isupper())}")
    print(f"   Digits: {sum(1 for c in text if c.isdigit())}")
    print(f"   Special characters: {sum(1 for c in text if not c.isalnum() and not c.isspace())}")

# Main program
print("STRING STATISTICS APPLICATION")
print("="*50)

# Get input from user
user_string = input("Enter a string: ")

if user_string:  # Check if string is not empty
    display_statistics(user_string)
else:
    print("Empty string entered. Please try again.")
