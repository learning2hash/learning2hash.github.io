---
    layout: publication
    title: "Simple, compact and robust approximate string dictionary"
    authors: Chegrane Ibrahim, Belazzougui Djamal
    conference: Arxiv
    year: 2013
    bibkey: chegrane2013simple
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1312.4678"}
    tags: ['Arxiv']
    ---
    This paper is concerned with practical implementations of approximate string dictionaries that allow edit errors. In this problem, we have as input a dictionary $D$ of $d$ strings of total length $n$ over an alphabet of size $\sigma$. Given a bound $k$ and a pattern $x$ of length $m$, a query has to return all the strings of the dictionary which are at edit distance at most $k$ from $x$, where the edit distance between two strings $x$ and $y$ is defined as the minimum-cost sequence of edit operations that transform $x$ into $y$. The cost of a sequence of operations is defined as the sum of the costs of the operations involved in the sequence. In this paper, we assume that each of these operations has unit cost and consider only three operations: deletion of one character, insertion of one character and substitution of a character by another. We present a practical implementation of the data structure we recently proposed and which works only for one error. We extend the scheme to $2\leq k<m$. Our implementation has many desirable properties: it has a very fast and space-efficient building algorithm. The dictionary data structure is compact and has fast and robust query time. Finally our data structure is simple to implement as it only uses basic techniques from the literature, mainly hashing (linear probing and hash signatures) and succinct data structures (bitvectors supporting rank queries).