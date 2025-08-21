class Lead:
    def __init__(self, crm_id, name, phone, email, from_date, nights, from_city, departure_city,
                 destination_city, budget, assigned_seller, travelling_cities=None):
        if not phone or not name or not email or nights < 0:
            raise ValueError("Invalid or missing required fields")
        self.crm_id = crm_id
        self.name = name
        self.phone = phone
        self.email = email
        self.from_date = from_date
        self.nights = nights
        self.from_city = from_city
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.budget = budget
        self.assigned_seller = assigned_seller
        self.travelling_cities = travelling_cities if travelling_cities else []

    def add_city(self, city_name):
        if city_name not in self.travelling_cities:
            self.travelling_cities.append(city_name)

    def remove_city(self, city_name):
        if city_name in self.travelling_cities:
            self.travelling_cities.remove(city_name)

    def get_lead_summary(self):
        return {
            "crm_id": self.crm_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "from_date": str(self.from_date),
            "nights": self.nights,
            "from_city": self.from_city,
            "departure_city": self.departure_city,
            "destination_city": self.destination_city,
            "budget": self.budget,
            "assigned_seller": self.assigned_seller,
            "travelling_cities": self.travelling_cities
        }

def validate_lead_data(lead_data):
        if not lead_data.get('crm_id'):
            raise ValueError("Invalid or missing required fields")
        if lead_data.get('nights', 0) < 0:
            raise ValueError("Invalid or missing required fields")


def fetch_lead_from_zoho(crm_id):
    # Simulated Zoho lead fetching logic (replace with actual Zoho API calls when needed)
    return {
        'crm_id': crm_id,
        'name': 'Default Name',
        'phone': '0000000000',
        'email': 'default@example.com',
        'from_date': '2025-01-01',
        'nights': 3,
        'from_city': 'Mumbai',
        'departure_city': 'BOM',
        'destination_city': 'Dubai',
        'assigned_seller': 'priya',
        'budget': 50000,
        'travelling_cities': ['Dubai']
    }