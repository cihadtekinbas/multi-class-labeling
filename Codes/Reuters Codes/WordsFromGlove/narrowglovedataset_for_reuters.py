import shelve
import pygtrie
import numpy as np
import time
from scipy import spatial
from nltk.corpus import reuters

trie = pygtrie.StringTrie()
db = shelve.open("/home/saidaltindis/Desktop/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/shelve_dict")

tag_list = reuters.categories()
print(len(tag_list))

#tag_list = ['earn', 'grain', 'crude', 'trade', 'interest']
tag_dict = {}
error_counter = 0
for key in tag_list:  # <- 1
    try:
        if '-' in key:
            keys = key.split('-')
            try:
                key_1 = np.asarray(db[key[0]], dtype="float64")
                key_2 = np.asarray(db[key[1]], dtype="float64")
                tag_dict[key] = [key_1, key_2]
                trie[key] = [key_1, key_2]
                db.sync()
            except KeyError:
                print("[ERROR] -> Tag \'" + key + '\' is not found in GloVe. Contains (-)' )
        else:
            data = np.asarray(db[key], dtype="float64")
            tag_dict[key] = data  # <- 1
            trie[key] = data
            db.sync()
    except KeyError:
        print("[ERROR] -> Tag \'" + key + '\' is not found in GloVe.' )
        error_counter += 1

print(error_counter)
print("Reading tag finished.")
'''
start_trie = time.time()

counter_earn = 0
counter_grain = 0
counter_crude = 0
counter_trade = 0
counter_interest = 0

for key in db.keys():
    vector = np.asarray(db[key], dtype = "float64")
    if spatial.distance.cosine(vector, tag_dict["earn"]) < 1:
        trie[key] = vector
        counter_earn = counter_earn + 1
    elif spatial.distance.cosine(vector, tag_dict["grain"]) < 1:
        trie[key] = vector
        counter_grain = counter_grain + 1
    elif spatial.distance.cosine(vector, tag_dict["crude"]) < 1:
        trie[key] = vector
        counter_crude = counter_crude + 1
    elif spatial.distance.cosine(vector, tag_dict["trade"]) < 1:
        trie[key] = vector
        counter_trade = counter_trade + 1
    elif spatial.distance.cosine(vector, tag_dict["interest"]) < 1:
        trie[key] = vector
        counter_interest = counter_interest + 1
db.close()

end_trie = time.time()
print("Trie operation is done.")
words = trie.keys()
start_shelve = time.time()
n_db = shelve.open("n_shelve_15_cat_reuters", writeback=True)

for word in words:
    n_db[word] = trie.__getitem__(word)

n_db.close()
end_shelve = time.time()

trie_time = end_trie - start_trie
shelve_time = end_shelve - start_shelve

print("Counter earn: " + str(counter_earn))
print("Counter grain: " + str(counter_grain))
print("Counter crude: " + str(counter_crude))
print("Counter trade: " + str(counter_trade))
print("Counter interest: " + str(counter_interest))

print("Trie length: " + str(trie.__len__()))

print("Time to create trie: " + str(trie_time))
print("Time to write shelve: "+ str(shelve_time))
'''