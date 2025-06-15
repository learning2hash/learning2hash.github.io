---
layout: publication
title: Adaptive Labeling For Deep Learning To Hash
authors: Yang Huei-fang, Tu, Chen
conference: "Arxiv"
year: 2024
citations: 6
bibkey: yang2024adaptive
additional_links:
  - {name: "Paper", url: "https://openaccess.thecvf.com/content_CVPRW_2019/papers/CEFRL/Yang_Adaptive_Labeling_for_Deep_Learning_to_Hash_CVPRW_2019_paper.pdf"}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Supervised', 'Semi-Supervised']
---
Hash function learning has been widely used for largescale image retrieval because of the efficiency of computation and storage. We introduce AdaLabelHash, a binary
hash function learning approach via deep neural networks
in this paper. In AdaLabelHash, class label representations are variables that are adapted during the backward
network training procedure. We express the labels as hypercube vertices in a K-dimensional space, and the class
label representations together with the network weights are
updated in the learning process. As the label representations (or referred to as codewords in this work), are learned
from data, semantically similar classes will be assigned
with the codewords that are close to each other in terms
of Hamming distance in the label space. The codewords
then serve as the desired output of the hash function learning, and yield compact and discriminating binary hash representations. AdaLabelHash is easy to implement, which
can jointly learn label representations and infer compact
binary codes from data. It is applicable to both supervised
and semi-supervised hash. Experimental results on standard benchmarks demonstrate the satisfactory performance
of AdaLabelHash.
