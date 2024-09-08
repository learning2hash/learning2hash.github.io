---
    layout: publication
    title: "Parallel and External-Memory Construction of Minimal Perfect Hash Functions with PTHash"
    authors: Pibiri Giulio Ermanno, Trani Roberto
    conference: Arxiv
    year: 2021
    bibkey: pibiri2021parallel
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2106.02350"}
    tags: ['Arxiv']
    ---
    A function $f : U \to \{0,\ldots,n-1\}$ is a minimal perfect hash function for a set $S \subseteq U$ of size $n$, if $f$ bijectively maps $S$ into the first $n$ natural numbers. These functions are important for many practical applications in computing, such as search engines, computer networks, and databases. Several algorithms have been proposed to build minimal perfect hash functions that: scale well to large sets, retain fast evaluation time, and take very little space, e.g., 2 - 3 bits/key. PTHash is one such algorithm, achieving very fast evaluation in compressed space, typically several times faster than other techniques. In this work, we propose a new construction algorithm for PTHash enabling: (1) multi-threading, to either build functions more quickly or more space-efficiently, and (2) external-memory processing to scale to inputs much larger than the available internal memory. Only few other algorithms in the literature share these features, despite of their big practical impact. We conduct an extensive experimental assessment on large real-world string collections and show that, with respect to other techniques, PTHash is competitive in construction time and space consumption, but retains 2 - 6$\times$ better lookup time.