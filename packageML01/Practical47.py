import pickle
#Unpickle the data
fh = open("data.pkl","rb")
areas = pickle.load(fh)
print(type(areas),areas)
fh.close()
