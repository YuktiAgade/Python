# Lab Assignment-2: Capitalize Lines Function

def capitalize_lines(lines):
    """
    Function that accepts a sequence of lines and returns them with 
    all characters capitalized
    """
    capitalized = []
    for line in lines:
        capitalized.append(line.upper())
    return capitalized

def get_lines_from_user():
    """Function to get multiple lines from user input"""
    print("Enter your lines (press Enter twice to finish):")
    lines = []
    
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        if line == "" and not lines:
            continue
        lines.append(line)
    
    # Remove the last empty line if it exists
    if lines and lines[-1] == "":
        lines.pop()
    
    return lines

def main():
    """Main function to demonstrate the capitalize_lines function"""
    
    print("="*50)
    print("LINE CAPITALIZER PROGRAM")
    print("="*50)
    
    # Method 1: Direct input from user
    print("\nMethod 1: Enter lines interactively")
    lines = get_lines_from_user()
    
    if lines:
        # Process the lines
        capitalized_lines = capitalize_lines(lines)
        
        # Display results
        print("\n" + "="*50)
        print("RESULTS")
        print("="*50)
        print("\nOriginal Lines:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line}")
        
        print("\nCapitalized Lines:")
        for i, line in enumerate(capitalized_lines, 1):
            print(f"{i}. {line}")
    else:
        print("No lines entered.")
    
    # Method 2: Using the sample input from the assignment
    print("\n" + "="*50)
    print("METHOD 2: Using sample input")
    print("="*50)
    
    sample_lines = [
        "Practice makes perfect",
        "Python programming is fun",
        "Hello World"
    ]
    
    print("\nSample Input:")
    for line in sample_lines:
        print(line)
    
    print("\nSample Output:")
    for line in capitalize_lines(sample_lines):
        print(line)

# Alternative implementation with file handling capability
def capitalize_lines_from_file(filename):
    """Function to read lines from a file and capitalize them"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        capitalized = [line.upper() for line in lines]
        
        # Write back to file (optional)
        with open('capitalized_' + filename, 'w') as file:
            file.writelines(capitalized)
        
        return capitalized
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Enhanced version with more features
def enhanced_capitalize_lines(lines, preserve_indentation=True):
    """
    Enhanced version that can handle different capitalization options
    
    Parameters:
    - lines: list of input lines
    - preserve_indentation: if True, keeps original indentation
    """
    result = []
    for line in lines:
        if preserve_indentation:
            # Split into indentation and content
            stripped = line.lstrip()
            indentation = line[:len(line) - len(stripped)]
            result.append(indentation + stripped.upper())
        else:
            result.append(line.upper())
    return result

# Demonstration of enhanced version
def demonstrate_enhanced_version():
    print("\n" + "="*50)
    print("ENHANCED VERSION (with indentation preservation)")
    print("="*50)
    
    test_lines = [
        "    indented line",
        "  another indented line",
        "normal line",
        "\t tabbed line"
    ]
    
    print("\nOriginal lines with indentation:")
    for line in test_lines:
        print(repr(line))
    
    print("\nCapitalized with preserved indentation:")
    for line in enhanced_capitalize_lines(test_lines):
        print(repr(line))

# Run the main program
if __name__ == "__main__":
    main()
    
    # Uncomment to see enhanced version
    # demonstrate_enhanced_version()
