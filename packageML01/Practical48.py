import pickle
fh = open("data.pkl","wb")
cities = ["Lucknow","Noida","Delhi","Kanpur"]
students= ("Akshara" , "James","John","Jeet","Alisha")

pickle_object = (students,cities)
pickle.dump(pickle_object,fh)
fh.close()
print("All Students & Cities data saved successfully in pickle.")
