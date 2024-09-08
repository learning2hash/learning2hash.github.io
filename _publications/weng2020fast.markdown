---
    layout: publication
    title: "Fast Search on Binary Codes by Weighted Hamming Distance"
    authors: Weng Zhenyu, Zhu Yuesheng, Liu Ruixin
    conference: Arxiv
    year: 2020
    bibkey: weng2020fast
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2009.08591"}
    tags: ['Arxiv', 'TIP']
    ---
    {% raw %}
    Weighted Hamming distance, as a similarity measure between binary codes and binary queries, provides superior accuracy in search tasks than Hamming distance. However, how to efficiently and accurately find $K$ binary codes that have the smallest weighted Hamming distance to the query remains an open issue. In this paper, a fast search algorithm is proposed to perform the non-exhaustive search for $K$ nearest binary codes by weighted Hamming distance. By using binary codes as direct bucket indices in a hash table, the search algorithm generates a sequence to probe the buckets based on the independence characteristic of the weights for each bit. Furthermore, a fast search framework based on the proposed search algorithm is designed to solve the problem of long binary codes. Specifically, long binary codes are split into substrings and multiple hash tables are built on them. Then, the search algorithm probes the buckets to obtain candidates according to the generated substring indices, and a merging algorithm is proposed to find the nearest binary codes by merging the candidates. Theoretical analysis and experimental results demonstrate that the search algorithm improves the search accuracy compared to other non-exhaustive algorithms and provides orders-of-magnitude faster search than the linear scan baseline.
    {% endraw %}