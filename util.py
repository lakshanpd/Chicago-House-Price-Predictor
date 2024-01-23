import pickle

__model = None

def load_saved_artifacts():
    global __model
    with open('E:\My Projects\Chicago Home Price Predictor\Server/artifacts/Chicago_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

def predict_price(Bedroom, Space, Room, Bathroom, Garage, Condition):
    return __model.predict([[Bedroom, Space, Room, Bathroom, Garage, Condition]])[0]