---
layout: publication
title: Effectively Leveraging Attributes For Visual Similarity
authors: Samarth Mishra, Zhongping Zhang, Yuan Shen, Ranjitha Kumar, Venkatesh Saligrama,
  Bryan Plummer
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: mishra2021effectively
citations: 4
additional_links: [{name: Code, url: 'https://github.com/samarth4149/PAN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2105.01695'}]
tags: [ICCV, Datasets, Evaluation]
short_authors: Mishra et al.
---
Measuring similarity between two images often requires performing complex
reasoning along different axes (e.g., color, texture, or shape). Insights into
what might be important for measuring similarity can can be provided by
annotated attributes, but prior work tends to view these annotations as
complete, resulting in them using a simplistic approach of predicting
attributes on single images, which are, in turn, used to measure similarity.
However, it is impractical for a dataset to fully annotate every attribute that
may be important. Thus, only representing images based on these incomplete
annotations may miss out on key information. To address this issue, we propose
the Pairwise Attribute-informed similarity Network (PAN), which breaks
similarity learning into capturing similarity conditions and relevance scores
from a joint representation of two images. This enables our model to identify
that two images contain the same attribute, but can have it deemed irrelevant
(e.g., due to fine-grained differences between them) and ignored for measuring
similarity between the two images. Notably, while prior methods of using
attribute annotations are often unable to outperform prior art, PAN obtains a
4-9% improvement on compatibility prediction between clothing items on Polyvore
Outfits, a 5% gain on few shot classification of images using Caltech-UCSD
Birds (CUB), and over 1% boost to Recall@1 on In-Shop Clothes Retrieval.
Implementation available at https://github.com/samarth4149/PAN