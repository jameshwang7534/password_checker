# Password Strength Checker

## Description
This Python program provides a simple password strength checker using a graphical user interface (GUI) built with Tkinter. The program evaluates a user's password based on the following criteria:
- Minimum length of 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one numeric digit
- At least one special character

If the password meets all these requirements, it is deemed "Strong" and will be saved to a file named `your_password.txt`.

## How to Run
### Prerequisites
Make sure you have Python installed on your system. The program uses Tkinter, which is included with most standard Python installations.

### Steps to Run
1. Save the provided Python script as `password_checker.py`.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script using:
   ```sh
   python password_checker.py
   ```
4. Enter a password in the GUI and click "Check Password".
5. The program will tell you if your password is secure!

## Limitations & Warnings
- **No Advanced Security Checks**: The tool does not check for common passwords, dictionary words, or entropy-based security vulnerabilities.

## Ethical Considerations & Responsible Use
- **False Sense of Security**: This tool only checks for basic strength criteria and does not guarantee absolute security. Users should be aware of other factors, such modifying the project for distributing harm.
- **Potential for Misuse**: Modifying this script to log passwords secretly would be unethical. Users should ensure they do not distribute modified versions with malicious intent.
- **Encouraging Safe Practices**: Users should always follow security best practices, such as using unique passwords for different accounts and enabling multi-factor authentication where possible.



