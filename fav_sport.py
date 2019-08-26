# -*- coding: utf-8 -*-
from collections import Counter
import matplotlib.pyplot as plt
from util_methods import distance



def major_cluster(labels):
    no_of_elements = Counter(labels)
    winner, winner_count = no_of_elements.most_common()[0]
    num_winners = len([count
                       for count in no_of_elements.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return major_cluster(labels[:-1])


def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))

    k_nearest_labels = [label for _, label in by_distance[:k]]

    return major_cluster(k_nearest_labels)


states = [(74.2179,27.0238,'Kabbadi'),(75.7139,15.3173,'Kabbadi'),(76.0856,29.0588,'Kabbadi'),(79.0193,18.1124,'Kabbadi'),(80.9462,26.8467,'Kabbadi'),(85.3131,25.0961,'Kabbadi'),(79.0193,30.0668,'Kabbadi'),(77.1734,31.1048,'Kabbadi'),
          (76.2711,10.8505,'Football'),(74.1240,15.2993,'Football'),(85.0985,20.9517,'Football'),(79.7400,15.9129,'Football'),(87.8550,22.9868,'Football'),(93.9063,24.6637,'Football'),(91.9882,23.9048,'Football'),(91.3662,25.4670,'Football'),(92.9376,23.1645,'Football'),
          (68.03215,23.71307,'Cricket'),(76.845245,35.674520,'Cricket'),(75.7139,19.7515,'Cricket'),(78.6569,22.9734,'Cricket'),(75.3412,31.1471,'Cricket'),(77.5385,8.0883,'Cricket'),(81.8661,21.2787,'Cricket'),(85.2799,23.6102,'Cricket'),(92.9376,26.2006,'Cricket'),(94.5624,26.1584,'Cricket'),(88.5122,27.5330,'Cricket'),(94.7278,28.2180,'Cricket')]
states = [([latitude, longitude], sport) for latitude, longitude, sport in states]

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


def plot_state_borders(plt, color='0.8'):
    pass

def plot_cities():
    plots = { "Cricket" : ([], []), "Football" : ([], []), "Kabbadi" : ([], []) }
    markers = { "Cricket" : "o", "Football" : "s", "Kabbadi" : "^" }
    colors  = { "Cricket" : "r", "Football" : "b", "Kabbadi" : "g" }

    for (latitude, longitude), sport in states:
        plots[sport][0].append(latitude)
        plots[sport][1].append(longitude)

    for sport, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[sport], marker=markers[sport],
                          label=sport, zorder=10)
    plot_state_borders(plt)
    plt.legend(loc=0)
    plt.axis([60,105,0,40])
    plt.title("Favoured Sports")
    plt.show()

def classify_and_plot_grid(k=1):
    plots = { "Cricket" : ([], []), "Football" : ([], []), "Kabbadi" : ([], []) }
    markers = { "Cricket" : "o", "Football" : "s", "Kabbadi" : "^" }
    colors  = { "Cricket" : "r", "Football" : "b", "Kabbadi" : "g" }

    for latitude in range(60,105):
        for longitude in range(0,40):
            predicted_sport = knn_classify(k, states, [latitude, longitude])
            plots[predicted_sport][0].append(latitude)
            plots[predicted_sport][1].append(longitude)

    for sport, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[sport], marker=markers[sport],
                          label=sport, zorder=0)
    plot_state_borders(plt, color='black')
    
    plt.legend(loc=0)
    plt.axis([60,105,0,40])
    plt.title(str(k) + "-Nearest Neighbor Favourite Sports")
    plt.show()
    
    
plot_cities()
classify_and_plot_grid()