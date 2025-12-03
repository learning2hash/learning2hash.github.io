---
layout: publication
title: Generating Compositional Color Representations From Text
authors: Paridhi Maheshwari, Nihal Jain, Praneetha Vaddamanu, Dhananjay Raut, Shraiysh
  Vaishay, Vishwa Vinay
conference: Proceedings of the 30th ACM International Conference on Information &amp;
  Knowledge Management
year: 2021
bibkey: maheshwari2021generating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.10477'}]
tags: ["CIKM", "Datasets", "Evaluation", "Image Retrieval", "Robustness"]
short_authors: Maheshwari et al.
---
We consider the cross-modal task of producing color representations for text
phrases. Motivated by the fact that a significant fraction of user queries on
an image search engine follow an (attribute, object) structure, we propose a
generative adversarial network that generates color profiles for such bigrams.
We design our pipeline to learn composition - the ability to combine seen
attributes and objects to unseen pairs. We propose a novel dataset curation
pipeline from existing public sources. We describe how a set of phrases of
interest can be compiled using a graph propagation technique, and then mapped
to images. While this dataset is specialized for our investigations on color,
the method can be extended to other visual dimensions where composition is of
interest. We provide detailed ablation studies that test the behavior of our
GAN architecture with loss functions from the contrastive learning literature.
We show that the generative model achieves lower Frechet Inception Distance
than discriminative ones, and therefore predicts color profiles that better
match those from real images. Finally, we demonstrate improved performance in
image retrieval and classification, indicating the crucial role that color
plays in these downstream tasks.