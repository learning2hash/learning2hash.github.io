#!/usr/bin/env python3

import json
import argparse
from collections import defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def summarize_by_tags(data, top_n=5):
    cluster_tags = defaultdict(list)
    for paper in data:
        cluster = paper.get("cluster")
        tags = paper.get("tags", [])
        cluster_tags[cluster].extend(tags)

    cluster_summary = {}
    for cluster, tags in cluster_tags.items():
        tag_counts = Counter(tags)
        top_tags = tag_counts.most_common(top_n)
        cluster_summary[cluster] = [{"tag": tag, "count": count} for tag, count in top_tags]

    return cluster_summary

def summarize_by_keywords(data, top_n=5):
    """
    Summarize clusters by keywords using TF-IDF analysis of abstracts.

    Parameters
    ----------
    data : list[dict]
        List of paper dictionaries with 'cluster', 'abstract' keys.
    top_n : int, default=5
        Number of top keywords to include in the summary for each cluster.

    Returns
    -------
    cluster_summary : dict[int, list[dict]]
        A dictionary mapping cluster IDs to lists of dictionaries with 'keyword' and 'score' keys.
    """
    cluster_texts = defaultdict(list)
    for paper in data:
        cluster = paper.get("cluster")
        abstract = paper.get("abstract", "")
        if abstract:  # Only use papers with abstracts
            cluster_texts[cluster].append(abstract)

    cluster_summary = {}
    for cluster, abstracts in cluster_texts.items():
        if not abstracts:
            cluster_summary[cluster] = [{"keyword": "N/A", "score": 0}]
            continue

        corpus = [" ".join(abstracts)]
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        tfidf_matrix = vectorizer.fit_transform(corpus)
        scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        cluster_summary[cluster] = [{"keyword": kw, "score": round(score, 3)} for kw, score in sorted_scores[:top_n]]

    return cluster_summary

def summarize_clusters(input_file, output_file, method='tags', top_n=5):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if method == 'tags':
        summary = summarize_by_tags(data, top_n=top_n)
    elif method == 'keywords':
        summary = summarize_by_keywords(data, top_n=top_n)
    else:
        raise ValueError(f"Unknown method '{method}'. Use 'tags' or 'keywords'.")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"✅ Cluster summary saved to {output_file} using method: {method}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize clusters using tags or TF-IDF keywords.")
    parser.add_argument("input_file", help="Path to the input clustered JSON file (e.g., tsne_clustered.json)")
    parser.add_argument("output_file", help="Path to the output cluster summary JSON file (e.g., cluster_summary.json)")
    parser.add_argument("--top_n", type=int, default=5, help="Number of top tags or keywords per cluster (default: 5)")
    parser.add_argument("--method", choices=["tags", "keywords"], default="keywords",
                        help="Summarization method: 'tags' (default) or 'keywords'")
    args = parser.parse_args()

    summarize_clusters(args.input_file, args.output_file, method=args.method, top_n=args.top_n)
