---
layout: publication
title: Mining Mid-level Visual Patterns With Deep CNN Activations
authors: Yao Li, Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
conference: International Journal of Computer Vision
year: 2016
bibkey: li2015mining
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.06343'}]
tags: ["CVPR", "ECCV", "ICCV"]
short_authors: Li et al.
---
The purpose of mid-level visual element discovery is to find clusters of
image patches that are both representative and discriminative. Here we study
this problem from the prospective of pattern mining while relying on the
recently popularized Convolutional Neural Networks (CNNs). We observe that a
fully-connected CNN activation extracted from an image patch typically
possesses two appealing properties that enable its seamless integration with
pattern mining techniques. The marriage between CNN activations and association
rule mining, a well-known pattern mining technique in the literature, leads to
fast and effective discovery of representative and discriminative patterns from
a huge number of image patches. When we retrieve and visualize image patches
with the same pattern, surprisingly, they are not only visually similar but
also semantically consistent, and thus give rise to a mid-level visual element
in our work. Given the patterns and retrieved mid-level visual elements, we
propose two methods to generate image feature representations for each. The
first method is to use the patterns as codewords in a dictionary, similar to
the Bag-of-Visual-Words model, we compute a Bag-of-Patterns representation. The
second one relies on the retrieved mid-level visual elements to construct a
Bag-of-Elements representation. We evaluate the two encoding methods on scene
and object classification tasks, and demonstrate that our approach outperforms
or matches recent works using CNN activations for these tasks.