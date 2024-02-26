from datetime import datetime, timedelta

def get_upcoming_birthdays(employees):
    today = datetime.now().date()
    upcoming_birthdays = []

    for name, dob in employees.items():
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
        next_birthday = datetime(today.year, dob_date.month, dob_date.day).date()
        
        if next_birthday < today:
            next_birthday = datetime(today.year + 1, dob_date.month, dob_date.day).date()
        
        days_until_birthday = (next_birthday - today).days
        if days_until_birthday <= 7:
            upcoming_birthdays.append((name, next_birthday))
    
    return upcoming_birthdays

# Приклад використання:
employees = {
    "Hanna Pan": "1990-05-12",
    "Julia Terebenko": "1985-02-27",
    "Ivan Palko": "1995-02-15",
    "Dmytro Pivtorak": "1992-02-28"
}

upcoming = get_upcoming_birthdays(employees)
print("Колеги, яких потрібно привітати з днем народження на цьому тижні:")
for name, birthday in upcoming:
    print(f"{name}: {birthday.strftime('%Y-%m-%d')}")
