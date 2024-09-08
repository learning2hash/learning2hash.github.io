---
    layout: publication
    title: "Analysis of Concurrent Lock-Free Hash Tries with Constant-Time Operations"
    authors: Prokopec Aleksandar
    conference: Arxiv
    year: 2017
    bibkey: prokopec2017analysis
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by-sa/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1712.09636"}
    tags: ['Arxiv']
    ---
    Ctrie is a scalable concurrent non-blocking dictionary data structure, with good cache locality, and non-blocking linearizable iterators. However, operations on most existing concurrent hash tries run in O(log n) time. In this technical report, we extend the standard concurrent hash-tries with an auxiliary data structure called a cache. The cache is essentially an array that stores pointers to a specific level of the hash trie. We analyze the performance implications of adding a cache, and prove that the running time of the basic operations becomes O(1).