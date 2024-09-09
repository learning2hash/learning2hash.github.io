---
layout: publication
title: "Fast and scalable minimal perfect hashing for massive key sets"
authors: Limasset Antoine, Rizk Guillaume, Chikhi Rayan, Peterlongo Pierre
conference: Arxiv
year: 2017
bibkey: limasset2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1702.03154"}
  - {name: "Code", url: "https://github.com/rizkg/BBHash"}
tags: ['ARXIV']
---
Minimal perfect hash functions provide space-efficient and collision-free hashing on static sets. Existing algorithms and implementations that build such functions have practical limitations on the number of input elements they can process, due to high construction time, RAM or external memory usage. We revisit a simple algorithm and show that it is highly competitive with the state of the art, especially in terms of construction time and memory usage. We provide a parallel C++ implementation called BBhash. It is capable of creating a minimal perfect hash function of $10^{10}$ elements in less than 7 minutes using 8 threads and 5 GB of memory, and the resulting function uses 3.7 bits/element. To the best of our knowledge, this is also the first implementation that has been successfully tested on an input of cardinality $10^{12}$. Source code: https://github.com/rizkg/BBHash