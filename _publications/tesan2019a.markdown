---
layout: publication
title: A CNN-RNN Framework For Image Annotation From Visual Cues And Social Network
  Metadata
authors: Tobia Tesan, Pasquale Coscia, Lamberto Ballan
conference: Arxiv
year: 2019
bibkey: tesan2019a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.05770'}]
tags: ["Datasets", "Tools & Libraries"]
short_authors: Tobia Tesan, Pasquale Coscia, Lamberto Ballan
---
Images represent a commonly used form of visual communication among people.
Nevertheless, image classification may be a challenging task when dealing with
unclear or non-common images needing more context to be correctly annotated.
Metadata accompanying images on social-media represent an ideal source of
additional information for retrieving proper neighborhoods easing image
annotation task. To this end, we blend visual features extracted from neighbors
and their metadata to jointly leverage context and visual cues. Our models use
multiple semantic embeddings to achieve the dual objective of being robust to
vocabulary changes between train and test sets and decoupling the architecture
from the low-level metadata representation. Convolutional and recurrent neural
networks (CNNs-RNNs) are jointly adopted to infer similarity among neighbors
and query images. We perform comprehensive experiments on the NUS-WIDE dataset
showing that our models outperform state-of-the-art architectures based on
images and metadata, and decrease both sensory and semantic gaps to better
annotate images.