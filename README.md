# Password Manager
This project is a simple **Password Manager** application developed in Python using the `tkinter` library. It allows users to securely store website credentials, generate strong passwords, and save them in a local file.

### Features

- **Password Generation**: 
  - Creates random, strong passwords containing a mix of letters, numbers, and symbols.
  - Automatically copies the generated password to the clipboard for convenience.

- **Save Credentials**:
  - Stores website name, email/username, and password in a local text file (`PasswordManager.txt`).
  - Displays a confirmation dialog before saving.

- **User Interface**:
  - Built with the `tkinter` library, offering a clean and intuitive GUI.

### How to Use

1. Enter the website name, email/username, and password (or generate a new one using the **Generate Password** button).
2. Click the **Add** button to save the credentials.
3. Saved credentials are appended to a text file (`PasswordManager.txt`), which opens automatically after each save.

### Technologies Used

- **Python**: Programming language.
- **tkinter**: GUI framework for Python.
- **pyperclip**: Library to copy text to the clipboard.
- **os**: For opening the saved file automatically.

***Note:** This application is a simple project for educational purposes and does not provide encryption for stored passwords.*

## Update - 01.24.2025

The project has received a major update, introducing JSON file handling and advanced exception management techniques, such as `try`, `except`, `else`, and `finally`. The new features include:

- **Data Verification:**  
  When entering a website name and click on the `search` button, the program checks if it is already registered in the JSON file.  
  - If the website is found, a pop-up will display the site name, email/username, and the previously saved password.  
  - If the website is not found, a warning message will notify you that no data was found in the database.

- **JSON File Creation:**  
  If the JSON file does not exist on the system, it will be automatically created with the name *PasswordManager.json*.

- **Automatic Opening:**  
  After saving the information, the JSON file will automatically open in your preferred editor for review or editing.

The updated code is available in the repository under the name: `main_upgraded.py`.

<img align="center" height="448" width="501" src="https://github.com/user-attachments/assets/9048c05b-c981-4cd6-ac0f-19d1e0385267"/>

---

## Images (Old Version)
<div style="display: inline_block"><br>
  <img align="center" height="324" width="377" src="https://github.com/user-attachments/assets/cce00725-e303-4111-b921-e5423fe944e0"/>
  <img align="center" height="333" width="439" src="https://github.com/user-attachments/assets/ae7a1dcb-8a2a-4804-bb04-a14bea6ca531"/>
  <img align="center" height="531" width="769" src="https://github.com/user-attachments/assets/0ed03e57-f947-4086-80f9-2523e163f30f"/>
  <img align="center" height="325" width="377" src="https://github.com/user-attachments/assets/d2a86330-ea35-454d-ba1f-31e9870e002b"/>
  <img align="center" height="526" width="790" src="https://github.com/user-attachments/assets/07fbd20c-13fc-47ca-b624-66f3068b234a"/>
  <img align="center" height="331" width="389" src="https://github.com/user-attachments/assets/da175116-45ac-4955-b0b0-53e1c80a3c70"/>
</div>
