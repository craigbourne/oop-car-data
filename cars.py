class CarDataError(Exception):
    """Custom exception for car data related errors"""
    pass

class Car:
    def __init__(self):
        # Initialise Car class with with the top 10 registered cars in the UK for 2024: https://www.rac.co.uk/drive/advice/buying-and-selling-guides/the-top-10-most-popular-cars-in-the-uk/
        try:
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
          self._validate_data()
        except Exception as e:
            raise CarDataError(f"Error initialising car data: {str(e)}")
    def _validate_data(self):

      # Validates the car data structure and content
      # Raises CarDataError if data is invalid

      required_specs = {'registrations', 'engine_options', 'transmission', 'fuel_type', 'body_style'}
      
      for manufacturer, models in self.car_data.items():
          if not isinstance(manufacturer, str):
              raise CarDataError(f"Invalid manufacturer name: {manufacturer}")

          for model, specs in models.items():
              if not isinstance(model, str):
                  raise CarDataError(f"Invalid model name: {model}")

              # Check for required specification fields
              missing_specs = required_specs - specs.keys()
              if missing_specs:
                  raise CarDataError(
                      f"Missing specifications for {manufacturer} {model}: {missing_specs}"
                  )

              # Validate registration numbers
              if not isinstance(specs['registrations'], int):
                  raise CarDataError(
                      f"Invalid registration number for {manufacturer} {model}"
                  )

              # Validate list fields
              list_fields = ['engine_options', 'transmission', 'fuel_type']
              for field in list_fields:
                  if not isinstance(specs[field], list):
                      raise CarDataError(
                          f"Invalid {field} data for {manufacturer} {model}"
                      )

    def demonstrate_items(self):
        """
        Demonstrates the items() method on car_data dictionary.
        Shows how to access  keys and values simultaneously at each level.
        """
        print("\n======================= Demonstrating items() method =======================")
        
        # First level: Manufacturers and their models
        for manufacturer, models in self.car_data.items():
            print(f"\nManufacturer: {manufacturer}")
            # Second level: Models and their specifications
            for model, specs in models.items():
                print(f"\n  Model: {model}")
                # Third level: Individual specifications
                for spec_name, spec_value in specs.items():
                    if isinstance(spec_value, list):
                        print(f"    {spec_name}: {', '.join(map(str, spec_value))}")
                    else:
                        print(f"    {spec_name}: {spec_value}")

    def demonstrate_keys(self):
        """
        Demonstrates the keys() method on our nested dictionary.
        Shows available manufacturers, models, and specification categories.
        """
        print("\n======================= Demonstrating keys() method =======================")


        # Get all manufacturer names
        manufacturers = self.car_data.keys()
        print(f"Available manufacturers: {', '.join(manufacturers)}")

        # Get models for each manufacturer
        for manufacturer in manufacturers:
            models = self.car_data[manufacturer].keys()
            print(f"\n{manufacturer} models: {', '.join(models)}")

            # Get specification categories for first model
            first_model = list(models)[0]
            specs = self.car_data[manufacturer][first_model].keys()
            print(f"Specification categories for {first_model}: {', '.join(specs)}")

    def demonstrate_values(self):
        """
        Demonstrates the values() method on our nested dictionary.
        Shows the actual data without the associated keys.
        """
        print("\n======================= Demonstrating values() method =======================")

        # Show registration numbers for all models
        print("\nRegistration numbers for all models:")
        for manufacturer in self.car_data.values():
            for model, specs in manufacturer.items():
                print(f"  {model}: {specs['registrations']} registrations")

        # Show all available engine options across the range
        all_engines = set()
        for manufacturer in self.car_data.values():
            for specs in manufacturer.values():
                all_engines.update(specs['engine_options'])
        print("\nAll available engine options:")
        for engine in sorted(all_engines):
            print(f"  - {engine}")

def main():
    # Main function to demonstrate dictionary operations on UK car registration data
    try:
        print("UK Car Registration Data Analysis")

        car_system = Car()

        car_system.demonstrate_items()
        car_system.demonstrate_keys()
        car_system.demonstrate_values()

    except CarDataError as e:
        print(f"Error in car data: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()