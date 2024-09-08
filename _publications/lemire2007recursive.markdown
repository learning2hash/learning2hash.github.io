---
    layout: publication
    title: "Recursive n-gram hashing is pairwise independent, at best"
    authors: Lemire Daniel, Kaser Owen
    conference: Computer Speech & Language
    year: 2007
    bibkey: lemire2007recursive
    additional_links:
       - {name: "DOI", url: "10.1016/j.csl.2009.12.001"}
   - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/0705.4676"}
    tags: ['Computer Speech & Language']
    ---
    {% raw %}
    Many applications use sequences of n consecutive symbols (n-grams). Hashing these n-grams can be a performance bottleneck. For more speed, recursive hash families compute hash values by updating previous values. We prove that recursive hash families cannot be more than pairwise independent. While hashing by irreducible polynomials is pairwise independent, our implementations either run in time O(n) or use an exponential amount of memory. As a more scalable alternative, we make hashing by cyclic polynomials pairwise independent by ignoring n-1 bits. Experimentally, we show that hashing by cyclic polynomials is is twice as fast as hashing by irreducible polynomials. We also show that randomized Karp-Rabin hash families are not pairwise independent.
    {% endraw %}