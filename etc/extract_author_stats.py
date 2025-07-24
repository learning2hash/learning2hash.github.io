#!/usr/bin/env python3

import os
import yaml
import json
import argparse
from collections import defaultdict, Counter
import networkx as nx
from community import community_louvain


def collate_author_statistics(markdown_dir, output_dir="output", output_filename="author_stats.json"):
    # Initial collection of per-author stats
    author_stats = defaultdict(lambda: {
        "paper_count": 0,
        "total_citations": 0,
        "tags": Counter(),
        "papers": [],               # List of dicts with title, year, citations, bibkey
        "coauthors": set()          # Temporary set of distinct co-authors
    })

    # Scan markdown files
    for filename in os.listdir(markdown_dir):
        if not (filename.endswith(".markdown") or filename.endswith(".md")):
            continue

        filepath = os.path.join(markdown_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            continue

        try:
            yaml_part = content.split('---')[1]
            metadata = yaml.safe_load(yaml_part)
        except Exception as e:
            print(f"❌ Error parsing {filename}: {e}")
            continue

        # Normalize authors into list
        authors = metadata.get("authors", [])
        if isinstance(authors, str):
            authors = [a.strip() for a in authors.split(",") if a.strip()]

        title = metadata.get("title", "Unknown Title")
        year = metadata.get("year", "Unknown Year")
        citations = metadata.get("citations", 0) or 0
        tags = metadata.get("tags", []) or []
        bibkey = metadata.get("bibkey", os.path.splitext(filename)[0])

        # Update stats
        for author in authors:
            stat = author_stats[author]
            stat["paper_count"] += 1
            stat["total_citations"] += citations
            stat["tags"].update(tags)
            stat["papers"].append({
                "title": title,
                "year": year,
                "citations": citations,
                "bibkey": bibkey
            })

        # Build co-author relationships
        for author in authors:
            for coauthor in authors:
                if coauthor != author:
                    author_stats[author]["coauthors"].add(coauthor)

    # Build full co-author graph
    G = nx.Graph()
    for author, stat in author_stats.items():
        G.add_node(author)
        for co in stat["coauthors"]:
            G.add_edge(author, co)

    # Compute communities via Louvain
    partition = community_louvain.best_partition(G)
    # Compute betweenness centrality
    bc = nx.betweenness_centrality(G)

    # Finalize output
    for author, stat in author_stats.items():
        # Top 5 tags
        stat["tags"] = [tag for tag, _ in stat["tags"].most_common(5)]

        # Compute age
        years = []
        for p in stat["papers"]:
            try:
                y = int(p.get("year", 0))
                years.append(y)
            except:
                continue
        stat["age"] = max(years) - min(years) if years else 0

        # Co-author list and count
        co_list = sorted(stat["coauthors"])
        stat["coauthors"] = co_list
        stat["coauthor_count"] = len(co_list)

        # Add community and betweenness
        stat["community"] = int(partition.get(author, 0))
        stat["betweenness"] = bc.get(author, 0.0)

    # Write JSON
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(author_stats, f, indent=2)

    print(f"✅ Author stats saved to {output_path}")
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract author statistics from markdown files.")
    parser.add_argument("--markdown_dir", required=True, help="Path to directory containing markdown files.")
    parser.add_argument("--output_dir", default="output", help="Directory to write the output JSON.")
    parser.add_argument("--output_filename", default="author_stats.json", help="Name of the output JSON file.")

    args = parser.parse_args()
    collate_author_statistics(args.markdown_dir, args.output_dir, args.output_filename)
