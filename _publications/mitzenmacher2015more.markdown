---
    layout: publication
    title: "More Analysis of Double Hashing for Balanced Allocations"
    authors: Mitzenmacher Michael
    conference: Arxiv
    year: 2015
    bibkey: mitzenmacher2015more
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1503.00658"}
    tags: ['Arxiv', 'TIP']
    ---
    With double hashing, for a key $x$, one generates two hash values $f(x)$ and $g(x)$, and then uses combinations $(f(x) +i g(x)) \bmod n$ for $i=0,1,2,...$ to generate multiple hash values in the range $[0,n-1]$ from the initial two. For balanced allocations, keys are hashed into a hash table where each bucket can hold multiple keys, and each key is placed in the least loaded of $d$ choices. It has been shown previously that asymptotically the performance of double hashing and fully random hashing is the same in the balanced allocation paradigm using fluid limit methods. Here we extend a coupling argument used by Lueker and Molodowitch to show that double hashing and ideal uniform hashing are asymptotically equivalent in the setting of open address hash tables to the balanced allocation setting, providing further insight into this phenomenon. We also discuss the potential for and bottlenecks limiting the use this approach for other multiple choice hashing schemes.