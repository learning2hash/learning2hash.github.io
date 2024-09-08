---
    layout: publication
    title: "Separate Chaining Meets Compact Hashing"
    authors: Köppl Dominik
    conference: Arxiv
    year: 2019
    bibkey: köppl2019separate
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1905.00163"}
    tags: ['Arxiv']
    ---
    While separate chaining is a common strategy for resolving collisions in a hash table taught in most textbooks, compact hashing is a less common technique for saving space when hashing integers whose domain is relatively small with respect to the problem size. It is widely believed that hash tables waste a considerable amount of memory, as they either leave allocated space untouched (open addressing) or store additional pointers (separate chaining). For the former, Cleary introduced the compact hashing technique that stores only a part of a key to save space. However, as can be seen by the line of research focusing on compact hash tables with open addressing, there is additional information, called displacement, required for restoring a key. There are several representations of this displacement information with different space and time trade-offs. In this article, we introduce a separate chaining hash table that applies the compact hashing technique without the need for the displacement information. Practical evaluations reveal that insertions in this hash table are faster or use less space than all previously known compact hash tables on modern computer architectures when storing sufficiently large satellite data.