#!/usr/bin/env python3

import os
import re
import yaml
import json
import argparse
from collections import defaultdict, Counter
import networkx as nx
from community import community_louvain


def collate_author_statistics(markdown_dir, output_dir="output", output_filename="author_stats.json"):
    """
    Collate author statistics from markdown files in a directory.

    Optimized to reduce file size:
    - Replaces bibkeys with titles in paper lists
    - Keeps only top 10 cited papers per author
    - Rounds float stats
    - Truncates coauthor lists
    """
    author_stats = defaultdict(lambda: {
        "paper_count": 0,
        "total_citations": 0,
        "tags": Counter(),
        "papers": [],
        "coauthors": set()
    })

    for filename in os.listdir(markdown_dir):
        if not filename.endswith(('.markdown', '.md')):
            continue
        path = os.path.join(markdown_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            continue
        try:
            yaml_part = content.split('---', 2)[1]
            meta = yaml.safe_load(yaml_part)
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            continue

        raw_authors = meta.get('authors', '')
        authors = []
        if isinstance(raw_authors, str):
            unified = re.sub(r"\s+and\s+|;", ',', raw_authors)
            for part in unified.split(','):
                name = part.strip()
                if not name:
                    continue
                name = re.sub(r"\s+", ' ', name)
                authors.append(name)
        elif isinstance(raw_authors, list):
            for part in raw_authors:
                if not isinstance(part, str):
                    continue
                name = part.strip()
                if not name:
                    continue
                name = re.sub(r"\s+", ' ', name)
                authors.append(name)

        year = meta.get('year', 'Unknown Year')
        citations = meta.get('citations', 0) or 0
        tags = meta.get('tags', []) or []
        title = meta.get('title', os.path.splitext(filename)[0])

        for author in authors:
            st = author_stats[author]
            st['paper_count'] += 1
            st['total_citations'] += citations
            st['tags'].update(tags)
            st['papers'].append({
                'year': year,
                'citations': citations,
                'title': title
            })
        for a in authors:
            for b in authors:
                if a != b:
                    author_stats[a]['coauthors'].add(b)

    filtered_authors = {
        name for name, stats in author_stats.items()
        if not (stats['total_citations'] < 50)
    }

    G = nx.Graph()
    for author in filtered_authors:
        G.add_node(author)
        for co in author_stats[author]['coauthors']:
            if co in filtered_authors:
                G.add_edge(author, co)

    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    if G.number_of_nodes() == 0:
        print("⚠️ No valid graph authors found.")
        partition = {}
        bc = {}
        degree = {}
        closeness = {}
        clustering = {}
    else:
        partition = community_louvain.best_partition(G)
        bc = nx.betweenness_centrality(G, k=100)
        degree = dict(G.degree())
        closeness = nx.closeness_centrality(G)
        clustering = nx.clustering(G)

    out = {}
    for author, st in author_stats.items():
        if st['paper_count'] == 1 and st['total_citations'] < 50:
            continue

        tags_top = [t for t, _ in st['tags'].most_common(5)]
        yrs = [int(p['year']) for p in st['papers'] if str(p['year']).isdigit()]
        age = max(yrs) - min(yrs) if yrs else 0
        co_list = sorted(
            co for co in st['coauthors'] if co in filtered_authors
        )[:20]  # Limit coauthors

        top_papers = sorted(st['papers'], key=lambda p: p['citations'], reverse=True)[:10]
        paper_refs = [{'title': p['title'], 'citations': p['citations'], 'year': p['year']} for p in top_papers]

        out[author] = {
            'paper_count': st['paper_count'],
            'total_citations': st['total_citations'],
            'tags': tags_top,
            'papers': paper_refs,
            'age': age,
            'coauthors': co_list,
            'coauthor_count': len(co_list),
            'community': int(partition.get(author, 0)),
            'betweenness': round(bc.get(author, 0.0), 3),
            'degree': degree.get(author, 0),
            'closeness': round(closeness.get(author, 0.0), 3),
            'clustering': round(clustering.get(author, 0.0), 3)
        }

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, output_filename)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=0)
    print(f"Author stats written to {out_path}")
    return out_path


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--markdown_dir', required=True)
    p.add_argument('--output_dir', default='output')
    p.add_argument('--output_filename', default='author_stats.json')
    args = p.parse_args()
    collate_author_statistics(args.markdown_dir, args.output_dir, args.output_filename)