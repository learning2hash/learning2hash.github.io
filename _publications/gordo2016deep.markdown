---
layout: publication
title: 'Deep Image Retrieval: Learning Global Representations For Image Search'
authors: Albert Gordo, Jon Almazan, Jerome Revaud, Diane Larlus
conference: Lecture Notes in Computer Science
year: 2016
bibkey: gordo2016deep
citations: 741
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.01325'}]
tags: [Scalability, Tools & Libraries, Datasets, Image Retrieval]
short_authors: Gordo et al.
---
We propose a novel approach for instance-level image retrieval. It produces a
global and compact fixed-length representation for each image by aggregating
many region-wise descriptors. In contrast to previous works employing
pre-trained deep networks as a black box to produce features, our method
leverages a deep architecture trained for the specific task of image retrieval.
Our contribution is twofold: (i) we leverage a ranking framework to learn
convolution and projection weights that are used to build the region features;
and (ii) we employ a region proposal network to learn which regions should be
pooled to form the final global descriptor. We show that using clean training
data is key to the success of our approach. To that aim, we use a large scale
but noisy landmark dataset and develop an automatic cleaning approach. The
proposed architecture produces a global image representation in a single
forward pass. Our approach significantly outperforms previous approaches based
on global descriptors on standard datasets. It even surpasses most prior works
based on costly local descriptor indexing and spatial verification. Additional
material is available at www.xrce.xerox.com/Deep-Image-Retrieval.