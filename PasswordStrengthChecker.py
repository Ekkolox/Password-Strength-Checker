import string

def check_password_strength(password, min_length=8, special_chars=string.punctuation):
   # Checks the strength of a password based on multiple criteria. Returns the strength rating and missing criteria for improvement   
    # Criteria of passwords definiton
    special_char_set = set(special_chars)
    length_ok = len(password) >= min_length
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_char_set for char in password)

    # Highlights missing criteria
    missing_criteria = []
    if not length_ok:
        missing_criteria.append(f"at least {min_length} characters")
    if not has_upper:
        missing_criteria.append("an uppercase letter")
    if not has_lower:
        missing_criteria.append("a lowercase letter")
    if not has_digit:
        missing_criteria.append("a digit")
    if not has_special:
        missing_criteria.append(f"a special character ({special_chars})")

    # Determine the strength
    conditions_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    if conditions_met <= 2:
        strength = "Weak"
    elif 3 <= conditions_met < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, missing_criteria

def main():
    print("Welcome to my  Password Strength Checker!")
    print("To create a strong password,your password must include the following:")
    print("  - At least 8 characters")
    print("  - A mix of Uppercase and lowercase letters")
    print("  - Numbers and special characters")
    print()

    user_password = input("Enter a potential password: ")
    strength, feedback = check_password_strength(user_password)

    print(f"\nYour password is rated as: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"  - Add {suggestion}")
    else:
        print("Great job! Your password is strong.")

if __name__ == "__main__":
    main()
