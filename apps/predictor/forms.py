from django import forms

class CarPriceForm(forms.Form):
    # Brand field with all the car brands
    # brand = forms.ChoiceField(
    #     label='Car Brand',
    #     choices=[
    #         ('', 'Select Brand'),  # Default empty option
    #         ('Maruti', 'Maruti'),
    #         ('Skoda', 'Skoda'), 
    #         ('Honda', 'Honda'),
    #         ('Hyundai', 'Hyundai'),
    #         ('Toyota', 'Toyota'),
    #         ('Ford', 'Ford'),
    #         ('Renault', 'Renault'),
    #         ('Mahindra', 'Mahindra'),
    #         ('Tata', 'Tata'),
    #         ('Chevrolet', 'Chevrolet'),
    #         ('Fiat', 'Fiat'),
    #         ('Datsun', 'Datsun'),
    #         ('Jeep', 'Jeep'),
    #         ('Mercedes-Benz', 'Mercedes-Benz'),
    #         ('Mitsubishi', 'Mitsubishi'),
    #         ('Audi', 'Audi'),
    #         ('Volkswagen', 'Volkswagen'),
    #         ('BMW', 'BMW'),
    #         ('Nissan', 'Nissan'),
    #         ('Lexus', 'Lexus'),
    #         ('Jaguar', 'Jaguar'),
    #         ('Land', 'Land Rover'),
    #         ('MG', 'MG'),
    #         ('Volvo', 'Volvo'),
    #         ('Daewoo', 'Daewoo'),
    #         ('Kia', 'Kia'),
    #         ('Force', 'Force'),
    #         ('Ambassador', 'Ambassador'),
    #         ('Ashok', 'Ashok Leyland'),
    #         ('Isuzu', 'Isuzu'),
    #         ('Opel', 'Opel'),
    #         ('Peugeot', 'Peugeot'),
    #     ]
    # )
    
    year = forms.IntegerField(label='Year', min_value=1900, max_value=2025)
    km_driven = forms.IntegerField(label='Kilometers Driven', min_value=0)
    engine = forms.IntegerField(label='Engine Capacity (cc)', min_value=500)
    max_power = forms.IntegerField(label='Max Power (bhp)', min_value=10)
    seats = forms.IntegerField(label='Number of Seats', min_value=2, max_value=15)
    seller_type = forms.ChoiceField(
        choices=[
            ('Individual', 'Individual'),
            ('Dealer', 'Dealer'),
            ('Trustmark Dealer', 'Trustmark Dealer'),
        ]
    )
    owner = forms.ChoiceField(
        choices=[
            ('First Owner', 'First Owner'),
            ('Second Owner', 'Second Owner'),
            ('Third Owner', 'Third Owner'),
            ('Fourth & Above Owner', 'Fourth & Above Owner'),
            ('Test Drive Car', 'Test Drive Car'),
        ]
    )
    transmission = forms.ChoiceField(
        choices=[
            ('Manual', 'Manual'),
            ('Automatic', 'Automatic'),
        ]
    )