import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone(+551199999999): ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))