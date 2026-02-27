import luhncheck as l
def iscreditcard(cardnum):
    cardnum=cardnum.replace(" ", "")
    cardnum=cardnum.replace("-", "")
    cardnum=int(cardnum)
    if l(cardnum, 16):
        return True
    else:
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
        validmonths=["1","2","3","4","5","6","7","8","9","10","11","12","01","02","03","04","05","06","07","08","09"]
        validyears=["26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]# ai use declaration. prompt:list every number from 00-99 in a comma separated list with speech marks around each number
        if mm not in validmonths:
            return False
        elif yy not in validyears:
            return False
        else:
            return True

    except ValueError:
        return False
    