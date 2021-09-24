from django import forms


class MyForm(forms.Form):
    CityChoices = (('mumbai', 'mumbai'),
                   ('delhi', 'delhi'),
                   ('chennai', 'chennai'),
                   ('kolkata', 'kolkata'),
                   ('jaipur', 'jaipur'),
                   ('bengaluru', 'bengaluru'),
                   ('gwalior', 'gwalior'),
                   ('lucknow', 'lucknow'),
                   ('nagpur', 'nagpur'),
                   ('thane', 'thane'),
                   ('pune', 'pune'),
                   ('kanpur', 'kanpur'),
                   ('patna', 'patna'),
                   ('virar', 'virar'))
    cityname = forms.ChoiceField(choices=CityChoices)
