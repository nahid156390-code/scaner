import phonenumbers
from phonenumbers import geocoder, carrier

def get_number_info():
    # User se input lein
    number = input("Phone Number daalein (country code k saath, e.g., +923001234567): ")

    try:
        # Number ko parse karein
        parsed_number = phonenumbers.parse(number)

        # Location aur Carrier nikalain
        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")

        print("\n--- Result ---")
        print(f"Number: {number}")
        print(f"Location: {location}")
        print(f"Service Provider: {service_provider}")
    except Exception as e:
        print("Error: Number invalid hai ya galat format mein hai.")

if __name__ == "__main__":
    get_number_info()
