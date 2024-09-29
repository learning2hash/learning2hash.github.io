#!/usr/bin/env python3

import sys
import json
from sklearn.cluster import KMeans

def main(input_file, output_file, n_clusters):
    # Load the t-SNE embeddings
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract embeddings
    embeddings = [d['tsne_embedding'] for d in data]

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(embeddings)
    labels = kmeans.labels_

    # Add cluster labels to data
    for i, d in enumerate(data):
        d['cluster'] = int(labels[i])

    # Save the updated data with cluster labels
    with open(output_file, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python perform_clustering.py <input_tsne_json> <output_clustered_json> <n_clusters>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    n_clusters = int(sys.argv[3])

    main(input_file, output_file, n_clusters)
