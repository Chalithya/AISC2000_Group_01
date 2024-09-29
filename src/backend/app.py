from flask import Flask, render_template, request
import pickle
import numpy as np
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app = Flask(__name__, template_folder=template_dir)

models = {
    "ada_model": pickle.load(open('../models/ada_model.pkl', 'rb')),
    "xgb_model": pickle.load(open('../models/xgb_model.pkl', 'rb')),
    "dt_model": pickle.load(open('../models/dt_model.pkl', 'rb')),
    "rf_model": pickle.load(open('../models/rf_model.pkl', 'rb'))
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_validated():
    try:

        model_selection = request.form.get('model_selection', 'ada_model')
        model = models[model_selection] 

        business_name = request.form.get('business_name', 0)
        business_rating_stars = float(request.form.get('business_rating_stars', 0))
        business_review_count = float(request.form.get('business_review_count', 0))
        total_checkins = float(request.form.get('total_checkins', 0))
        BusinessAcceptsCreditCards = int(request.form.get('BusinessAcceptsCreditCards', 0))
        BusinessParking_garage = int(request.form.get('BusinessParking_garage', 0))
        BusinessParking_street = int(request.form.get('BusinessParking_street', 0))
        BusinessParking_validated = int(request.form.get('BusinessParking_validated', 0))
        BusinessParking_lot = int(request.form.get('BusinessParking_lot', 0))
        BusinessParking_valet = int(request.form.get('BusinessParking_valet', 0))
        RestaurantsGoodForGroups = int(request.form.get('RestaurantsGoodForGroups', 0))
        BikeParking = int(request.form.get('BikeParking', 0))
        is_open = int(request.form.get('is_open', 0))

        additional_features = np.zeros(14)

        features = np.array([[business_rating_stars, business_review_count, total_checkins,
                              BusinessAcceptsCreditCards, BusinessParking_garage,
                              BusinessParking_street, BusinessParking_validated,
                              BusinessParking_lot, BusinessParking_valet,
                              RestaurantsGoodForGroups, BikeParking, is_open] + list(additional_features)])

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = f'According to {model_selection} the {business_name} is validated.'
            color = 'green'
        else:
            result = f'According to {model_selection} the {business_name} is not validated.'
            color = 'red'

    except Exception as e:
        result = 'Error: ' + str(e)
        color = 'orange'

    return render_template('index.html', result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
