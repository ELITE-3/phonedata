print ("""
 ███████████  █████   █████    ███████    ██████   █████ ██████████
░░███░░░░░███░░███   ░░███   ███░░░░░███ ░░██████ ░░███ ░░███░░░░░█
 ░███    ░███ ░███    ░███  ███     ░░███ ░███░███ ░███  ░███  █ ░ 
 ░██████████  ░███████████ ░███      ░███ ░███░░███░███  ░██████   
 ░███░░░░░░   ░███░░░░░███ ░███      ░███ ░███ ░░██████  ░███░░█   
 ░███         ░███    ░███ ░░███     ███  ░███  ░░█████  ░███ ░   █
 █████        █████   █████ ░░░███████░   █████  ░░█████ ██████████
░░░░░        ░░░░░   ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ ░░░░░░░░░░ 
                                                                   
                                                                   
                                                                   
       ██████████     █████████   ███████████   █████████          
      ░░███░░░░███   ███░░░░░███ ░█░░░███░░░█  ███░░░░░███         
       ░███   ░░███ ░███    ░███ ░   ░███  ░  ░███    ░███         
       ░███    ░███ ░███████████     ░███     ░███████████         
       ░███    ░███ ░███░░░░░███     ░███     ░███░░░░░███         
       ░███    ███  ░███    ░███     ░███     ░███    ░███         
       ██████████   █████   █████    █████    █████   █████        
      ░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░    ░░░░░   ░░░░░                                                                  
                                                                   

    CODED BY ELITE-3 """)
try:
    import phonenumbers
except ModuleNotFoundError:
    print("REQUIRED MODULES IS NOT INSTALLED \nPLS INSTALL REQUIREMNTS.TXT")
    a=0
else :
    print("required modules are installed   skipping..... \n \n")
    print("press ctrl+c to exit \n \n")
    a=1


while a==1 :
        num=input("ENTER PHONE NUMBER(with country code and +):  ")
        from phonenumbers import geocoder
        from phonenumbers import carrier
        from phonenumbers import timezone
        number = phonenumbers.parse(num)
        print("VALIDITY          :",phonenumbers.is_valid_number(number),"\n")
        print("COUNRTY           :",geocoder.description_for_number(number,'en'),"\n")
        print("CARRIER           :",carrier.name_for_number(number,'en'),"\n")
        print("TIMEZONE          :",timezone.time_zones_for_number(number),"\n")
        print("NATIONAL NO       :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL),"\n")
        print("INTERNATIONAL NO  :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),"\n")
        print("E164 NO           :",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164),"\n")
