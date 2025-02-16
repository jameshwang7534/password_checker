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
Ensure you have Python installed on your system. The program uses Tkinter, which is included with most standard Python installations.

### Steps to Run
1. Save the provided Python script as `password_checker.py`.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script using:
   ```sh
   python password_checker.py
   ```
4. Enter a password in the GUI and click "Check Password".
5. If the password meets all criteria, it will be saved in `your_password.txt` and the application will close.

## Limitations & Warnings
- **Educational Use Only**: This tool is designed for learning purposes and should not be used as a robust security measure for protecting sensitive accounts or information.
- **Not a Secure Storage Solution**: Storing passwords in a plain text file (`your_password.txt`) is **insecure**. For real-world applications, consider using password managers or secure encryption techniques.
- **No Advanced Security Checks**: The tool does not check for common passwords, dictionary words, or entropy-based security vulnerabilities.

## Ethical Considerations & Responsible Use
- **False Sense of Security**: This tool only checks for basic strength criteria and does not guarantee absolute security. Users should be aware that other factors, such as password reuse and phishing attacks, affect password security.
- **Potential for Misuse**: Modifying this script to log passwords secretly would be unethical and a violation of privacy. Users should ensure they do not distribute modified versions with malicious intent.
- **Encouraging Safe Practices**: Users should always follow security best practices, such as using unique passwords for different accounts and enabling multi-factor authentication where possible.

## Future Improvements
- Implement hashing instead of storing passwords in plain text.
- Add more robust security checks, such as preventing common or easily guessed passwords.
- Provide user feedback on how to improve weak passwords.


