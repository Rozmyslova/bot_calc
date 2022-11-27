import datetime
from datetime import datetime


def log(data_from_user, command, result):
    current_datetime = datetime.now()
    temp = str(current_datetime)
    with open("results.txt", "a", encoding='utf-8') as file:
        file.write(f'\n{temp} {", "} {data_from_user} {", "} {command} {", "} {result}')