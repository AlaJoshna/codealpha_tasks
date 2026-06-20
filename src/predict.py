import pickle

with open("../models/heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("../models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

print("Model Loaded Successfully!")
print("Scaler Loaded Successfully!")

sample_data = [[52, 1, 0, 125, 212, 0, 1, 168, 0, 1.0, 2, 2, 3]]

sample_data = scaler.transform(sample_data)

prediction = model.predict(sample_data)

if prediction[0] == 1:
    print("Heart Disease Risk: YES")
else:
    print("Heart Disease Risk: NO")