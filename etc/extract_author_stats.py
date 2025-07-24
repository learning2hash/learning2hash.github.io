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

    Reads markdown files, extracts metadata, and computes:
      - Paper count, citations, top tags
      - Publication timeline (sparkline data)
      - Author age (last_year - first_year)
      - Co-author relationships and count
      - Louvain communities and betweenness centrality

    Output JSON structure per author:
    {
      "paper_count": int,
      "total_citations": int,
      "tags": [top 5 tags],
      "papers": [{title, year, citations, bibkey}, ...],
      "age": int,
      "coauthors": [list of names],
      "coauthor_count": int,
      "community": int,
      "betweenness": float
    }
    """
    # Initialize stats
    author_stats = defaultdict(lambda: {
        "paper_count": 0,
        "total_citations": 0,
        "tags": Counter(),
        "papers": [],
        "coauthors": set()
    })

    # Read markdown files
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

        # Normalize authors robustly (handle commas, 'and', and whitespace)
        raw_authors = meta.get('authors', '')
        authors = []
        if isinstance(raw_authors, str):
            # replace any ' and ' or ';' with commas, then split
            unified = re.sub(r"\s+and\s+|;", ',', raw_authors)
            for part in unified.split(','):
                name = part.strip()
                if not name:
                    continue
                # collapse internal whitespace to single spaces
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

        title = meta.get('title', 'Unknown Title')
        year = meta.get('year', 'Unknown Year')
        citations = meta.get('citations', 0) or 0
        tags = meta.get('tags', []) or []
        bibkey = meta.get('bibkey', os.path.splitext(filename)[0])

        # Update stats
        for author in authors:
            st = author_stats[author]
            st['paper_count'] += 1
            st['total_citations'] += citations
            st['tags'].update(tags)
            st['papers'].append({
                'title': title,
                'year': year,
                'citations': citations,
                'bibkey': bibkey
            })
        # Track coauthors
        for a in authors:
            for b in authors:
                if a != b:
                    author_stats[a]['coauthors'].add(b)

    # Build global graph
    G = nx.Graph()
    for author, st in author_stats.items():
        G.add_node(author)
        for co in st['coauthors']:
            G.add_edge(author, co)

    # Community & centrality
    partition = community_louvain.best_partition(G)
    bc = nx.betweenness_centrality(G)

    # Finalize output
    out = {}
    for author, st in author_stats.items():
        # Top 5 tags
        tags_top = [t for t, _ in st['tags'].most_common(5)]
        # Age
        yrs = [int(p['year']) for p in st['papers'] if str(p['year']).isdigit()]
        age = max(yrs) - min(yrs) if yrs else 0
        # Coauthors
        co_list = sorted(st['coauthors'])

        out[author] = {
            'paper_count': st['paper_count'],
            'total_citations': st['total_citations'],
            'tags': tags_top,
            'papers': st['papers'],
            'age': age,
            'coauthors': co_list,
            'coauthor_count': len(co_list),
            'community': int(partition.get(author, 0)),
            'betweenness': bc.get(author, 0.0)
        }

    # Write JSON
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, output_filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2)
    print(f"Author stats written to {out_path}")
    return out_path


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--markdown_dir', required=True)
    p.add_argument('--output_dir', default='output')
    p.add_argument('--output_filename', default='author_stats.json')
    args = p.parse_args()
    collate_author_statistics(args.markdown_dir, args.output_dir, args.output_filename)
