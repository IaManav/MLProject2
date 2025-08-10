from django import forms

class CarPriceForm(forms.Form):
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
