---
    layout: publication
    title: "Fast Consistent Hashing in Constant Time"
    authors: Leu Eric
    conference: Arxiv
    year: 2023
    bibkey: leu2023fast
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2307.12448"}
    tags: ['Arxiv']
    ---
    Consistent hashing is a technique that can minimize key remapping when the number of hash buckets changes. The paper proposes a fast consistent hash algorithm (called power consistent hash) that has $O(1)$ expected time for key lookup, independent of the number of buckets. Hash values are computed in real time. No search data structure is constructed to store bucket ranges or key mappings. The algorithm has a lightweight design using $O(1)$ space with superior scalability. In particular, it uses two auxiliary hash functions to achieve distribution uniformity and $O(1)$ expected time for key lookup. Furthermore, it performs consistent hashing such that only a minimal number of keys are remapped when the number of buckets changes. Consistent hashing has a wide range of use cases, including load balancing, distributed caching, and distributed key-value stores. The proposed algorithm is faster than well-known consistent hash algorithms with $O(\log n)$ lookup time.