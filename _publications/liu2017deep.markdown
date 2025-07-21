---
layout: publication
title: 'Deep Sketch Hashing: Fast Free-hand Sketch-based Image Retrieval'
authors: Liu et al.
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: liu2017deep
citations: 267
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.05605'}]
tags: ["Hashing Methods", "Image Retrieval", "CVPR"]
---
Free-hand sketch-based image retrieval (SBIR) is a specific cross-view
retrieval task, in which queries are abstract and ambiguous sketches while the
retrieval database is formed with natural images. Work in this area mainly
focuses on extracting representative and shared features for sketches and
natural images. However, these can neither cope well with the geometric
distortion between sketches and images nor be feasible for large-scale SBIR due
to the heavy continuous-valued distance computation. In this paper, we speed up
SBIR by introducing a novel binary coding method, named \textbf\{Deep Sketch
Hashing\} (DSH), where a semi-heterogeneous deep architecture is proposed and
incorporated into an end-to-end binary coding framework. Specifically, three
convolutional neural networks are utilized to encode free-hand sketches,
natural images and, especially, the auxiliary sketch-tokens which are adopted
as bridges to mitigate the sketch-image geometric distortion. The learned DSH
codes can effectively capture the cross-view similarities as well as the
intrinsic semantic correlations between different categories. To the best of
our knowledge, DSH is the first hashing work specifically designed for
category-level SBIR with an end-to-end deep architecture. The proposed DSH is
comprehensively evaluated on two large-scale datasets of TU-Berlin Extension
and Sketchy, and the experiments consistently show DSH's superior SBIR
accuracies over several state-of-the-art methods, while achieving significantly
reduced retrieval time and memory footprint.