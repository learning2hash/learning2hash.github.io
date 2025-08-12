---
layout: publication
title: 'Sparseconvmil: Sparse Convolutional Context-aware Multiple Instance Learning
  For Whole Slide Image Classification'
authors: Marvin Lerousseau, Maria Vakalopoulou, Eric Deutsch, Nikos Paragios
conference: Arxiv
year: 2021
bibkey: lerousseau2021sparseconvmil
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.02726'}]
tags: []
short_authors: Lerousseau et al.
---
Multiple instance learning (MIL) is the preferred approach for whole slide
image classification. However, most MIL approaches do not exploit the
interdependencies of tiles extracted from a whole slide image, which could
provide valuable cues for classification. This paper presents a novel MIL
approach that exploits the spatial relationship of tiles for classifying whole
slide images. To do so, a sparse map is built from tiles embeddings, and is
then classified by a sparse-input CNN. It obtained state-of-the-art performance
over popular MIL approaches on the classification of cancer subtype involving
10000 whole slide images. Our results suggest that the proposed approach might
(i) improve the representation learning of instances and (ii) exploit the
context of instance embeddings to enhance the classification performance. The
code of this work is open-source at \{github censored for review\}.