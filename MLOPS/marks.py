import joblib
model = joblib.load("marks.pk1")
while True:
    inp  = input("\nEnter no of study hours : ")
    print()
    print(f"\nMarks you may score : {model.predict([[inp]])}")
    

