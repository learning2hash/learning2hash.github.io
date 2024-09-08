---
    layout: publication
    title: "Hashing with Linear Probing and Referential Integrity"
    authors: Sanders Peter
    conference: Arxiv
    year: 2018
    bibkey: sanders2018hashing
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1808.04602"}
    tags: ['TOM', 'Arxiv']
    ---
    We describe a variant of linear probing hash tables that never moves elements and thus supports referential integrity, i.e., pointers to elements remain valid while this element is in the hash table. This is achieved by the folklore method of marking some table entries as formerly occupied (tombstones). The innovation is that the number of tombstones is minimized. Experiments indicate that this allows an unbounded number of operations with bounded overhead compared to linear probing without tombstones (and without referential integrity).