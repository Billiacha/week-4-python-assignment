def file_read_write():
    try:
        # Ask user for input file name
        input_file = input("Enter the name of the file to read: ")

        # Try opening the file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask user for output file name
        output_file = input("Enter the name of the new file to write: ")

        # Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"🎉 Successfully created '{output_file}' with modified content!")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read or write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the program
file_read_write()
