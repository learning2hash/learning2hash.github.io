---
    layout: publication
    title: "A practical index for approximate dictionary matching with few mismatches"
    authors: Cisłak Aleksander, Grabowski Szymon
    conference: Arxiv
    year: 2015
    bibkey: cisłak2015a
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1501.04948"}
    tags: ['Arxiv']
    ---
    {% raw %}
    Approximate dictionary matching is a classic string matching problem (checking if a query string occurs in a collection of strings) with applications in, e.g., spellchecking, online catalogs, geolocation, and web searchers. We present a surprisingly simple solution called a split index, which is based on the Dirichlet principle, for matching a keyword with few mismatches, and experimentally show that it offers competitive space-time tradeoffs. Our implementation in the C++ language is focused mostly on data compaction, which is beneficial for the search speed (e.g., by being cache friendly). We compare our solution with other algorithms and we show that it performs better for the Hamming distance. Query times in the order of 1 microsecond were reported for one mismatch for the dictionary size of a few megabytes on a medium-end PC. We also demonstrate that a basic compression technique consisting in $q$-gram substitution can significantly reduce the index size (up to 50% of the input text size for the DNA), while still keeping the query time relatively low.
    {% endraw %}