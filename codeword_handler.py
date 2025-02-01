# codeword_handler.py
# A spy-themed program that uses a dictionary to map codewords to specific functions.

# Function to handle the 'infiltrate' codeword
def handle_infiltrate(location):
    """
    Handles the codeword 'infiltrate'.

    Args:
    location (str): The location to infiltrate.

    Returns:
    str: A message confirming the infiltration mission.
    """
    return f"Mission: Infiltrate {location}. Proceed with caution!"

# Function to handle the 'extract' codeword
def handle_extract(target):
    """
    Handles the codeword 'extract'.

    Args:
    target (str): The target to extract.

    Returns:
    str: A message confirming the extraction mission.
    """
    return f"Mission: Extract {target}. Ensure no witnesses!"

# Function to handle the 'decrypt' codeword
def handle_decrypt(code):
    """
    Handles the codeword 'decrypt'.

    Args:
    code (str): The code to decrypt.

    Returns:
    str: A message revealing the decrypted information.
    """
    return f"Decrypted Message: '{code}' translates to 'The package is in the vault.'"

# Function to handle the 'evade' codeword
def handle_evade(direction):
    """
    Handles the codeword 'evade'.

    Args:
    direction (str): The direction to evade.

    Returns:
    str: A message confirming the evasion plan.
    """
    return f"Evasion Plan: Move {direction} to avoid detection."

# Dictionary that maps spy codewords to the functions
codewords = {
    "infiltrate": handle_infiltrate,  # Maps 'infiltrate' to the handle_infiltrate function
    "extract": handle_extract,        # Maps 'extract' to the handle_extract function
    "decrypt": handle_decrypt,        # Maps 'decrypt' to the handle_decrypt function
    "evade": handle_evade,            # Maps 'evade' to the handle_evade function
}

# Main program
def main():
    # Display welcome message and available codewords
    print("Welcome to Spy Agency HQ.")
    print("Available codewords:", ", ".join(codewords.keys()))

    # Get user input
    codeword = input("Enter a codeword: ").strip().lower()

    # Check if the codeword exists in the dictionary
    if codeword in codewords:
        # Call the corresponding function with an argument
        argument = input(f"Enter the argument for '{codeword}': ").strip()
        result = codewords[codeword](argument)
        print(result)
    else:
        # Handle unknown codewords
        print("Codeword not recognized. Mission aborted.")

# Run the program
if __name__ == "__main__":
    main()
