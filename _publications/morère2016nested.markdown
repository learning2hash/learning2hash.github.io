---
    layout: publication
    title: "Nested Invariance Pooling and RBM Hashing for Image Instance Retrieval"
    authors: Morère Olivier, Lin Jie, Veillard Antoine, Chandrasekhar Vijay, Poggio Tomaso
    conference: Arxiv
    year: 2016
    bibkey: morère2016nested
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1603.04595"}
    tags: ['Arxiv']
    ---
    {% raw %}
    The goal of this work is the computation of very compact binary hashes for image instance retrieval. Our approach has two novel contributions. The first one is Nested Invariance Pooling (NIP), a method inspired from i-theory, a mathematical theory for computing group invariant transformations with feed-forward neural networks. NIP is able to produce compact and well-performing descriptors with visual representations extracted from convolutional neural networks. We specifically incorporate scale, translation and rotation invariances but the scheme can be extended to any arbitrary sets of transformations. We also show that using moments of increasing order throughout nesting is important. The NIP descriptors are then hashed to the target code size (32-256 bits) with a Restricted Boltzmann Machine with a novel batch-level regularization scheme specifically designed for the purpose of hashing (RBMH). A thorough empirical evaluation with state-of-the-art shows that the results obtained both with the NIP descriptors and the NIP+RBMH hashes are consistently outstanding across a wide range of datasets.
    {% endraw %}