import requests
from requests import get
import sys

def main():
    menu()


def menu():
    choice = input("""
    A - Get User Public IP
    B - Get Location Information using IP
    Q - Exit

    Please enter your choice: """)

    if choice == "A" or choice =="a":
        get_public_ip()
    elif choice == "B" or choice =="b":
        get_ip_location()
    elif choice =="Q" or choice =="q":
        sys.exit
    else:
        print("Please select only either A or B")
        print("Please try again")
        menu()


def get_public_ip():
    ip = get('https://api.ipify.org').text 
    print('\nPublic IP address is: {}'.format(ip)) 


def get_ip_location():
    ip_address = input("\ninput your IP Address: ") 
    
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json() 
    
    ip_location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country code": response.get("country_code"),
        "currency": response.get("currency_name"),
        "languages": response.get("languages"),
        "time zone": response.get("timezone"),
        "postal code": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "calling code": response.get("country_calling_code"),
        "asn": response.get("asn"),
        "isp": response.get("org")
    }
    return print(ip_location_data)

main()