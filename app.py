from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

model = pickle.load(open('flight_model.pkl','rb'))

app = Flask(__name__)

@app.route("/")
@cross_origin()

def home():
    return render_template("form.html")

@app.route("/predict", methods=["GET","POST"])
@cross_origin()




def predict():
    if request.method =="POST":
        source = request.form["element_5"]
        if source=="Kolkata":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
        elif source=="Delhi":
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
        elif source=="Chennai":
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
        elif source == "Mumbai":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1

        destination = request.form['element_6']
        if destination == "Kolkata":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
        elif destination == "Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        elif destination == "Cochin":
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        elif destination == "Hyderabad":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0



        stops = request.form['element_7']

        airline  = request.form['element_8']
        if airline == "Air India":
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "Jet Airways":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 1
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "SpiceJet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 1
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "Multiple carriers":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 1
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "GoAir":
            Airline_Air_India = 0
            Airline_GoAir = 1
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "IndiGo":
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo = 1
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "Vistara":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 1
            Airline_Vistara_Premium_economy = 0
        elif airline == "Vistara Premium economy":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 1
        elif airline == "Jet Airways Business":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 1
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "Multiple carriers Premium economy":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 1
            Airline_SpiceJet = 0
            Airline_Trujet  = 0
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0
        elif airline == "Trujet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo  = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business  = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy  = 0
            Airline_SpiceJet = 0
            Airline_Trujet  = 1
            Airline_Vistara  = 0
            Airline_Vistara_Premium_economy = 0

        journey_day = int(request.form['element_1_1'])
        journey_month = int(request.form['element_1_2'])

        # am_pm_d = request.form['element_2_4']
        dep_hour = int(request.form['element_2_1'])
        dep_minute = int(request.form['element_2_2'])
        # if am_pm_d == "PM":
        #     def_hour = dep_hour+12

        arr_hour = int(request.form['element_4_1'])
        arr_minute = int(request.form['element_4_2'])
        # am_pm = request.form['element_4_4']
        # if am_pm == "PM":
        #     arr_hour = arr_hour+12

        arr_day = int(request.form['element_3_1'])
        arr_month = int(request.form['element_3_2'])

        hour = abs(arr_hour-dep_hour)
        minute = abs(arr_month - dep_minute)
        duration = hour*60+minute

        # ['Duration', 'Total_Stops', 'Price', 'journey_day', 'journey_month',
        #  'dep_hour', 'dep_minute', 'arr_hour', 'arr_minute', 'Airline_Air India',
        #  'Airline_GoAir', 'Airline_IndiGo', 'Airline_Jet Airways',
        #  'Airline_Jet Airways Business', 'Airline_Multiple carriers',
        #  'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        #  'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        #  'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
        #  'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
        #  'Destination_Kolkata', 'Destination_New Delhi']

        Destination_New_Delhi = 0
        prediction = model.predict([[
            duration, stops, journey_day, journey_month,dep_hour, dep_minute, arr_hour,arr_minute,
            Airline_Air_India,
            Airline_GoAir,
            Airline_IndiGo,
            Airline_Jet_Airways,
            Airline_Jet_Airways_Business,
            Airline_Multiple_carriers,
            Airline_Multiple_carriers_Premium_economy,
            Airline_SpiceJet,
            Airline_Trujet,
            Airline_Vistara,
            Airline_Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi
        ]])

        output = round(prediction[0],2)

        return render_template('form.html',prediction_text="Fare for the Flight is Rs. {}".format(output))
    return render_template('home.html')




if __name__ == "__main__":
    app.run(debug=True)