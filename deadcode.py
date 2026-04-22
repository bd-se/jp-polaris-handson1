DEBUG = True

# うるう年
# 西暦が4で割り切れる年は原則うるう年。
# ただし、100で割り切れる年は平年（365日）。
# しかし、400で割り切れる年はうるう年。
def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return True
    else:
        return False
    return False
    
if __name__ == "__main__":
    
    year = input("Enter a year: ")
    if year.isdigit():
        year = int(year)
        result = is_leap_year(year)
        if(DEBUG):
            print(f"DEBUG: {year} is a leap year.")
        else:
            print(f"DEBUG: {year} is a leap year.")

