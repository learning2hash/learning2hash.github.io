---
layout: publication
title: Contrastive Learning With Stronger Augmentations
authors: Xiao Wang, Guo-jun Qi
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: wang2021contrastive
citations: 146
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.07713'}]
tags: ["Self-Supervised"]
short_authors: Xiao Wang, Guo-jun Qi
---
Representation learning has significantly been developed with the advance of
contrastive learning methods. Most of those methods have benefited from various
data augmentations that are carefully designated to maintain their identities
so that the images transformed from the same instance can still be retrieved.
However, those carefully designed transformations limited us to further explore
the novel patterns exposed by other transformations. Meanwhile, as found in our
experiments, the strong augmentations distorted the images' structures,
resulting in difficult retrieval. Thus, we propose a general framework called
Contrastive Learning with Stronger Augmentations~(CLSA) to complement current
contrastive learning approaches. Here, the distribution divergence between the
weakly and strongly augmented images over the representation bank is adopted to
supervise the retrieval of strongly augmented queries from a pool of instances.
Experiments on the ImageNet dataset and downstream datasets showed the
information from the strongly augmented images can significantly boost the
performance. For example, CLSA achieves top-1 accuracy of 76.2% on ImageNet
with a standard ResNet-50 architecture with a single-layer classifier
fine-tuned, which is almost the same level as 76.5% of supervised results. The
code and pre-trained models are available in
https://github.com/maple-research-lab/CLSA.