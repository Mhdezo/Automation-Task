# SeleniumBase Automation Task for Elevatus Platform
This repository contains a Python script using SeleniumBase to automate the UI testing of candidate registration and job application on the Elevatus platform.

________________________________________
# Task Overview:
This project automates the following processes:
1.	Register a New Candidate: Automates the full registration process.
2.	Apply for a Job: Automates applying for a job on the platform.
Key Features:
•	Dynamic Data Generation: New user data (name, email, password, phone number) is generated for each test run.
•	Data Validation: Several checks are performed to ensure that the data entered is valid.
•	Test Reporting: A detailed test report is created after each run.
________________________________________
# Prerequisites:
Ensure the following are installed:
•	Python 3.x installed.
•	Required dependencies: pip install seleniumbase faker pytest
________________________________________
# How to Run the Test:
1.	Open Command Prompt (CMD)
2.	Clone the repository: git clone https://github.com/Mhdezo/Automation-Task.git
3.	Navigate to the project directory: cd Automation-Task
4.	Run the test and generate a test report: pytest registration.py --html=report.html
________________________________________
# Key Validations Performed:
1.	Email Format Validation: Ensures a valid email format (contains @ and a proper domain).
2.	Password Complexity Validation: Checks that the password includes uppercase, lowercase, digits, and symbols (no dot .).
3.	Phone Number Validation: Validates that the phone number starts with '077', '078', or '079'.
4.	Name Validation: Ensures first and last names are non-empty.
5.	Dynamic Data Generation: First name, last name, email, password, and phone number are generated for each test run.
6.	Form Submission: Verifies that the registration form is submitted successfully.
7.	Job Application Validation: Confirms that the candidate successfully applies for the job.
________________________________________
# Test Report:
After each run, a report (report.html) is generated, detailing:
•	Test Results (pass/fail for each step).
•	Execution Time
•	Errors, if any, encountered during the test.
________________________________________
# Notes:
This is my first project using SeleniumBase and Python for UI automation. It focuses on form handling, dynamic data generation, and a real-world scenario of job application testing.
