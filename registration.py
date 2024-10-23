from seleniumbase import BaseCase
from faker import Faker
import random
import string
import time

class ElevatusTest(BaseCase):

    def setUp(self):
        # Generating random test data
        super().setUp()
        self.fake = Faker()

    def validate_email(self, email):
        # Email validation --> checks for the presence of '@' and a domain
        return '@' in email and '.' in email.split('@')[1]

    def validate_password(self, password):
        # Password validation --> must include upper, lower case, digits, and symbols (except '.')
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation.replace('.', '') for c in password)
        return has_upper, has_lower, has_digit, has_symbol

    def validate_phone(self, phone):
        # Validates phone numbers --> starting with '077', '078', or '079'
        return phone.startswith(('077', '078', '079'))

    def generate_valid_password(self):
        # Generates a valid password
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation.replace('.', '&'), k=12))
            if all(self.validate_password(password)):
                return password

    def generate_valid_user_data(self):
        # Generates a valid user data for registration
        while True:
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            password = self.generate_valid_password()
            email = self.fake.email()
            phone = random.choice(['077', '078', '079']) + self.fake.msisdn()[:7]

            # Return data only if all validations pass
            if (self.validate_email(email) and
                all(self.validate_password(password)) and
                self.validate_phone(phone) and
                first_name.strip() and last_name.strip()):
                return first_name, last_name, password, email, phone
            else:
                print("Invalid data generated, retrying...")

    def register_candidate(self, first_name, last_name, password, email, phone):
        # Candidate registration process
        self.open("https://mcitcareerssd.elevatus.io/")
        self.click('button:contains("I Accept Recommended Cookies")')
        self.click('button:contains("Register")')

        # Fill in registration form
        self.type('input[name="firstName"]', first_name)
        self.type('input[name="lastName"]', last_name)
        self.type('input[name="password"]', password)
        self.type('input[name="confirmPassword"]', password)
        self.type('input[name="email"]', email)
        self.type('input[type="tel"]', phone)

        # Enable and submit the form
        # MAke the Sign button clickable ** The T&C couldn't locate it (CustomCheckboxLogin)
        self.execute_script("document.querySelector('button[type=\"submit\"]').removeAttribute('disabled')")
        self.click('button[type="submit"]')
        time.sleep(5)

    def apply_for_job(self):
        # Applying for a job
        self.click('button:contains("Jobs")')
        self.click('button:contains("View")')
        time.sleep(3)
        self.click('button:contains("Apply")')
        time.sleep(3)

    def test_registration_and_job_application(self):
        # Registration and job application
        first_name, last_name, password, email, phone = self.generate_valid_user_data()
        self.register_candidate(first_name, last_name, password, email, phone)
        self.apply_for_job()

    def tearDown(self):
        # Cleanup after each test
        super().tearDown()
