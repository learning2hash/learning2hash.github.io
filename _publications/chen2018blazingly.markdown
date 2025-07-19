---
layout: publication
title: Blazingly Fast Video Object Segmentation With Pixel-wise Metric Learning
authors: Chen et al.
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: chen2018blazingly
citations: 283
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.03131'}]
tags: [Distance Metric Learning, CVPR]
---
This paper tackles the problem of video object segmentation, given some user
annotation which indicates the object of interest. The problem is formulated as
pixel-wise retrieval in a learned embedding space: we embed pixels of the same
object instance into the vicinity of each other, using a fully convolutional
network trained by a modified triplet loss as the embedding model. Then the
annotated pixels are set as reference and the rest of the pixels are classified
using a nearest-neighbor approach. The proposed method supports different kinds
of user input such as segmentation mask in the first frame (semi-supervised
scenario), or a sparse set of clicked points (interactive scenario). In the
semi-supervised scenario, we achieve results competitive with the state of the
art but at a fraction of computation cost (275 milliseconds per frame). In the
interactive scenario where the user is able to refine their input iteratively,
the proposed method provides instant response to each input, and reaches
comparable quality to competing methods with much less interaction.