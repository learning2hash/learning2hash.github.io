---
    layout: publication
    title: "Fast Compressed Tries through Path Decompositions"
    authors: Grossi Roberto, Ottaviano Giuseppe
    conference: Arxiv
    year: 2011
    bibkey: grossi2011fast
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1111.5220"}
    tags: ['Arxiv', 'Graph']
    ---
    {% raw %}
    Tries are popular data structures for storing a set of strings, where common prefixes are represented by common root-to-node paths. Over fifty years of usage have produced many variants and implementations to overcome some of their limitations. We explore new succinct representations of path-decomposed tries and experimentally evaluate the corresponding reduction in space usage and memory latency, comparing with the state of the art. We study two cases of applications: (1) a compressed dictionary for (compressed) strings, and (2) a monotone minimal perfect hash for strings that preserves their lexicographic order. For (1), we obtain data structures that outperform other state-of-the-art compressed dictionaries in space efficiency, while obtaining predictable query times that are competitive with data structures preferred by the practitioners. In (2), our tries perform several times faster than other trie-based monotone perfect hash functions, while occupying nearly the same space.
    {% endraw %}