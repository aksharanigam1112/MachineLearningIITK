import pickle

#Pickle the data
cities = ("Lucknow","Noida","Delhi","Kanpur")
fh = open("data.pkl","wb")                  #Creates binary file
pickle.dump(cities,fh)
fh.close()
print("All cities data saved successfully in pickle.")

# To save the data along with the format(data structure) is called pickling
# and to retrieve back with the data structure is called unpickling
