from flask import Flask,request,render_template,jsonify
import random
import pickle

# Create a flask applications
app = Flask(__name__)

test_df = pickle.load(open("models/gender_test_df.pkl","rb"))
test_age_group_df = pickle.load(open("models/age_group_test_df.pkl","rb"))
gender_model = pickle.load(open("models/model_gender.pkl","rb"))
age_group_model = pickle.load(open("models/model_age_group.pkl","rb"))


@app.route("/")
def homepage():
    device_ids = test_df[test_df["train_test_flag"] == "test"]["device_id"].values
    
    # Select 50 random devices from the array
    random_devices = random.sample(sorted(device_ids), 50)

    return render_template('index.html', device_ids=random_devices)


def select_campaign(gender,age_group):
    campaign_gender = {
        "Female":[ ("Campaign 1", "Specific personalized fashion-related campaigns targeting female customers."),
                  ("Campaign 2", "Specific cashback offers on special days [for example, International Women’s Day] targeting female customers.") ],
        "Male":[ ("Campaign 3", "Personalized call and data packs targeting male customers.") ]
    }

    campaign_age = {
        "0-24":[ ("Campaign 4", "Bundled smartphone offers for the age group 0–24 years.") ],
        "25-32" : [ ("Campaign 5", "Special offers for payment wallet offers - those in the age group of 25–32 years.") ],
        "33-45":[ ("Campaign 6", "Special cashback offers for Privilege Membership 33-45 years.") ],
        "46+":[ ("Campaign 6", "Special cashback offers for Older Customers [46+] years.") ]
    }
        
    selected_campaign = campaign_gender[gender] + campaign_age[age_group]

    return selected_campaign


def predict_gender(device_id):
    x_gender = test_df[test_df["device_id"] == int(device_id)].drop(["device_id", "gender", "age_group", "train_test_flag"],axis=1).iloc[0,:]
    return "Female" if gender_model.predict(x_gender.values.reshape(1, -1))[0] == 0 else "Male"


def predict_age_group(device_id):
    x_gender = test_age_group_df[test_age_group_df["device_id"] == int(device_id)].drop(["device_id", "gender", "age_group", "train_test_flag"],axis=1).iloc[0,:]
    print(age_group_model.predict(x_gender.values.reshape(1, -1)))
    age_group_predicted = age_group_model.predict(x_gender.values.reshape(1, -1))[0]
    return "0-24" if age_group_predicted == 0 else "25-32" if age_group_predicted == 1 else "33-45" if age_group_predicted == 2 else "46+"


def generate_recommendation(device_id):
    gender = predict_gender(device_id)
    age_group = predict_age_group(device_id)

    return {
        'device_id': device_id,
        'gender': gender,
        'age_group': age_group,
        'campaign': select_campaign(gender, age_group)
    }


@app.route("/predict", methods=['POST'])
def predict():
    # Check if the request contains JSON data
    if request.is_json:
        # Get the JSON data from the request
        data = request.json

        # Get the device_id
        device_id = int(data['device_id'])
        # Process the JSON data as needed

        # Return a JSON response
        return jsonify(generate_recommendation(device_id)), 200
    else:
        # If the request does not contain JSON data, return an error response
        return jsonify({'error': 'Request data is not in JSON format'}), 400


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)