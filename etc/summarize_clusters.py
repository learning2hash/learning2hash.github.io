#!/usr/bin/env python3

import json
import argparse
from collections import defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def summarize_by_tags(data, top_n=5):
    """
    Summarize clusters by tag frequency.

    Parameters
    ----------
    data : list[dict]
        List of paper dictionaries with 'cluster' and 'tags' keys.
    top_n : int, default=5
        Number of top tags to include in the summary for each cluster.

    Returns
    -------
    cluster_summary : dict[int, list[dict]]
        A dictionary mapping cluster IDs to lists of dictionaries with 'tag' and 'count' keys.
    """
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

from collections import defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import nltk

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    """
    Lemmatize a given text by tokenizing and lemmatizing each word.

    Parameters
    ----------
    text : str
        The text to lemmatize.

    Returns
    -------
    lemmatized_text : str
        The lemmatized text.
    """
    tokens = word_tokenize(text.lower())
    return " ".join([lemmatizer.lemmatize(token) for token in tokens if token.isalpha()])

def summarize_by_keywords(data, top_n=5, min_idf_diff=0.02):
    """
    Summarize clusters by discriminative lemmatized keywords using TF-IDF.

    Parameters
    ----------
    data : list[dict]
        List of paper dicts with 'cluster' and 'abstract'.
    top_n : int
        Keywords to keep per cluster.
    min_idf_diff : float
        Minimum IDF difference to consider a keyword unique to a cluster.

    Returns
    -------
    cluster_summary : dict[int, list[dict]]
        Mapping of cluster ID -> list of {keyword, score}.
    """
    cluster_texts = defaultdict(list)
    all_docs = []

    for paper in data:
        cluster = paper.get("cluster")
        abstract = paper.get("abstract", "")
        if abstract:
            lemmatized = lemmatize_text(abstract)
            cluster_texts[cluster].append(lemmatized)
            all_docs.append((cluster, lemmatized))

    # Compute global TF-IDF
    documents = [doc for _, doc in all_docs]
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()

    # Map each cluster to its TF-IDF rows
    cluster_indices = defaultdict(list)
    for i, (cluster, _) in enumerate(all_docs):
        cluster_indices[cluster].append(i)

    cluster_summary = {}
    for cluster, indices in cluster_indices.items():
        if not indices:
            cluster_summary[cluster] = [{"tag": "N/A", "count": 0}]
            continue

        # Mean TF-IDF vector for the cluster
        mean_vec = tfidf_matrix[indices].mean(axis=0).A1
        cluster_scores = {feature_names[i]: score for i, score in enumerate(mean_vec)}

        # Mean TF-IDF for other clusters
        other_indices = [i for i in range(tfidf_matrix.shape[0]) if i not in indices]
        other_vec = tfidf_matrix[other_indices].mean(axis=0).A1 if other_indices else [0] * len(feature_names)
        other_scores = {feature_names[i]: score for i, score in enumerate(other_vec)}

        # Rank by how much more a keyword is used in this cluster
        discriminative_scores = []
        for kw in cluster_scores:
            diff = cluster_scores[kw] - other_scores.get(kw, 0)
            if diff > min_idf_diff:
                discriminative_scores.append((kw, diff))

        sorted_discriminative = sorted(discriminative_scores, key=lambda x: x[1], reverse=True)
        cluster_summary[cluster] = [{"tag": kw, "count": round(score, 3)} for kw, score in sorted_discriminative[:top_n]]

    return cluster_summary

def summarize_clusters(input_file, output_file, method='tags', top_n=5):
    """
    Summarize clusters from a JSON file using specified method and save the summary to another JSON file.

    Parameters
    ----------
    input_file : str
        Path to the input JSON file containing clustered data.
    output_file : str
        Path to the output JSON file where the cluster summary will be saved.
    method : str, default='tags'
        Summarization method to use. Options are 'tags' or 'keywords'.
    top_n : int, default=5
        Number of top tags or keywords to include in the summary for each cluster.

    Raises
    ------
    ValueError
        If the provided method is not 'tags' or 'keywords'.

    This function reads a clustered JSON file, summarizes the clusters using either tag frequency
    or TF-IDF keyword analysis, and writes the summary to an output JSON file.
    """

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
