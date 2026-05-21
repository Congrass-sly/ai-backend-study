import re
def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$')
    e = pattern.match(email)
    return e is not None

# 正确邮箱
print(validate_email("test@example.com"))      # True
print(validate_email("user.name@example.co.uk")) # True


# 错误邮箱
print(validate_email("a@b.c"))                 # False(后缀字母未大于2)
print(validate_email("test@example"))          # False（无后缀）
print(validate_email("@example.com"))          # False（无用户名）
print(validate_email("test@.com"))             # False（域名为空）