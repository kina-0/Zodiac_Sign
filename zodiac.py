def zodiac_sign(date,month):
    
    if month=="january":
        astro_sign='CAPRICON' if(date<=19) else "AQUARIUS"
        
    elif month=="feb":
        astro_sign="AQUARIUS" if (date<=18) else "PISCES"
        
    elif month=="march":
        astro_sign="PISCES" if (date<=20) else "ARIES"
        
    elif month=="april":
        astro_sign="ARIES" if (date<=19) else "TAURUS"
        
    elif month=="may":
        astro_sign="TAURUS" if (date<=20) else "GEMINI"
        
    elif month=="june":
        astro_sign="GEMINI" if (date<=20) else "CANCER"
        
    elif month=="july":
        astro_sign="CANCER" if (date<=22) else "LEO"
        
    elif month=="august":
        astro_sign="LEO" if (date<=22) else "VIRGO"
        
    elif month=="september":
        astro_sign="VIRGO" if (date<=22) else "LIBRA"
        
    elif month=="october":
        astro_sign="LIBRA" if (date<=22) else "SCORPIO"
        
    elif month=="november":
        astro_sign="SCORPIO" if (date<=21) else "SAGITTARIUS"
        
    elif month=="december":
        astro_sign="SAGITTARIUS" if (date<=21) else "CAPRICON"
    
    else:
        astro_sign="NULL"
        
    print("Your Zodiac Sign is",astro_sign)

date=int(input("Enter your date"))
month=input("enter your month")
month=month.lower()
zodiac_sign(date, month)

