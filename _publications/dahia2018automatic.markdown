---
layout: publication
title: Automatic Dataset Annotation To Learn CNN Pore Description For Fingerprint
  Recognition
authors: "Gabriel Dahia, Maur\xEDcio Pamplona Segundo"
conference: Arxiv
year: 2018
bibkey: dahia2018automatic
citations: 3
additional_links: [{name: Code, url: 'https://github.com/gdahia/high-res-fingerprint-recognition'},
  {name: Paper, url: 'https://arxiv.org/abs/1809.10229'}]
tags: ["Datasets"]
short_authors: "Gabriel Dahia, Maur\xEDcio Pamplona Segundo"
---
High-resolution fingerprint recognition often relies on sophisticated
matching algorithms based on hand-crafted keypoint descriptors, with pores
being the most common keypoint choice. Our method is the opposite of the
prevalent approach: we use instead a simple matching algorithm based on robust
local pore descriptors that are learned from the data using a CNN. In order to
train this CNN in a fully supervised manner, we describe how the automatic
alignment of fingerprint images can be used to obtain the required training
annotations, which are otherwise missing in all publicly available datasets.
This improves the state-of-the-art recognition results for both partial and
full fingerprints in a public benchmark. To confirm that the observed
improvement is due to the adoption of learned descriptors, we conduct an
ablation study using the most successful pore descriptors previously used in
the literature. All our code is available at
https://github.com/gdahia/high-res-fingerprint-recognition