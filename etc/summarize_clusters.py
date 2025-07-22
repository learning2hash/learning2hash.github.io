#!/usr/bin/env python3

import json
from collections import defaultdict, Counter

def summarize_tags_by_cluster(input_file="tsne_clustered.json", output_file="cluster_summary.json", top_n=5):
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
    summarize_tags_by_cluster()