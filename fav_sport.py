# -*- coding: utf-8 -*-
from collections import Counter
import matplotlib.pyplot as plt
import math


def vector_subtract(v,w):
    return [v_i - w_i
            for v_i, w_i in zip(v,w)]

def dot(v,w):
    return sum(v_i*w_i
               for v_i, w_i in zip(v,w))
    
def sum_of_squares(v):
    return dot(v,v)

def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    #most_common(n) will return the Top n of the list
    winner, winner_count = vote_counts.most_common()[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1])


def knn_classify(k, labeled_points, new_point):
    #each labeled point is a pair (point, label)
    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)


states = [(74.2179,27.0238,'Kabbadi'),(75.7139,15.3173,'Kabbadi'),(76.0856,29.0588,'Kabbadi'),(79.0193,18.1124,'Kabbadi'),(80.9462,26.8467,'Kabbadi'),(85.3131,25.0961,'Kabbadi'),(79.0193,30.0668,'Kabbadi'),(77.1734,31.1048,'Kabbadi'),
          (76.2711,10.8505,'Football'),(74.1240,15.2993,'Football'),(85.0985,20.9517,'Football'),(79.7400,15.9129,'Football'),(87.8550,22.9868,'Football'),(93.9063,24.6637,'Football'),(91.9882,23.9048,'Football'),(91.3662,25.4670,'Football'),(92.9376,23.1645,'Football'),
          (68.03215,23.71307,'Cricket'),(76.845245,35.674520,'Cricket'),(75.7139,19.7515,'Cricket'),(78.6569,22.9734,'Cricket'),(75.3412,31.1471,'Cricket'),(77.5385,8.0883,'Cricket'),(81.8661,21.2787,'Cricket'),(85.2799,23.6102,'Cricket'),(92.9376,26.2006,'Cricket'),(94.5624,26.1584,'Cricket'),(88.5122,27.5330,'Cricket'),(94.7278,28.2180,'Cricket')]
          
         
states = [([latitude, longitude], sport) for latitude, longitude, sport in states]

#driver code for testing k-means **START**
# try several different values for k
for k in [1,3,5,7]:
    num_correct = 0

    for location, actual_sport in states:

        other_cities = [other_city
                        for other_city in states
                        if other_city != (location, actual_sport)]

        predicted_sport = knn_classify(k, other_cities, location)

        if predicted_sport == actual_sport:
            num_correct += 1

    print(k, "neighbor[s]:", num_correct, "correct out of", len(states))
        
#driver code for testing k-means **END**




def plot_state_borders(plt, color='0.8'):
    pass

def plot_cities():

    # key is language, value is pair (longitudes, latitudes)
    plots = { "Cricket" : ([], []), "Football" : ([], []), "Kabbadi" : ([], []) }

    # we want each language to have a different marker and color
    markers = { "Cricket" : "o", "Football" : "s", "Kabbadi" : "^" }
    colors  = { "Cricket" : "r", "Football" : "b", "Kabbadi" : "g" }

    for (latitude, longitude), sport in states:
        plots[sport][0].append(latitude)
        plots[sport][1].append(longitude)

    # create a scatter series for each language
    for sport, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[sport], marker=markers[sport],
                          label=sport, zorder=10)
    plot_state_borders(plt)    # assume we have a function that does this
    plt.legend(loc=0)          # let matplotlib choose the location
    plt.axis([60,105,0,40]) # set the axes
    plt.title("Favoured Sports")
    plt.show()

def classify_and_plot_grid(k=1):
    plots = { "Cricket" : ([], []), "Football" : ([], []), "Kabbadi" : ([], []) }
    markers = { "Cricket" : "o", "Football" : "s", "Kabbadi" : "^" }
    colors  = { "Cricket" : "r", "Football" : "b", "Kabbadi" : "g" }

    for longitude in range(8, 35):
        for latitude in range(70, 95):
            predicted_language = knn_classify(k, states, [latitude, longitude])
            plots[predicted_language][0].append(longitude)
            plots[predicted_language][1].append(latitude)

    # create a scatter series for each language
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=0)

    plot_state_borders(plt, color='black')    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location
    plt.axis([8,35,70,95]) # set the axes
    plt.title(str(k) + "-Nearest Neighbor Favourite Sports")
    plt.show()
    
    
plot_cities()
classify_and_plot_grid()