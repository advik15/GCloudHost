import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/cluster',methods = ['POST'])
def perform_clustering():
    data = request.get_json()
    latitudes = data.get('latitudes')
    longitudes = data.get('longitudes')

    if not latitudes or not longitudes:
        return jsonify({'error': 'Latitudes and longitudes are required'}), 400

    features = np.array(list(zip(latitudes, longitudes)))

    # Determine the optimal number of clusters using the elbow method
    inertia = []
    k_values = range(2, len(latitudes) + 1)

    for k in k_values:
        kmeans = KMeans(n_clusters=k, init="random", n_init=10, max_iter=300, random_state=42)
        kmeans.fit(features)
        inertia.append(kmeans.inertia_)

    # Find the farthest point to determine the optimal number of clusters
    farthest_point = find_farthest_point(k_values, inertia)

    # Create the K-means model with the optimal k
    kmeans = KMeans(n_clusters=farthest_point[0], init="random", n_init=10, max_iter=300, random_state=42)

    # Perform clustering
    kmeans.fit(features)
    labels = kmeans.labels_

    # Add cluster labels to the data
    data['cluster'] = labels.tolist()

    # Display the dataframe with cluster information
    return jsonify(data), 200

def perpendicular_distance(x1, y1, x2, y2, x, y):
    # Calculate the square of the length of the line segment
    segment_length_squared = (x2 - x1)**2 + (y2 - y1)**2

    if segment_length_squared == 0:
        # If the segment has zero length, return the distance to the start point
        return np.sqrt((x - x1)**2 + (y - y1)**2)

    # Calculate the projection of point (x, y) onto the line
    t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / segment_length_squared

    if t < 0:
        # Closest point is the start point
        return np.sqrt((x - x1)**2 + (y - y1)**2)
    elif t > 1:
        # Closest point is the end point
        return np.sqrt((x - x2)**2 + (y - y2)**2)
    else:
        # Closest point is within the line segment
        closest_x = x1 + t * (x2 - x1)
        closest_y = y1 + t * (y2 - y1)
        return np.sqrt((x - closest_x)**2 + (y - closest_y)**2)

def find_farthest_point(x_coords, y_coords):
    n = len(x_coords)
    if n < 2:
        raise ValueError("At least 2 points are required to find the farthest point.")

    x1, y1 = x_coords[0], y_coords[0]
    x2, y2 = x_coords[-1], y_coords[-1]

    max_distance = -1
    farthest_point = None

    for i in range(1, n - 1):
        x, y = x_coords[i], y_coords[i]
        distance = perpendicular_distance(x1, y1, x2, y2, x, y)

        if distance > max_distance:
            max_distance = distance
            farthest_point = (x, y)

    return farthest_point

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8081, debug=True)