import phonenumbers
from phonenumbers import geocoder
ph = input("Enter the phonenumber:")
phone_number1 = phonenumbers.parse(ph)
print("Phone Number Location:")
print(geocoder.description_for_number(phone_number1,"en"))
