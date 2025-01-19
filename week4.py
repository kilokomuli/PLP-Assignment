def modify_content(content):
    """
    Function to modify content. 
    Here, we'll convert it to uppercase as an example modification.
    """
    return content.upper()


def main():
    import os

    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the input filename: ").strip()
        
        # Check if the file exists and is readable
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Prompt the user for the output filename
        output_filename = input("Enter the output filename: ").strip()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' was successfully modified and saved as '{output_filename}'.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
