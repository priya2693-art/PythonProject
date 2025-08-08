
class PaymentGateway:
    def charge(self, amount: float) -> bool:
        print(f"Charging ₹{amount}")
        return True  # Simulates external API call

class FlightBookingService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def book_flight(self, amount: float) -> str:
        if self.payment_gateway.charge(amount):
            return "Booking Confirmed"
        else:
            return "Payment Failed"
