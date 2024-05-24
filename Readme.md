# Ad Campaign Recommender
# Capstone 1 - Surbhi Sinha

This is a submission for capstone project where we have a telecom data set comprising of events, location & app meta data. Based on this data set we need to create machine learning model to predict age and gender of user. We will use this prediction to to recommend different ad campaign to the user.

We have two scenarios using which we have created our model for this prediction:
1. Scenario 1: In this case we will use the event data of users as well as their location
2. Scenario 2: In this case we will only use the app, metadata etc.


## How to run

1. Create a folder named `data` and download these datasets to the given folder:
    - https://uoacapstone.s3.amazonaws.com/app_events.csv
    - https://uoacapstone.s3.amazonaws.com/train_event_data.csv
    - https://uoacapstone.s3.amazonaws.com/app_events_meta_data.csv
    - https://uoacapstone.s3.amazonaws.com/train_mobile_brand.csv
    - https://cdn.upgrad.com/uploads/production/29360be3-ae2f-4dc3-840b-e0e679203abb/train_test_split.csv

2. Next We need to run the python notebooks in these order:
    - eda_data_preparation.ipynb : This notebook is doing the complete EDA , Data Cleaning and Data Set preparation
    - model_building.ipynb :  This notebook is being used for model creation, evaluation for Scenario 1 & Scenario 2

3. Copy the models generated into the flask app folder `cp -r models/ recommender_app/models`

4. Now run the flask application using docker. 
    - [Install Docker](https://docs.docker.com/engine/install/)
    - `docker build -t <image_name> .`
    - `docker run -p [PORT]:[PORT] <image_name>`