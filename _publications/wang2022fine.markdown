---
layout: publication
title: Fine-grained Image Style Transfer With Visual Transformers
authors: Jianbo Wang, Huan Yang, Jianlong Fu, Toshihiko Yamasaki, Baining Guo
conference: Lecture Notes in Computer Science
year: 2023
bibkey: wang2022fine
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.05176'}]
tags: []
short_authors: Wang et al.
---
With the development of the convolutional neural network, image style
transfer has drawn increasing attention. However, most existing approaches
adopt a global feature transformation to transfer style patterns into content
images (e.g., AdaIN and WCT). Such a design usually destroys the spatial
information of the input images and fails to transfer fine-grained style
patterns into style transfer results. To solve this problem, we propose a novel
STyle TRansformer (STTR) network which breaks both content and style images
into visual tokens to achieve a fine-grained style transformation.
Specifically, two attention mechanisms are adopted in our STTR. We first
propose to use self-attention to encode content and style tokens such that
similar tokens can be grouped and learned together. We then adopt
cross-attention between content and style tokens that encourages fine-grained
style transformations. To compare STTR with existing approaches, we conduct
user studies on Amazon Mechanical Turk (AMT), which are carried out with 50
human subjects with 1,000 votes in total. Extensive evaluations demonstrate the
effectiveness and efficiency of the proposed STTR in generating visually
pleasing style transfer results.