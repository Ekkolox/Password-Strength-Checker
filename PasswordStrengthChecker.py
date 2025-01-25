import sys
import string
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox
)
from PyQt6.QtCore import Qt


# Function to check password strength
def check_password_strength(password, min_length=8, special_chars=string.punctuation):
    special_char_set = set(special_chars)
    length_ok = len(password) >= min_length
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_char_set for char in password)

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

    conditions_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    if conditions_met <= 2:
        strength = "Weak"
    elif 3 <= conditions_met < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, missing_criteria


# A function to generate a password using random ASCII characters
def generate_password(min_length=8, special_chars=string.punctuation):
    password = []
    password.append(random.choice(string.ascii_letters))

    # Generate random characters until the password reaches the desired length
    while len(password) < min_length:
        char_type = random.choice(['letter', 'digit', 'special'])
        if char_type == 'letter':
            password.append(random.choice(string.ascii_letters))
        elif char_type == 'digit':
            password.append(random.choice(string.digits))
        else:
            password.append(random.choice(special_chars))

    # Shuffle to mix characters randomly
    random.shuffle(password)

    return ''.join(password)


# Main window class for GUI
class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Strength Checker")
        self.setGeometry(200, 200, 400, 300)

        # Create layout
        layout = QVBoxLayout()

        # Label for instructions
        self.instructions_label = QLabel("Enter your password to check its strength")
        layout.addWidget(self.instructions_label)

        # Password input field
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.textChanged.connect(self.update_password_strength)
        layout.addWidget(self.password_input)

        # Checkbox to toggle password visibility
        self.show_password_checkbox = QCheckBox("Show Password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        layout.addWidget(self.show_password_checkbox)

        # Label for displaying password strength
        self.strength_label = QLabel("Password strength: ")
        layout.addWidget(self.strength_label)

        # Label for color-coded strength indicator
        self.strength_indicator = QLabel("")
        self.strength_indicator.setFixedHeight(10)
        layout.addWidget(self.strength_indicator)

        # Button to generate a strong password
        self.generate_button = QPushButton("Generate Strong Password")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        # Label for displaying suggestions to improve password
        self.suggestions_label = QLabel("")
        layout.addWidget(self.suggestions_label)

        self.setLayout(layout)

    # Function to update the password strength in real time
    def update_password_strength(self):
        user_password = self.password_input.text()
        strength, feedback = check_password_strength(user_password)

        # Update the strength label
        self.strength_label.setText(f"Password strength: {strength}")

        # Update the color of the strength indicator
        if strength == "Weak":
            color = "red"
        elif strength == "Moderate":
            color = "limegreen"
        else:  # Strong
            color = "green"

        self.strength_indicator.setStyleSheet(f"background-color: {color};")

        # Update suggestions
        if feedback:
            self.suggestions_label.setText(
                "Suggestions to improve your password:\n" + "\n".join([f"- Add {suggestion}" for suggestion in feedback])
            )
        else:
            self.suggestions_label.setText("Great job! Your password is strong.")

    # Function to toggle password visibility
    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    # Function to generate a password
    def generate_password(self):
        generated_password = generate_password()
        self.password_input.setText(generated_password)


# Main entry point for the application
def main():
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

