import luhncheck as l
import bcrypt
import base64
def password_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return base64.b64encode(hashed).decode('utf-8')
def verify_password(password, hashed):
    hashed_bytes = base64.b64decode(hashed)
    return bcrypt.checkpw(password.encode('utf-8'), hashed_bytes)
def iscreditcard(cardnum):
    if cardnum is None:
        return False

    cardnum = str(cardnum).replace(" ", "").replace("-", "")
    if not cardnum.isdigit() :
        return False

    try:
        return l.is_luhn(cardnum, 16)
    except TypeError:
        # If the input is not a valid number, return False
        return False
def isemail(email):
    if"@"in email:
        emailpart1, emailpart2 = email.split("@")
        if "." in emailpart2:
            return True
        else:
            return False
def range_check(value, low, high):#checks if a value is between a low and high number and  checks that said value isn't just numbers (to prevent numeric input in name fields)
    if low <= len(value) <= high and not value.isdigit():
        return True
    else:
        return False
def mmyy_format(datestr):#for expiry date validation. checks if the input is in the standard format mm/yy  
    
    try:
        mm,yy = datestr.split("/")
        validmonths=[str(i) for i in range(1, 13)]#list comprehension that makes list of validmonths
        validyears=[str(i) for i in range(26, 100)]#list comprehension that makes list of validyears(assuming cards won't have expired)
        if mm not in validmonths:
            return False
        elif yy not in validyears:
            return False
        else:
            return True

    except ValueError:
        return False

