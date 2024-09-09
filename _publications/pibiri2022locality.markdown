---
    layout: publication
    title: "Locality-Preserving Minimal Perfect Hashing of k-mers"
    authors: Pibiri Giulio Ermanno, Shibuya Yoshihiro, Limasset Antoine
    conference: Arxiv
    year: 2022
    bibkey: pibiri2022locality
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2210.13097"}
    tags: ['ARXIV']
    ---
    Minimal perfect hashing is the problem of mapping a static set of $n$ distinct keys into the address space $\\{1,\ldots,n\\}$ bijectively. It is well-known that $n\log_2(e)$ bits are necessary to specify a minimal perfect hash function (MPHF) $f$, when no additional knowledge of the input keys is to be used. However, it is often the case in practice that the input keys have intrinsic relationships that we can exploit to lower the bit complexity of $f$. For example, consider a string and the set of all its distinct $k$-mers as input keys: since two consecutive $k$-mers share an overlap of $k-1$ symbols, it seems possible to beat the classic $\log_2(e)$ bits/key barrier in this case. Moreover, we would like $f$ to map consecutive $k$-mers to consecutive addresses, as to also preserve as much as possible their relationship in the codomain. This is a useful feature in practice as it guarantees a certain degree of locality of reference for $f$, resulting in a better evaluation time when querying consecutive $k$-mers. Motivated by these premises, we initiate the study of a new type of locality-preserving MPHF designed for $k$-mers extracted consecutively from a collection of strings. We design a construction whose space usage decreases for growing $k$ and discuss experiments with a practical implementation of the method: in practice, the functions built with our method can be several times smaller and even faster to query than the most efficient MPHFs in the literature.