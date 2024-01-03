import re

def chek_password(password):
    if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
        return True
    else:
        return False

