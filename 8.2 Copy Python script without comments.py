# Application to copy Python script content without comments

def remove_comments_from_file():
    # Ask user for source and destination file names
    source_file = input("Enter the source Python file name: ")
    destination_file = input("Enter the destination file name: ")
    
    try:
        # Read source file content
        with open(source_file, 'r') as source:
            source_content = source.readlines()
        
        # Process content to remove comments
        cleaned_content = []
        for line in source_content:
            # Check if line contains a comment
            if '#' in line:
                # Find the position of '#'
                comment_index = line.find('#')
                # Check if '#' is inside a string (simplified approach)
                # This is a basic implementation; a full solution would need string parsing
                if not is_comment_in_string(line, comment_index):
                    # Remove the comment part
                    line = line[:comment_index]
            cleaned_content.append(line)
        
        # Write cleaned content to destination file
        with open(destination_file, 'w') as destination:
            destination.writelines(cleaned_content)
        
        # Print content of both files
        print("\n" + "="*50)
        print(f"CONTENT OF SOURCE FILE ({source_file}):")
        print("="*50)
        print(''.join(source_content))
        
        print("\n" + "="*50)
        print(f"CONTENT OF DESTINATION FILE ({destination_file}):")
        print("="*50)
        print(''.join(cleaned_content))
        
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_comment_in_string(line, comment_pos):
    """Check if # is within a string (simplified approach)"""
    # Count quotes before the comment position
    quote_count = 0
    in_string = False
    string_char = None
    
    for i, char in enumerate(line[:comment_pos]):
        if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):  # Not escaped
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
    
    return in_string

# Alternative simplified version for basic comment removal
def copy_without_comments_simple():
    """Simpler version that removes lines starting with #"""
    source_file = input("Enter the source Python file name: ")
    destination_file = input("Enter the destination file name: ")
    
    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()
        
        # Filter out comment lines and inline comments
        cleaned_lines = []
        for line in lines:
            # Remove full line comments
            if line.strip().startswith('#'):
                continue
            
            # Remove inline comments (basic)
            if '#' in line:
                line = line.split('#', 1)[0] + '\n'
            
            cleaned_lines.append(line)
        
        with open(destination_file, 'w') as dest:
            dest.writelines(cleaned_lines)
        
        # Print both files
        print("\nOriginal file content:")
        print(''.join(lines))
        print("\nFile without comments:")
        print(''.join(cleaned_lines))
        
    except FileNotFoundError:
        print(f"File {source_file} not found!")

# Execute the function
if __name__ == "__main__":
    print("PYTHON SCRIPT COMMENT REMOVER")
    print("-" * 30)
    copy_without_comments_simple()
    # For more advanced comment removal, use remove_comments_from_file()
