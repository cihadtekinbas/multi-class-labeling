from scipy import spatial
import sys
import heapq_max
import heapq
import time
import pygtrie
import scipy.io as io
import numpy as np
from scipy.cluster.vq import kmeans2
import shelve
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from pylab import rcParams
from sklearn.manifold import TSNE

rcParams['figure.figsize'] = 15, 10


def return_matrix(random_words, dim=300):
    word_matrix = np.random.randn(len(random_words), dim)
    i = 0
    for word in random_words:
        word_matrix[i] = trie[word]
        i += 1
    return word_matrix


trie = pygtrie.StringTrie()
db = shelve.open("n_shelve_8_cat")

tags =["education", "film", "food", "music","health","police","women","children"]

tag_dict = {}
print(1)
for value in tags:  # <- 1
    data = np.asarray(db[value], dtype="float64")
    tag_dict[value] = data  # <- 1
    db.sync()
print(2)
tm = db.keys()
print(3)
data = []
count = 0
for x in tm:
    trie[x] = np.asarray(db[x], dtype="float64")
    # count+=1
    # if count==1000:
    #     break
    # Variable göre average al.
    # data.append(db[x])
print(4)


def midpoint(list):
    mid1 = np.arange(300)
    for t in range(300):  # temp array
        mid1[t] = 0
    mid = np.asarray(mid1, dtype="float64")
    for e in list:  # listedeki her elamnı temp arraye ekle
        for p in range(300):
            mid[p] = mid[p]+e[p]
    for p in range(300):
        mid[p] = mid[p]/len(list)  # her elemanı böl ortayı bul

    return mid


closest_points_list = {}  # eklenen noktaları tut
for j in tag_dict:
    closest_points_list[j] = []
    closest_points_list[j].append(tag_dict[j])
# sadece kulanacağın orta noktaları tut her dönüşte bir tanesini güncelle
mid_points_list = {}

for j in tag_dict:
    mid_points_list[j] = tag_dict[j]
name_list = {}  # eklenen kelimeleri ismini tut
for i in tag_dict:
    name_list[i] = []
    name_list[i].append(i)
min_list = {}  # temp min list
for j in tag_dict:
    min_list[j] = []
start = time.time()
count = 0
run = 1
heap_list={}

found_name=""
for j in tag_dict:
    heap_list[j] = []
while run == 1:
    startt = time.time()
    # for j in tag_dict:
    #     min_list[j] = []
    for x in trie:
        count += 1
        if found_name=="":
            for i in tag_dict:
                if x not in name_list[i]:
                    # try:
                    result = spatial.distance.cosine(trie[x], mid_points_list[i])

                    # except  :
                    # print(closest_points_list[i])
                    heapq_max.heappush_max(min_list[i], (result, trie[x], x, i))
                    # pushes a new item on the heap
                    if len(min_list[i]) > 1:
                        heapq_max.heappop_max(min_list[i])
                    heapq_max.heappush_max(heap_list[i],(result,x))

                    if len(heap_list[i])>40:
                        heapq_max.heappop_max(heap_list[i])
                    # if result < min_list[i]:
                    #     min_list[i]=result
        else:
            if x not in name_list[found_name]:
                    # try:
                    result = spatial.distance.cosine(trie[x], mid_points_list[found_name])

                    # except  :
                    # print(closest_points_list[i])
                    heapq_max.heappush_max(min_list[found_name], (result, trie[x], x, found_name))
                    # pushes a new item on the heap
                    if len(min_list[found_name]) > 1:
                        heapq_max.heappop_max(min_list[found_name])
                    heapq_max.heappush_max(heap_list[found_name],(result,x))

                    if len(heap_list[found_name])>40:
                        heapq_max.heappop_max(heap_list[found_name])
                    # if result < min_list[i]:
                    #     min_list[i]=result

    # print(fg,min_list)
    onemin = []
    for df in min_list:
        onemin.append(min_list[df])

    heapq.heapify(onemin)
    # print(onemin)
    z = heapq.heappop(onemin)
    s, d, f, g = heapq_max.heappop_max(z)
    found_name=g
    min_list[g]=[]
    name_list[g].append(f)
    closest_points_list[g].append(d)
    mid_points_list[g] = midpoint(closest_points_list[g])
    endd = time.time()
    flag=1
    for name in name_list:
        if len(name_list[name])<40:
            flag=0
    if flag==1:
        run=0
    print(endd-startt)

    # print(f,g)
    # sys.exit()
    # for df in min_list:
    #     x,y,z,g=heapq_max.heappop_max(min_list[df])
    #     name_list[df].append(z)
    #     closest_points_list[df].append(y)
    #     mid_points_list[df]=midpoint(closest_points_list[df])
    #     # sys.exit()

for gh in name_list:
    print(name_list[gh])


end = time.time()
for na in heap_list:
    print(heap_list[na])
sys.exit()
print(count)
print(name_list['film'])
random_words = []
random_words.append('film')
for x in name_list['film']:
    random_words.append(x[2])
    # print(name_list[x])


# random_words = ['man','woman','king','queen','microwave','baby','boy','girl','pizza','royal','mother','father','doctor','cook','throne']
return_matrix_ = return_matrix(random_words)
pca_ = PCA(n_components=2)
viz_data = pca_.fit_transform(return_matrix_)
for ct in range(len(random_words)):
    if random_words[ct] != 'film':
        random_words[ct] = ''

plt.scatter(viz_data[:, 0], viz_data[:, 1], cmap=plt.get_cmap('Spectral'))
for label, x, y in zip(random_words, viz_data[:, 0], viz_data[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        xytext=(-14, 14),
        textcoords='offset points',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
    )
plt.xlabel('PCA Component 1 ')
plt.ylabel('PCA Component 2')
plt.title('PCA representation for Word Embedding')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()

tsne = TSNE(n_components=2, verbose=1, perplexity=3, method='exact')
tsne_results = tsne.fit_transform(return_matrix_)
plt.scatter(tsne_results[:, 0], tsne_results[:, 1],
            cmap=plt.get_cmap('Spectral'))
for label, x, y in zip(random_words, tsne_results[:, 0], tsne_results[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        xytext=(-14, 14),
        textcoords='offset points',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
    )
plt.xlabel('TSNE Component 1 ')
plt.ylabel('TSNE Component 2')
plt.title('TSNE representation for Word Embedding')
plt.show()

print(min_list)

print(end - start)

# # Convert dictionary to numpy array.
# list_of_values = list(tag_dict.values())
# centroids = np.asarray(list_of_values, dtype = "float64")
# data = np.asarray(data, dtype = "float64")

# # Do agglomerative clustering.
# km, label = kmeans2(data,centroids,iter = 3,minit = "matrix")

# print(label[0:10000:500])
