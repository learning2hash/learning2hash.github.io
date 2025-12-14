---
layout: publication
title: Learning Genomic Sequence Representations Using Graph Neural Networks Over
  De Bruijn Graphs
authors: "Kacper Kapu\u015Bniak, Manuel Burger, Gunnar R\xE4tsch, Amir Joudaki"
conference: Arxiv
year: 2023
bibkey: "kapu\u015Bniak2023learning"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.03865'}]
tags: [Self-Supervised, Supervised]
short_authors: "Kapu\u015Bniak et al."
---
The rapid expansion of genomic sequence data calls for new methods to achieve
robust sequence representations. Existing techniques often neglect intricate
structural details, emphasizing mainly contextual information. To address this,
we developed k-mer embeddings that merge contextual and structural string
information by enhancing De Bruijn graphs with structural similarity
connections. Subsequently, we crafted a self-supervised method based on
Contrastive Learning that employs a heterogeneous Graph Convolutional Network
encoder and constructs positive pairs based on node similarities. Our
embeddings consistently outperform prior techniques for Edit Distance
Approximation and Closest String Retrieval tasks.