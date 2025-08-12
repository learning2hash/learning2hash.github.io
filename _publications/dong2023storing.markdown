---
layout: publication
title: Storing A Trie With Compact And Predictable Space
authors: Yuxuan Dong
conference: Arxiv
year: 2023
bibkey: dong2023storing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.03690'}]
tags: ["Compact Codes", "Memory Efficiency", "Tree Based ANN"]
short_authors: Yuxuan Dong
---
This paper proposed a storing approach for trie structures, called coordinate
hash trie. The basic idea is using a global hash table with a special hash
function to store all edges of a trie. For a trie with \(n\) nodes and an
alphabet with size \(m\), the execution time of finding, inserting and deleting a
child node, is \(O(1)\) for the average case, \(O(m)\) for the worst case. The
space used by this approach is \(O(n)\), unrelated to \(m\). The constant of space
consumption is predictable, with no need for reallocation or resizing. In
addition, this approach is very easy to implement.