---
    layout: publication
    title: "ShockHash: Near Optimal-Space Minimal Perfect Hashing Beyond Brute-Force"
    authors: Lehmann Hans-Peter, Sanders Peter, Walzer Stefan
    conference: Arxiv
    year: 2023
    bibkey: lehmann2023shockhash
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2310.14959"}
    tags: ['Arxiv', 'Graph']
    ---
    {% raw %}
    A minimal perfect hash function (MPHF) maps a set S of n keys to the first n integers without collisions. There is a lower bound of n*log(e)=1.44n bits needed to represent an MPHF. This can be reached by a brute-force algorithm that tries e^n hash function seeds in expectation and stores the first seed leading to an MPHF. The most space-efficient previous algorithms for constructing MPHFs all use such a brute-force approach as a basic building block. In this paper, we introduce ShockHash - Small, heavily overloaded cuckoo hash tables for minimal perfect hashing. ShockHash uses two hash functions h_0 and h_1, hoping for the existence of a function f : S->{0, 1} such that x -> h_{f(x)}(x) is an MPHF on S. It then uses a 1-bit retrieval data structure to store f using n + o(n) bits. In graph terminology, ShockHash generates n-edge random graphs until stumbling on a pseudoforest - where each component contains as many edges as nodes. Using cuckoo hashing, ShockHash then derives an MPHF from the pseudoforest in linear time. We show that ShockHash needs to try only about (e/2)^n=1.359^n seeds in expectation. This reduces the space for storing the seed by roughly n bits (maintaining the asymptotically optimal space consumption) and speeds up construction by almost a factor of 2^n compared to brute-force. Bipartite ShockHash reduces the expected construction time again to 1.166^n by maintaining a pool of candidate hash functions and checking all possible pairs. ShockHash as a building block within the RecSplit framework can be constructed up to 3 orders of magnitude faster than competing approaches. It can build an MPHF for 10 million keys with 1.489 bits per key in about half an hour. When instead using ShockHash after an efficient k-perfect hash function, it achieves space usage similar to the best competitors, while being significantly faster to construct and query.
    {% endraw %}