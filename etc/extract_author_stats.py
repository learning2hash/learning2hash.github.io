#!/usr/bin/env python3

import os
import yaml
import json
import argparse
from collections import defaultdict, Counter

def collate_author_statistics(markdown_dir, output_dir="output", output_filename="author_stats.json"):
    author_stats = defaultdict(lambda: {
        "paper_count": 0,
        "total_citations": 0,
        "tags": Counter(),
        "papers": []  # List of dicts with title, year, citations, bibkey
    })

    for filename in os.listdir(markdown_dir):
        if not filename.endswith(".markdown") and not filename.endswith(".md"):
            continue

        filepath = os.path.join(markdown_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            continue  # Skip malformed files

        try:
            yaml_part = content.split('---')[1]
            metadata = yaml.safe_load(yaml_part)
        except Exception as e:
            print(f"❌ Error parsing {filename}: {e}")
            continue

        authors = metadata.get("authors", [])
        if isinstance(authors, str):
            authors = [a.strip() for a in authors.split(",")]

        title = metadata.get("title", "Unknown Title")
        year = metadata.get("year", "Unknown Year")
        citations = metadata.get("citations", 0)
        tags = metadata.get("tags", [])
        bibkey = metadata.get("bibkey", os.path.splitext(filename)[0])

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

    # Finalize output
    for author in author_stats:
        # Keep only the top 5 tags
        top_tags = [tag for tag, _ in author_stats[author]["tags"].most_common(5)]
        author_stats[author]["tags"] = top_tags

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