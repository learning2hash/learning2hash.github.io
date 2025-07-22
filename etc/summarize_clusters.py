#!/usr/bin/env python3

import json
import argparse
from collections import defaultdict, Counter

def summarize_tags_by_cluster(input_file, output_file, top_n=5):
    """
    Summarize top tags for each t-SNE cluster from a JSON file.

    Parameters
    ----------
    input_file : str
        Path to the input JSON file containing t-SNE embeddings and tags.
    output_file : str
        Path to the output JSON file where the cluster summary will be saved.
    top_n : int, optional
        Number of top tags to include per cluster. Defaults to 5.

    Notes
    -----
    The cluster summary is a dictionary with cluster IDs as keys and a list of
    top tags as values, where each tag is represented as a dictionary with keys
    "tag" and "count".

    Example
    -------
    >>> summarize_tags_by_cluster("tsne_clustered.json", "cluster_summary.json")
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Aggregate tags by cluster
    cluster_tags = defaultdict(list)
    for paper in data:
        cluster = paper.get("cluster")
        tags = paper.get("tags", [])
        cluster_tags[cluster].extend(tags)

    # Summarize top tags
    cluster_summary = {}
    for cluster, tags in cluster_tags.items():
        tag_counts = Counter(tags)
        top_tags = tag_counts.most_common(top_n)
        cluster_summary[cluster] = [{"tag": tag, "count": count} for tag, count in top_tags]

    # Save summary
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cluster_summary, f, indent=2)

    print(f"✅ Cluster summary saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize top tags for each t-SNE cluster.")
    parser.add_argument("input_file", help="Path to the input clustered JSON file (e.g., tsne_clustered.json)")
    parser.add_argument("output_file", help="Path to the output cluster summary JSON file (e.g., cluster_summary.json)")
    parser.add_argument("--top_n", type=int, default=5, help="Number of top tags to include per cluster (default: 5)")
    args = parser.parse_args()

    summarize_tags_by_cluster(args.input_file, args.output_file, args.top_n)