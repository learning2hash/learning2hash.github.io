---
layout: publication
title: 'Less Is More: Selective Reduction Of CT Data For Self-supervised Pre-training
  Of Deep Learning Models With Contrastive Learning Improves Downstream Classification
  Performance'
authors: "Daniel Wolf, Tristan Payer, Catharina Silvia Lisson, Christoph Gerhard Lisson,\
  \ Meinrad Beer, Michael G\xF6tz, Timo Ropinski"
conference: Computers in Biology and Medicine
year: 2024
bibkey: wolf2024less
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.14524'}]
tags: ["Datasets", "Evaluation", "Neural Hashing", "Self-Supervised", "Supervised"]
short_authors: Wolf et al.
---
Self-supervised pre-training of deep learning models with contrastive
learning is a widely used technique in image analysis. Current findings
indicate a strong potential for contrastive pre-training on medical images.
However, further research is necessary to incorporate the particular
characteristics of these images. We hypothesize that the similarity of medical
images hinders the success of contrastive learning in the medical imaging
domain. To this end, we investigate different strategies based on deep
embedding, information theory, and hashing in order to identify and reduce
redundancy in medical pre-training datasets. The effect of these different
reduction strategies on contrastive learning is evaluated on two pre-training
datasets and several downstream classification tasks. In all of our
experiments, dataset reduction leads to a considerable performance gain in
downstream tasks, e.g., an AUC score improvement from 0.78 to 0.83 for the
COVID CT Classification Grand Challenge, 0.97 to 0.98 for the OrganSMNIST
Classification Challenge and 0.73 to 0.83 for a brain hemorrhage classification
task. Furthermore, pre-training is up to nine times faster due to the dataset
reduction. In conclusion, the proposed approach highlights the importance of
dataset quality and provides a transferable approach to improve contrastive
pre-training for classification downstream tasks on medical images.