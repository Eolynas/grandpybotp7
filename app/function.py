from datetime import datetime


def get_date_now():
    now = datetime.now()

    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute

    if now.day < 10 :
        day = f"0{now.day}"
    if now.month < 10:
        month = f"0{now.month}"
    if now.hour < 10:
        hour = f"0{now.hour}"
    if now.minute < 10:
        minute = f"0{now.minute}"


    date_now_format = f"{day}/{month}/{year} {hour}:{minute}"

    return date_now_format

if __name__ == "__main__":
    get_date_now()