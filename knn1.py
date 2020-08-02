import math

data_set = [
    (2,9,8,4, "Good"),
    (3,7,7,9, "Bad"),
    (10,3,10,3, "Good"),
    (2,9,6,10, "Good"),
    (3,3,2,5, "Bad"),
    (2,8,5,6, "Bad"),
    (7,2,3,10, "Good"),
    (1,10,8,10, "Bad"),
    (2,8,1,10, "Good"),
]

A = (3,2,1,5)
B = (8,3,1,2)
C = (6,10,8,3)
D = (9,6,4,1)

def calc_distance(datas, test):
    distances = []
    for data in datas:
        distances.append(
            ( round(math.sqrt(((data[0] - test[0])**2 + (data[1] - test[1])**2 + (data[2] - test[2])**2 + (data[3] - test[3])**2)), 3), data[4] ))
    return distances

def most_frequent(list1):
    return max(set(list1), key = list1.count)

def get_neighbours(distances, k):
    labels = []
    distances.sort()
    print(distances[:k])
    for distance in distances[:k]:
        labels.append(distance[1])
    print("It can be classified as: ", end="")
    print(most_frequent(labels))


distances = calc_distance(data_set,D)
get_neighbours(distances, 7)

distances = calc_distance(data_set,D)
get_neighbours(distances, 7) 