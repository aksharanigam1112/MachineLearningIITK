import pickle
fh = open("data.pkl","rb")

(s,c) = pickle.load(fh)
print(s,"\n\n",c)
fh.close()