---
    layout: publication
    title: "Algorithms to compute the Burrows-Wheeler Similarity Distribution"
    authors: Louza Felipe A., Telles Guilherme P., Gog Simon, Zhao Liang
    conference: Arxiv
    year: 2019
    bibkey: louza2019algorithms
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1903.10583"}
    tags: ['ARXIV']
    ---
    The Burrows-Wheeler transform (BWT) is a well studied text transformation widely used in data compression and text indexing. The BWT of two strings can also provide similarity measures between them, based on the observation that the more their symbols are intermixed in the transformation, the more the strings are similar. In this article we present two new algorithms to compute similarity measures based on the BWT for string collections. In particular, we present practical and theoretical improvements to the computation of the Burrows-Wheeler similarity distribution for all pairs of strings in a collection. Our algorithms take advantage of the BWT computed for the concatenation of all strings, and use compressed data structures that allow reducing the running time with a small memory footprint, as shown by a set of experiments with real and artificial datasets.