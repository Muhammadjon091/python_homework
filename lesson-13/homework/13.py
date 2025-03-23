from datetime import date

def calculate_age():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = date.fromisoformat(birth_date)
    today = date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30  
    if months < 0:
        years -= 1
        months += 12

    print(f"Your age: {years} years, {months} months, and {days} days.")

calculate_age()




def days_until_birthday():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = date.fromisoformat(birth_date)
    today = date.today()

    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_remaining = (next_birthday - today).days
    print(f"Days until next birthday: {days_remaining} days.")

days_until_birthday()




from datetime import datetime, timedelta

def schedule_meeting():
    current_time = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))

    start_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(hours=duration_hours, minutes=duration_minutes)

    print(f"Meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")

schedule_meeting()





from datetime import datetime
import pytz

def timezone_converter():
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_timezone = input("Enter current timezone (e.g., 'America/New_York'): ")
    to_timezone = input("Enter target timezone (e.g., 'Asia/Tokyo'): ")

    dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    localized_dt = from_tz.localize(dt)
    converted_dt = localized_dt.astimezone(to_tz)

    print(f"Converted time: {converted_dt.strftime('%Y-%m-%d %H:%M')} in {to_timezone}")

timezone_converter()





import time

def countdown_timer():
    future_time = input("Enter future date and time (YYYY-MM-DD HH:MM): ")
    target_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M")

    while True:
        now = datetime.now()
        remaining = target_time - now
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}")
        time.sleep(1)

countdown_timer()



import re

def validate_email():
    email = input("Enter an email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        print("Valid email!")
    else:
        print("Invalid email format.")

validate_email()





def format_phone_number():
    phone = input("Enter a 10-digit phone number: ")
    if len(phone) == 10 and phone.isdigit():
        formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        print("Formatted phone number:", formatted)
    else:
        print("Invalid phone number.")

format_phone_number()





def check_password_strength():
    password = input("Enter a password: ")
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if length and has_upper and has_lower and has_digit:
        print("Strong password!")
    else:
        print("Weak password! Must be at least 8 characters, contain uppercase, lowercase, and a digit.")

check_password_strength()




def find_word():
    text = input("Enter text: ")
    word = input("Enter word to find: ")
    
    occurrences = [i for i in range(len(text)) if text.startswith(word, i)]
    
    if occurrences:
        print(f"Word found at positions: {occurrences}")
    else:
        print("Word not found.")

find_word()





def extract_dates():
    text = input("Enter text: ")
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    
    dates = re.findall(pattern, text)
    
    if dates:
        print("Extracted dates:", dates)
    else:
        print("No dates found.")

extract_dates()





