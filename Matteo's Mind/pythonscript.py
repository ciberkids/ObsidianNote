import os
import sh
import re

def find_and_replace(dry_run=True):
    # Define the directory to search
    directory = '.'
    # Define the file extension to search
    file_extension = '.md'
    # Define the pattern to search for
    search_pattern = r'!\[\[Pasted image ([0-9]*).png\]\]'
    # Define the replacement pattern
    replacement_pattern = r'![](./images/Pasted%20image%20\1.png)'

    # ANSI escape codes for coloring
    RED = '\033[91m'
    RESET = '\033[0m'

    # Find all files with the specified extension
    try:
        files = sh.find(directory, '-type', 'f', '-name', f'*{file_extension}').splitlines()
    except sh.ErrorReturnCode as e:
        print(f"Error finding files: {e}")
        return

    # Process each file
    for file in files:
        try:
            with open(file, 'r') as f:
                content = f.read()

            # Find all matches in the file
            matches = re.findall(search_pattern, content)
            if matches:
                print(f"File: {file}")
                file_dir = os.path.dirname(file)  # Get the directory of the current file
                for match in matches:
                    old_string = f'![[Pasted image {match}.png]]'
                    new_string = f'![](images/Pasted%20image%20{match}.png)'
                    image_path = os.path.join(file_dir, 'images', f'Pasted image {match}.png')
                    
                    # Check if the image file exists
                    if os.path.exists(image_path):
                        print(f"  Replace: {old_string} -> {new_string}")
                        if not dry_run:
                            # Replace the content
                            content = re.sub(re.escape(old_string), new_string, content)
                    else:
                        print(f"{RED}  Image file does not exist: {image_path}{RESET}")

                if not dry_run:
                    # Write the changes back to the file
                    with open(file, 'w') as f:
                        f.write(content)
                    print(f"  Changes applied to {file}")
                else:
                    print(f"  Dry run: No changes applied to {file}")

        except Exception as e:
            print(f"Error processing file {file}: {e}")

if __name__ == "__main__":
    # Set dry_run to False to apply changes
    find_and_replace(dry_run=True)
