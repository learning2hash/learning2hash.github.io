---
layout: publication
title: Automatic Spatially-aware Fashion Concept Discovery
authors: Xintong Han, Zuxuan Wu, Phoenix X. Huang, Xiao Zhang, Menglong Zhu, Yuan
  Li, Yang Zhao, Larry S. Davis
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: han2017automatic
citations: 182
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01311'}]
tags: [Evaluation, Datasets, ICCV]
short_authors: Han et al.
---
This paper proposes an automatic spatially-aware concept discovery approach
using weakly labeled image-text data from shopping websites. We first fine-tune
GoogleNet by jointly modeling clothing images and their corresponding
descriptions in a visual-semantic embedding space. Then, for each attribute
(word), we generate its spatially-aware representation by combining its
semantic word vector representation with its spatial representation derived
from the convolutional maps of the fine-tuned network. The resulting
spatially-aware representations are further used to cluster attributes into
multiple groups to form spatially-aware concepts (e.g., the neckline concept
might consist of attributes like v-neck, round-neck, etc). Finally, we
decompose the visual-semantic embedding space into multiple concept-specific
subspaces, which facilitates structured browsing and attribute-feedback product
retrieval by exploiting multimodal linguistic regularities. We conducted
extensive experiments on our newly collected Fashion200K dataset, and results
on clustering quality evaluation and attribute-feedback product retrieval task
demonstrate the effectiveness of our automatically discovered spatially-aware
concepts.