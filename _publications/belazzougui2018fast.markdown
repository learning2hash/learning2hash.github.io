---
    layout: publication
    title: "Fast Prefix Search in Little Space, with Applications"
    authors: Belazzougui Djamal, Boldi Paolo, Pagh Rasmus, Vigna Sebastiano
    conference: Arxiv
    year: 2018
    bibkey: belazzougui2018fast
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1804.04720"}
    tags: ['ARXIV']
    ---
    It has been shown in the indexing literature that there is an essential difference between prefix/range searches on the one hand, and predecessor/rank searches on the other hand, in that the former provably allows faster query resolution. Traditionally, prefix search is solved by data structures that are also dictionaries---they actually contain the strings in $S$. For very large collections stored in slow-access memory, we propose much more compact data structures that support \emph{weak} prefix searches---they return the ranks of matching strings provided that \emph{some} string in $S$ starts with the given prefix. In fact, we show that our most space-efficient data structure is asymptotically space-optimal. Previously, data structures such as String B-trees (and more complicated cache-oblivious string data structures) have implicitly supported weak prefix queries, but they all have query time that grows logarithmically with the size of the string collection. In contrast, our data structures are simple, naturally cache-efficient, and have query time that depends only on the length of the prefix, all the way down to constant query time for strings that fit in one machine word. We give several applications of weak prefix searches, including exact prefix counting and approximate counting of tuples matching conjunctive prefix conditions.