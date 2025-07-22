---
layout: publication
title: Large-scale Product Retrieval With Weakly Supervised Representation Learning
authors: Han Xiao, Ng Kam Woh, Nag Sauradip, Qu Zhiyu
conference: Arxiv
year: 2022
bibkey: han2022large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.00955'}]
tags: ["Image-Retrieval", "Scalability", "Hybrid-Ann-Methods", "Datasets", "Supervised", "Re-Ranking"]
short_authors: Han et al.
---
Large-scale weakly supervised product retrieval is a practically useful yet
computationally challenging problem. This paper introduces a novel solution for
the eBay Visual Search Challenge (eProduct) held at the Ninth Workshop on
Fine-Grained Visual Categorisation workshop (FGVC9) of CVPR 2022. This
competition presents two challenges: (a) E-commerce is a drastically
fine-grained domain including many products with subtle visual differences; (b)
A lacking of target instance-level labels for model training, with only coarse
category labels and product titles available. To overcome these obstacles, we
formulate a strong solution by a set of dedicated designs: (a) Instead of using
text training data directly, we mine thousands of pseudo-attributes from
product titles and use them as the ground truths for multi-label
classification. (b) We incorporate several strong backbones with advanced
training recipes for more discriminative representation learning. (c) We
further introduce a number of post-processing techniques including whitening,
re-ranking and model ensemble for retrieval enhancement. By achieving 71.53%
MAR, our solution "Involution King" achieves the second position on the
leaderboard.