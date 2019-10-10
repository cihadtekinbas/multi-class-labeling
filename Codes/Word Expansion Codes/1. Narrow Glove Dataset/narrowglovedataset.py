import shelve
import pygtrie
import numpy as np
import time
from scipy import spatial

trie = pygtrie.StringTrie()
db = shelve.open("shelve_dict")

tag_list = ["education", "music", "film", "food","police","health","women","children","technology","sport"]
tag_dict = {}

for key in tag_list:  # <- 1
    data = np.asarray(db[key], dtype="float64")
    tag_dict[key] = data  # <- 1
    trie[key] = data
    db.sync()


print("Reading tag finished.")
start_trie = time.time()

counter_edu = 0
counter_health = 0
counter_food = 0
counter_film = 0
counter_children = 0
counter_music = 0
counter_police = 0
counter_women = 0
counter_technology=0
counter_sport=0
for key in db.keys():
    vector = np.asarray(db[key], dtype = "float64")
    if spatial.distance.cosine(vector, tag_dict["education"]) < 1:
        trie[key] = vector
        counter_edu = counter_edu + 1
    elif spatial.distance.cosine(vector, tag_dict["film"]) < 1:
        trie[key] = vector
        counter_film = counter_film + 1
    elif spatial.distance.cosine(vector, tag_dict["food"]) < 1:
        trie[key] = vector
        counter_food = counter_food + 1
    elif spatial.distance.cosine(vector, tag_dict["music"]) < 1:
        trie[key] = vector
        counter_music = counter_music + 1
    elif spatial.distance.cosine(vector, tag_dict["health"]) < 1:
        trie[key] = vector
        counter_health = counter_health + 1
    elif spatial.distance.cosine(vector, tag_dict["police"]) < 1:
        trie[key] = vector
        counter_police = counter_police + 1
    elif spatial.distance.cosine(vector, tag_dict["women"]) < 1:
        trie[key] = vector
        counter_women = counter_women + 1
    elif spatial.distance.cosine(vector, tag_dict["children"]) < 1:
        trie[key] = vector
        counter_children = counter_children + 1
    elif spatial.distance.cosine(vector, tag_dict["technology"]) < 1:
        trie[key] = vector
        counter_technology = counter_technology + 1
    elif spatial.distance.cosine(vector, tag_dict["sport"]) < 1:
        trie[key] = vector
        counter_sport = counter_sport + 1
db.close()

end_trie = time.time()
print("Trie operation is done.")
words = trie.keys()
start_shelve = time.time()
n_db = shelve.open("n_shelve_10_cat", writeback=True)

for word in words:
    n_db[word] = trie.__getitem__(word)

n_db.close()
end_shelve = time.time()

trie_time = end_trie - start_trie
shelve_time = end_shelve - start_shelve

print("Counter Edu: " + str(counter_edu))
print("Counter Film: " + str(counter_film))
print("Counter Food: " + str(counter_food))
print("Counter Music: " + str(counter_music))
print("Counter Health: " + str(counter_health))
print("Counter Police: " + str(counter_police))
print("Counter Children: " + str(counter_children))
print("Counter Women: " + str(counter_women))
print("Counter Technology: " + str(counter_technology))
print("Counter Sport: " + str(counter_sport))

print("Trie length: " + str(trie.__len__()))

print("Time to create trie: " + str(trie_time))
print("Time to write shelve: "+ str(shelve_time))
