---
layout: publication
title: Accurate And Fast Pixel Retrieval With Spatial And Uncertainty Aware Hypergraph
  Diffusion
authors: Guoyuan An, Yuchi Huo, Sung-Eui Yoon
conference: Arxiv
year: 2024
bibkey: an2024accurate
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11242'}]
tags: ["Efficiency", "Image Retrieval"]
short_authors: Guoyuan An, Yuchi Huo, Sung-Eui Yoon
---
This paper presents a novel method designed to enhance the efficiency and
accuracy of both image retrieval and pixel retrieval. Traditional diffusion
methods struggle to propagate spatial information effectively in conventional
graphs due to their reliance on scalar edge weights. To overcome this
limitation, we introduce a hypergraph-based framework, uniquely capable of
efficiently propagating spatial information using local features during query
time, thereby accurately retrieving and localizing objects within a database.
  Additionally, we innovatively utilize the structural information of the image
graph through a technique we term "community selection". This approach allows
for the assessment of the initial search result's uncertainty and facilitates
an optimal balance between accuracy and speed. This is particularly crucial in
real-world applications where such trade-offs are often necessary.
  Our experimental results, conducted on the (P)ROxford and (P)RParis datasets,
demonstrate the significant superiority of our method over existing diffusion
techniques. We achieve state-of-the-art (SOTA) accuracy in both image-level and
pixel-level retrieval, while also maintaining impressive processing speed. This
dual achievement underscores the effectiveness of our hypergraph-based
framework and community selection technique, marking a notable advancement in
the field of content-based image retrieval.