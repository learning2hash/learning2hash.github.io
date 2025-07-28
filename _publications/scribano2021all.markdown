---
layout: publication
title: 'All You Can Embed: Natural Language Based Vehicle Retrieval With Spatio-temporal
  Transformers'
authors: Carmelo Scribano, Davide Sapienza, Giorgia Franchini, Micaela Verucchi, Marko
  Bertogna
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: scribano2021all
citations: 7
additional_links: [{name: Code, url: 'https://github.com/cscribano/AYCE_2021'}, {
    name: Paper, url: 'https://arxiv.org/abs/2106.10153'}]
tags: ["CVPR"]
short_authors: Scribano et al.
---
Combining Natural Language with Vision represents a unique and interesting
challenge in the domain of Artificial Intelligence. The AI City Challenge Track
5 for Natural Language-Based Vehicle Retrieval focuses on the problem of
combining visual and textual information, applied to a smart-city use case. In
this paper, we present All You Can Embed (AYCE), a modular solution to
correlate single-vehicle tracking sequences with natural language. The main
building blocks of the proposed architecture are (i) BERT to provide an
embedding of the textual descriptions, (ii) a convolutional backbone along with
a Transformer model to embed the visual information. For the training of the
retrieval model, a variation of the Triplet Margin Loss is proposed to learn a
distance measure between the visual and language embeddings. The code is
publicly available at https://github.com/cscribano/AYCE_2021.