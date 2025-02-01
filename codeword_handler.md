# Spy-Themed Codeword Handler  
**Author:** Gower Campbell  

This document explains the `codeword_handler.py` program, a **spy-themed** application that uses **user-defined functions** and **dictionaries** to map codewords to specific actions. The program simulates a spy agency interface where users enter codewords to unlock secret missions or access hidden information.

---

## Table of Contents  
1. [Introduction](#introduction)  
2. [Code Overview](#code-overview)  
   - [Function Definitions](#function-definitions)  
   - [Dictionary Mapping](#dictionary-mapping)  
   - [Main Program Logic](#main-program-logic)  
3. [How It Works](#how-it-works)  
4. [Key Features](#key-features)  
5. [Future Improvements](#future-improvements)  

---

## 1. Introduction  
The `codeword_handler.py` program demonstrates how **user-defined functions** and **dictionaries** can work together to create dynamic and interactive code. By entering spy-themed codewords like "infiltrate," "extract," or "decrypt," users can trigger specific functions that simulate spy missions. This program is a fun and engaging way to explore Python's capabilities.

---

## 2. Code Overview  

### Function Definitions  
The program defines four functions to handle spy-related codewords:  

#### `handle_infiltrate(location)`  
```python
def handle_infiltrate(location):
    """
    Handles the codeword 'infiltrate'.

    Args:
    location (str): The location to infiltrate.

    Returns:
    str: A message confirming the infiltration mission.
    """
    return f"Mission: Infiltrate {location}. Proceed with caution!"
```  
- **Purpose**: Simulates an infiltration mission.  
- **Example**: `handle_infiltrate("enemy base")` returns `"Mission: Infiltrate enemy base. Proceed with caution!"`.  

#### `handle_extract(target)`  
```python
def handle_extract(target):
    """
    Handles the codeword 'extract'.

    Args:
    target (str): The target to extract.

    Returns:
    str: A message confirming the extraction mission.
    """
    return f"Mission: Extract {target}. Ensure no witnesses!"
```  
- **Purpose**: Simulates an extraction mission.  
- **Example**: `handle_extract("VIP")` returns `"Mission: Extract VIP. Ensure no witnesses!"`.  

#### `handle_decrypt(code)`  
```python
def handle_decrypt(code):
    """
    Handles the codeword 'decrypt'.

    Args:
    code (str): The code to decrypt.

    Returns:
    str: A message revealing the decrypted information.
    """
    return f"Decrypted Message: '{code}' translates to 'The package is in the vault.'"
```  
- **Purpose**: Simulates a decryption mission.  
- **Example**: `handle_decrypt("X7G9")` returns `"Decrypted Message: 'X7G9' translates to 'The package is in the vault.'"`.  

#### `handle_evade(direction)`  
```python
def handle_evade(direction):
    """
    Handles the codeword 'evade'.

    Args:
    direction (str): The direction to evade.

    Returns:
    str: A message confirming the evasion plan.
    """
    return f"Evasion Plan: Move {direction} to avoid detection."
```  
- **Purpose**: Simulates an evasion plan.  
- **Example**: `handle_evade("north")` returns `"Evasion Plan: Move north to avoid detection."`.  

---

### Dictionary Mapping  
The `codewords` dictionary maps spy-related codewords to their corresponding functions:  
```python
codewords = {
    "infiltrate": handle_infiltrate,  # Maps 'infiltrate' to the handle_infiltrate function
    "extract": handle_extract,        # Maps 'extract' to the handle_extract function
    "decrypt": handle_decrypt,        # Maps 'decrypt' to the handle_decrypt function
    "evade": handle_evade,            # Maps 'evade' to the handle_evade function
}
```  
- **Purpose**: Allows dynamic calling of functions based on user input.  
- **Flexibility**: New codewords and handlers can be added easily by updating the dictionary.  

---

### Main Program Logic  
The `main()` function handles the program’s logic:  
1. Displays a welcome message and available codewords.  
2. Prompts the user to enter a codeword.  
3. Checks if the codeword exists in the `codewords` dictionary.  
4. If the codeword exists, prompts the user for an argument and calls the corresponding function.  
5. If the codeword doesn’t exist, displays an error message and aborts the mission.  

---

## 3. How It Works  
1. The program starts by displaying available codewords: `infiltrate`, `extract`, `decrypt`, and `evade`.  
2. The user enters a codeword (e.g., `infiltrate`).  
3. If the codeword is valid, the program prompts the user for an argument (e.g., `enemy base`).  
4. The corresponding function is called with the argument, and the result is displayed.  
5. If the codeword is invalid, the program displays an error message.  

---

## 4. Key Features  
1. **Dynamic Function Calls**: The program uses a dictionary to call functions dynamically based on user input.  
2. **Modular Design**: Each codeword has its own handler function, making the code easy to extend and maintain.  
3. **Immersive Theme**: The spy theme makes the program engaging and fun to use.  
4. **User-Friendly**: Clear prompts and error handling ensure a smooth user experience.  

---

## 5. Future Improvements  
1. **Add More Codewords**: Extend the dictionary to include more spy-related codewords and handlers.  
2. **Input Validation**: Ensure the user enters valid codewords and arguments.  
3. **Error Handling**: Add more robust error handling for unexpected inputs.  
4. **Graphical Interface**: Create a GUI using libraries like `tkinter` for a more interactive experience.  
5. **Scoring System**: Add a scoring system to track successful missions.  

---

## Example Output  

```
Welcome to Spy Agency HQ.
Available codewords: infiltrate, extract, decrypt, evade
Enter a codeword: infiltrate
Enter the argument for 'infiltrate': enemy base
Mission: Infiltrate enemy base. Proceed with caution!

Welcome to Spy Agency HQ.
Available codewords: infiltrate, extract, decrypt, evade
Enter a codeword: decrypt
Enter the argument for 'decrypt': X7G9
Decrypted Message: 'X7G9' translates to 'The package is in the vault.'

Welcome to Spy Agency HQ.
Available codewords: infiltrate, extract, decrypt, evade
Enter a codeword: retreat
Codeword not recognized. Mission aborted.
```
