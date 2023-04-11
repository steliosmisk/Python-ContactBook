from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QVBoxLayout, QMessageBox, QGroupBox
)
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QRegExp
from pydantic.networks import email_validator


def save_contact():
    name = name_input.text()
    phone = phone_input.text()
    email = email_input.text()
    address = address_input.text()

    if not all([name, phone, email, address]):
        QMessageBox.warning(None, 'Error', 'Please enter all contact information')
    else:
        with open('mycontacts.txt', 'a') as f:
            f.write(f'Name: {name}\n')
            f.write(f'Phone: {phone}\n')
            f.write(f'Email: {email}\n')
            f.write(f'Address: {address}\n')
            f.write(f'--------------------------------\n')
        QMessageBox.information(None, 'Success', 'Contact saved successfully')
        clear_inputs()


def clear_inputs():
    name_input.setText('')
    phone_input.setText('')
    email_input.setText('')
    address_input.setText('')


# Initialization
app = QApplication([])
display = QWidget()
display.setWindowTitle("Contact Book")
display.setGeometry(300, 300, 300, 300)

# Create layout
fonts = QFont("Arial", 10, QFont.Bold)
layout = QVBoxLayout()

# Create name
name_layout = QHBoxLayout()
name_label = QLabel('Name: ')
name_label.setFont(fonts)
name_layout.addWidget(name_label)
name_input = QLineEdit()
name_input.setPlaceholderText("Enter a name")
name_layout.addWidget(name_input)

# Create phone
phone_layout = QHBoxLayout()
phone_label = QLabel('Phone: ')
phone_label.setFont(fonts)
phone_layout.addWidget(phone_label)
phone_input = QLineEdit()
phone_input.setPlaceholderText("Enter a phone number")
phone_validator = QRegExpValidator(QRegExp("[+()0-9]+"))
phone_input.setValidator(phone_validator)
phone_layout.addWidget(phone_input)

# Create email
email_layout = QHBoxLayout()
email_label = QLabel('Email: ')
email_label.setFont(fonts)
email_layout.addWidget(email_label)
email_input = QLineEdit()
email_input.setPlaceholderText("Enter an email address")
email_pattern = QRegExp("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
email_validator = QRegExpValidator(email_pattern)
email_input.setValidator(email_validator)
email_layout.addWidget(email_input)

# Create Address
address_layout = QHBoxLayout()
address_label = QLabel('Address: ')
address_label.setFont(fonts)
address_layout.addWidget(address_label)
address_input = QLineEdit()
address_input.setPlaceholderText("Enter an address")
address_layout.addWidget(address_input)

# Create save button
save_button = QPushButton('Save')
save_button.clicked.connect(save_contact)

# Create contact group box
contact_group_box = QGroupBox('Contact Information')
contact_layout = QGridLayout()
contact_layout.addLayout(name_layout, 0, 0)
contact_layout.addLayout(phone_layout, 1, 0)
contact_layout.addLayout(email_layout, 2, 0)
contact_layout.addLayout(address_layout, 3, 0)
contact_group_box.setLayout(contact_layout)

# Add widgets to layout
layout.addWidget(contact_group_box)
layout.addWidget(save_button)

# Set layout
display.setLayout(layout)

# Events
display.show()
app.exec_()
