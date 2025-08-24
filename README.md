# Pwned Passwords Checker

Securely check your passwords against known data breaches using the Have I Been Pwned API.

## Description

This project provides a Python script to help users determine if their passwords have been compromised in past data breaches. It integrates with the **Have I Been Pwned API** (`pwnedpasswords.com/range/`) while maintaining user privacy. The script hashes the provided passwords locally using **SHA-1** and sends only the first five characters of the hash to the API. It then compares the remaining hash "tail" against the API's response to identify any matches and reports the number of times the password has been found in leaked databases.
## Getting Started

### Dependencies

* **Python 3.x**
* **`requests` library**: For making HTTP requests to the Have I Been Pwned API.
* **`hashlib` (built-in)**: For generating SHA-1 hashes of passwords.
* **`sys` (built-in)**: For handling command-line arguments.

### Installing

1. **Save the code** to a `.py` file (e.g., `password_checker.py`).
2. **Install the `requests` library** using pip: ```pip install requests```

### Executing program

Run this program directly from your terminal or command prompt (CLI). The script takes one or more passwords as command-line arguments.

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved the file using the cd command.
3. Execute the script by typing python followed by the script name and then each password you wish to check, separated by spaces.

```
python main.py <password1> <password2> [<password3> ...]
```

### Example
```
python main.py mysecretpass MySecureP@ssw0rd!
```

## Help

* **"Error fetching: 400" or similar HTTP errors:** This usually indicates a problem with the API call. Double-check your internet connection. For this specific API, a 400 error might suggest an incorrectly formatted hash prefix, though the script handles this automatically for SHA-1.
* **No output for `sys.argv`:** If you run the script and don't get any password check results, ensure you are actually providing passwords as arguments after `python main.py`.

---
## Authors

Simon Valenzuela  
[GitHub](https://github.com/CaptSV)  
[LinkedIn](https://www.linkedin.com/in/simonrpvalenzuela/)

---
## Version History

* 0.1
    * Initial Release: Command-line argument-based password checking with the Have I Been Pwned API. This comprehensive initial version includes:
      * Secure SHA-1 hashing of passwords.
      * Querying the Have I Been Pwned API's range endpoint.
      * Retrieving and reporting leak counts.
      * Handling multiple password inputs via sys.argv.
      * Robust error handling for API fetching issues.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit)  - see the LICENSE.md file for details

## Acknowledgments

* This project was developed as part of the [ZTM - Complete Python Developer course](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/).
* [Have I Been Pwned API](https://www.google.com/search?q=https://haveibeenpwned.com/API/v3%23PasswordRanges) for providing the data.
* [requests](https://pypi.org/project/requests/) library for simplifying HTTP requests.
* [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hashing algorithm for password security.