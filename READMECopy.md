# KMeans-Predictive-Modeling
K-Means Clustering is a Machine Learning Algorithm which creates a model based on the nearest-neighbour-choice. </br>
The model in this repository has been implemented by k-means classification which predics the favourite sport in a state(in India).</br>
This is a duplicate readme just to test the repo's pull requests. </br>


### Explanation
**util_methods.py** - Contains the linear algebra methods that are used in the k-means model. </br></br>
**fav_sport.py** - Run this file to get output of the model. It contains the following methods:
* *major_cluster(labels)* : Takes a list of input variables as parameter and returns a winner with most number of occurences.
* *knn_classify(k, labeled_points, new_point)* : Driver algorithm which creates cluster based on the value of k.
* *plot_cities()* : Plots the cities based on (latitude and longitude) with the appropriate markers of favourite sport.
* *classify_and_plot_grid()* : Plots the graph of k-means clustering model!


### Use
An attempt to make the code as readable as possible has been made. <br>
You can modify the code to create your own k-means classification.</br>
**e.g.** Instead of *states*(a list used in the *fav_sport.py* file), you can use languages which people speak throughout the world.</br>
Feel free to reach out for any suggestions or help!


#### Inspiration
Joel Grus and his book: Data Science from Scratch
