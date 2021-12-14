from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Booking, Car, Contact, Driver, Flight, Gallery, Trip, Category, Contact
import datetime
from django.forms import Form, ModelForm, DateField, widgets
from django_countries.widgets import CountrySelectWidget


region_choices = ('ab', 'bc')
class TripForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Trip destination'}))
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation on arrival')
    # trip_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation at trip destination')
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['destination'].label = "Trip destination"
        self.fields['image'].label = "Upload image(formats .png, .jpeg, jpg)"
        self.fields['slots'].placeholder = "Number of slots"
        self.fields['start'].label = "Start date of trip"
        self.fields['end'].label = "Start date of trip"
        self.fields['price'].placeholder = "Price(in Dollars)"
        # self.fields['category'].widget = forms.CheckboxSelectMultiple()

    def clean_date(self):
        date = self.cleaned_data['date']
        if self.start < datetime.date.today():
            raise forms.ValidationError("You should only book dates in the future!")
        return date

    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ('category', 'available', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'})
        } 


class FlightForm(forms.ModelForm):
    # start = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From '}))
    # destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To'}))
    # price = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Price of flight'}))

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ('available', )   


class CarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Make of car eg toyota'}))

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('available', )   
     

class GalleryForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Caption uploaded image'}))

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Gallery
        fields = '__all__'
        exclude = ('hidden', )   


class BookingForm(forms.ModelForm):
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked',)
        

class TripBookingForm(forms.ModelForm):
    pickup = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter location we can pick you for the trip'}))
    dropoff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter a location we can drop you after trip'}))
    slots = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter number of trip participants'}))

    def __init__(self, *args, **kwargs):
        super(TripBookingForm, self).__init__(*args, **kwargs)
        self.fields['trip'].disabled = True 
        self.fields['service'].disabled = True 
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('car', 'time_booked', 'car_hire', 'flight', 'flight_type', 'departure_date', 'adults', 'children', 
        'infants', 'driven_by', 'carhire_trip', 'booked_by',)


class FlightBookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlightBookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].disabled = True 
        self.fields['flight'].disabled = True 
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'car', 'start', 'end', 'trip', 'car_hire', 'pickup', 'dropoff', 'driven_by', 
        'carhire_trip', 'booked_by', 'slots', )
        widgets = {
            'departure_date': widgets.DateInput(attrs={'type': 'date'}),
            'country': CountrySelectWidget()
        } 


class CarBookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CarBookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].disabled = True 
        self.fields['car'].disabled = True 
        self.fields['start'].label = "Pickup date"
        self.fields['end'].label = "Drop off date"
        self.fields['carhire_trip'].label = "Area of car trip"
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'flight', 'trip', 'flight_type', 'departure_date', 'pickup', 'dropoff',  'slots', 
        'adults', 'children', 'infants', 'booked_by',)
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'}),
        } 


class ContactForm(forms.Form):    
    # full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    # email = forms.CharField()
    # telephone = forms.CharField()
    # message = forms.Textarea()

    class Meta(object):
        model = Contact
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
				attrs={
					'full_name': 'form-control'
					}
				),
            'content': forms.Textarea(
				attrs={
					'email': 'form-control'
					}
				),
            'telephone': forms.TextInput(
				attrs={
					'telephone': 'form-control'
					}
				),
            'message': forms.Textarea(
				attrs={
					'message': 'form-control'
					}
				),
			}


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter category'}))
  
    class Meta:
        model = Category
        fields = '__all__'


class AccomodationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter name of accomodation'}))
    # budget = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter name of accomodation'}))

    class Meta:
        model = Accomadation
        fields = '__all__'
        exclude = ('available',)


