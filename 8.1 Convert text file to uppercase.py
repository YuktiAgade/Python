# Program to read a text file and write its contents in uppercase to a new file

def convert_to_uppercase():
    # Get input and output file names from user
    input_file = input("Enter the source file name: ")
    output_file = input("Enter the destination file name: ")
    
    try:
        # Read the content from source file
        with open(input_file, 'r') as source:
            content = source.read()
        
        # Convert content to uppercase
        uppercase_content = content.upper()
        
        # Write uppercase content to destination file
        with open(output_file, 'w') as destination:
            destination.write(uppercase_content)
        
        print(f"File converted successfully! Content written to {output_file}")
        
        # Optional: Display the converted content
        print("\nConverted content:")
        print(uppercase_content)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the function
if __name__ == "__main__":
    convert_to_uppercase()
