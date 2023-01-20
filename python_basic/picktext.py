import pickle

mymovie = {"호텔 도로나": "100", "호텔 메로나": "90"}
pickle.dump(mymovie,open("text.txt", "wb"))

mymovie = pickle.load(open("text.txt", "rb"))
print(mymovie)