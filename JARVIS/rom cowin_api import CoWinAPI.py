from cowin_api import CoWinAPI

pin_code = "110059"
date = '14-05-2021' 
min_age_limit = 18 

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
print(available_centers)