---
layout: publication
title: Can Cross Encoders Produce Useful Sentence Embeddings?
authors: Ananthakrishnan et al.
conference: Natural Language Engineering
year: 2025
bibkey: ananthakrishnan2025can
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.03552'}]
---
Cross encoders (CEs) are trained with sentence pairs to detect relatedness.
As CEs require sentence pairs at inference, the prevailing view is that they
can only be used as re-rankers in information retrieval pipelines. Dual
encoders (DEs) are instead used to embed sentences, where sentence pairs are
encoded by two separate encoders with shared weights at training, and a loss
function that ensures the pair's embeddings lie close in vector space if the
sentences are related. DEs however, require much larger datasets to train, and
are less accurate than CEs. We report a curious finding that embeddings from
earlier layers of CEs can in fact be used within an information retrieval
pipeline. We show how to exploit CEs to distill a lighter-weight DE, with a
5.15x speedup in inference time.