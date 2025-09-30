---
layout: publication
title: Resource Aware Person Re-identification Across Multiple Resolutions
authors: Yan Wang, Lequn Wang, Yurong You, Xu Zou, Vincent Chen, Serena Li, Gao Huang,
  Bharath Hariharan, Kilian Q. Weinberger
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: wang2018resource
citations: 264
additional_links: [{name: Code, url: 'https://github.com/mileyan/DARENet'}, {name: Paper,
    url: 'https://arxiv.org/abs/1805.08805'}]
tags: ["CVPR", "Datasets"]
short_authors: Wang et al.
---
Not all people are equally easy to identify: color statistics might be enough
for some cases while others might require careful reasoning about high- and
low-level details. However, prevailing person re-identification(re-ID) methods
use one-size-fits-all high-level embeddings from deep convolutional networks
for all cases. This might limit their accuracy on difficult examples or makes
them needlessly expensive for the easy ones. To remedy this, we present a new
person re-ID model that combines effective embeddings built on multiple
convolutional network layers, trained with deep-supervision. On traditional
re-ID benchmarks, our method improves substantially over the previous
state-of-the-art results on all five datasets that we evaluate on. We then
propose two new formulations of the person re-ID problem under
resource-constraints, and show how our model can be used to effectively trade
off accuracy and computation in the presence of resource constraints. Code and
pre-trained models are available at https://github.com/mileyan/DARENet.