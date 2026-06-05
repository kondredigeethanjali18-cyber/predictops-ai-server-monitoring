import pickle

model = pickle.load(open("random_forest_model.pkl", "rb"))

result = model.predict([[100, 40000, 98, 3000, 120, 50, 10, 50, 180]]
)
print(result)

