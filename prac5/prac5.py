import sys
from datetime import datetime

class DateValidationError(Exception): pass

def parse_and_validate_dates(date_str1: str, date_str2: str):
    try:
        d1 = datetime.strptime(date_str1, "%Y-%m-%d")
        d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    except ValueError:
        raise DateValidationError("Неправильний формат дати. Використовуйте РРРР-ММ-ДД.")
    if d2 < d1:
        raise DateValidationError("Друга дата не може бути раніше за першу.")
    return d1, d2

def days_between(d1, d2):
    return (d2 - d1).days

def run_tests():
    assert days_between(datetime(2020, 1, 1), datetime(2020, 1, 10)) == 9
    assert days_between(datetime(2020, 2, 28), datetime(2020, 3, 1)) == 2
    print("Тести пройдено")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    try:
        date1 = input().strip()
        date2 = input().strip()
        d1, d2 = parse_and_validate_dates(date1, date2)
        print(days_between(d1, d2))
    except DateValidationError as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()