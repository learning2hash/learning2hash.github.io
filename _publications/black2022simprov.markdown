---
layout: publication
title: 'Simprov: Scalable Image Provenance Framework For Robust Content Attribution'
authors: Alexander Black, Tu Bui, Simon Jenni, Zhifei Zhang, Viswanathan Swaminanthan,
  John Collomosse
conference: Arxiv
year: 2022
bibkey: black2022simprov
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.14245'}]
tags: [Robustness, Datasets, Re-ranking, Hybrid ANN Methods, Scalability, Tools &
    Libraries]
short_authors: Black et al.
---
We present SImProv - a scalable image provenance framework to match a query
image back to a trusted database of originals and identify possible
manipulations on the query. SImProv consists of three stages: a scalable search
stage for retrieving top-k most similar images; a re-ranking and
near-duplicated detection stage for identifying the original among the
candidates; and finally a manipulation detection and visualization stage for
localizing regions within the query that may have been manipulated to differ
from the original. SImProv is robust to benign image transformations that
commonly occur during online redistribution, such as artifacts due to noise and
recompression degradation, as well as out-of-place transformations due to image
padding, warping, and changes in size and shape. Robustness towards
out-of-place transformations is achieved via the end-to-end training of a
differentiable warping module within the comparator architecture. We
demonstrate effective retrieval and manipulation detection over a dataset of
100 million images.