import os

def list_directory_contents(directory_path):
    try:
        # Check if the provided path is indeed a directory
        if not os.path.isdir(directory_path):
            print(f"Error: The path '{directory_path}' is not a directory.")
            return
        
        # Use os.scandir() to iterate over directory entries
        with os.scandir(directory_path) as entries:
            print(f"Contents of directory '{directory_path}':")
            for entry in entries:
                # Print the name of each entry and whether it's a file or a directory
                entry_type = 'Directory' if entry.is_dir() else 'File'
                print(f"{entry.name} ({entry_type})")
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
directory_path = '/'
list_directory_contents(directory_path)
