from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CarPriceForm
from src.pipeline.predict_pipeline import PredictPipeline, Custom_Data

def car_price_predict(request):
    if request.method == 'POST':
        form = CarPriceForm(request.POST)
        if form.is_valid():
            data = Custom_Data(
                year=form.cleaned_data['year'],
                selling_price=0,  # or as applicable
                km_driven=form.cleaned_data['km_driven'],
                fuel=None,  # add if needed
                seller_type=form.cleaned_data['seller_type'],
                transmission=form.cleaned_data['transmission'],
                owner=form.cleaned_data['owner'],
                mielage=None,  # add if needed
                engine=form.cleaned_data['engine'],
                max_power=form.cleaned_data['max_power'],
                seats=form.cleaned_data['seats'],
            )
            input_df = data.get_data_as_dataframe()
            pipeline = PredictPipeline()
            prediction = pipeline.predict(input_df)[0]

            # Store the prediction in session or pass via URL or post-redirect-get
            request.session['prediction'] = prediction

            # Redirect to result page
            return redirect(reverse('car_price_result'))
    else:
        form = CarPriceForm()
    return render(request, 'predictor/form.html', {'form': form})


def car_price_result(request):
    prediction = request.session.get('prediction', None)
    return render(request, 'predictor/result.html', {'prediction': prediction})

