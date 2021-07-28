# Install in  terminal this command: pip install phonenumbers
#then import the phone numbers

import phonenumbers  #we need a test.py file

from test import number 

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
#C = Country, H= History
print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
