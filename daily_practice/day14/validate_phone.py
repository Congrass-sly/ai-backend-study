import re
def validate_phone(phone):
    pattern = re.compile(r'^1[3-9]\d{9}$')
    num = pattern.match(phone)
    return num is not None