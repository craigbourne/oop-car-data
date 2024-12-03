class Car:
    def __init__(self):
        # Initialise Car class with with the top 10 registered cars in the UK for 2024: https://www.rac.co.uk/drive/advice/buying-and-selling-guides/the-top-10-most-popular-cars-in-the-uk/
        self.car_data = {
            "Ford": {
                "Puma": {
                    "registrations": 42465,
                    "engine_options": ["1.0L EcoBoost", "1.0L EcoBoost Hybrid"],
                    "transmission": ["7-speed Automatic", "6-speed Manual"],
                    "fuel_type": ["Petrol", "Petrol Hybrid"],
                    "body_style": "Compact SUV"
                }
            },
            "Kia": {
                "Sportage": {
                    "registrations": 42115,
                    "engine_options": ["1.6L T-GDi", "1.6L CRDi"],
                    "transmission": ["6-speed Manual", "7-speed DCT"],
                    "fuel_type": ["Petrol", "Diesel", "Hybrid"],
                    "body_style": "SUV"
                }
            },
            "Nissan": {
                "Qashqai": {
                    "registrations": 35271,
                    "engine_options": ["1.3L DiG-T", "1.5L e-POWER"],
                    "transmission": ["6-speed Manual", "Xtronic"],
                    "fuel_type": ["Petrol", "Hybrid"],
                    "body_style": "SUV"
                },
                "Juke": {
                    "registrations": 30548,
                    "engine_options": ["1.0L DiG-T", "1.6L Hybrid"],
                    "transmission": ["6-speed Manual", "7-speed DCT"],
                    "fuel_type": ["Petrol", "Hybrid"],
                    "body_style": "Compact SUV"
                }
            },
            "Volkswagen": {
                "Golf": {
                    "registrations": 29427,
                    "engine_options": ["1.0L TSI", "1.5L TSI", "2.0L TSI"],
                    "transmission": ["6-speed Manual", "7-speed DSG"],
                    "fuel_type": ["Petrol", "Diesel", "Hybrid"],
                    "body_style": "Hatchback"
                },
                "Polo": {
                    "registrations": 25817,
                    "engine_options": ["1.0L TSI", "2.0L TSI"],
                    "transmission": ["5-speed Manual", "7-speed DSG"],
                    "fuel_type": ["Petrol"],
                    "body_style": "Hatchback"
                }
            },
            "Hyundai": {
                "Tucson": {
                    "registrations": 28115,
                    "engine_options": ["1.6L T-GDi", "1.6L CRDi"],
                    "transmission": ["6-speed Manual", "7-speed DCT"],
                    "fuel_type": ["Petrol", "Diesel", "Hybrid"],
                    "body_style": "SUV"
                }
            },
            "Audi": {
                "A3": {
                    "registrations": 26830,
                    "engine_options": ["1.0L TFSI", "1.5L TFSI", "2.0L TFSI"],
                    "transmission": ["6-speed Manual", "7-speed S tronic"],
                    "fuel_type": ["Petrol", "Diesel", "Hybrid"],
                    "body_style": "Hatchback"
                }
            },
            "MG": {
                "HS": {
                    "registrations": 25414,
                    "engine_options": ["1.5L Turbo", "1.5L Plug-in Hybrid"],
                    "transmission": ["6-speed Manual", "10-speed CVT"],
                    "fuel_type": ["Petrol", "Plug-in Hybrid"],
                    "body_style": "SUV"
                }
            },
            "Volvo": {
                "XC40": {
                    "registrations": 24621,
                    "engine_options": ["1.5L T2", "2.0L T4", "P8 Pure Electric"],
                    "transmission": ["8-speed Automatic", "Single-speed"],
                    "fuel_type": ["Petrol", "Hybrid", "Electric"],
                    "body_style": "Compact SUV"
                }
            }
        }

def main():
    car_system = Car()

if __name__ == "__main__":
    main()