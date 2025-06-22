---
layout: publication
title: Zero-shot Hashing Based On Reconstruction With Part Alignment
authors: Yan Jiang et al.
conference: Arxiv
year: 2025
citations: 0
bibkey: jiang2025zero
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.07037'}]
tags: [Applications, Hashing Methods]
---
Hashing algorithms have been widely used in large-scale image retrieval
tasks, especially for seen class data. Zero-shot hashing algorithms have been
proposed to handle unseen class data. The key technique in these algorithms
involves learning features from seen classes and transferring them to unseen
classes, that is, aligning the feature embeddings between the seen and unseen
classes. Most existing zero-shot hashing algorithms use the shared attributes
between the two classes of interest to complete alignment tasks. However, the
attributes are always described for a whole image, even though they represent
specific parts of the image. Hence, these methods ignore the importance of
aligning attributes with the corresponding image parts, which explicitly
introduces noise and reduces the accuracy achieved when aligning the features
of seen and unseen classes. To address this problem, we propose a new zero-shot
hashing method called RAZH. We first use a clustering algorithm to group
similar patches to image parts for attribute matching and then replace the
image parts with the corresponding attribute vectors, gradually aligning each
part with its nearest attribute. Extensive evaluation results demonstrate the
superiority of the RAZH method over several state-of-the-art methods.