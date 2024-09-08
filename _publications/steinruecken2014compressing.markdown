---
    layout: publication
    title: "Compressing Sets and Multisets of Sequences"
    authors: Steinruecken Christian
    conference: Arxiv
    year: 2014
    bibkey: steinruecken2014compressing
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1401.6410"}
    tags: ['Graph', 'Arxiv', 'TIP']
    ---
    This article describes lossless compression algorithms for multisets of sequences, taking advantage of the multiset's unordered structure. Multisets are a generalisation of sets where members are allowed to occur multiple times. A multiset can be encoded na\"ively by simply storing its elements in some sequential order, but then information is wasted on the ordering. We propose a technique that transforms the multiset into an order-invariant tree representation, and derive an arithmetic code that optimally compresses the tree. Our method achieves compression even if the sequences in the multiset are individually incompressible (such as cryptographic hash sums). The algorithm is demonstrated practically by compressing collections of SHA-1 hash sums, and multisets of arbitrary, individually encodable objects.