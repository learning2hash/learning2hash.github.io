---
layout: publication
title: Multi-modal Extreme Classification
authors: Anshul Mittal, Kunal Dahiya, Shreya Malani, Janani Ramaswamy, Seba Kuruvilla,
  Jitendra Ajmera, Keng-Hao Chang, Sumeet Agarwal, Purushottam Kar, Manik Varma
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: mittal2022multi
citations: 9
additional_links: [{name: Code, url: 'https://github.com/Extreme-classification/MUFIN'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.04961'}]
tags: ["CVPR"]
short_authors: Mittal et al.
---
This paper develops the MUFIN technique for extreme classification (XC) tasks
with millions of labels where datapoints and labels are endowed with visual and
textual descriptors. Applications of MUFIN to product-to-product recommendation
and bid query prediction over several millions of products are presented.
Contemporary multi-modal methods frequently rely on purely embedding-based
methods. On the other hand, XC methods utilize classifier architectures to
offer superior accuracies than embedding only methods but mostly focus on
text-based categorization tasks. MUFIN bridges this gap by reformulating
multi-modal categorization as an XC problem with several millions of labels.
This presents the twin challenges of developing multi-modal architectures that
can offer embeddings sufficiently expressive to allow accurate categorization
over millions of labels; and training and inference routines that scale
logarithmically in the number of labels. MUFIN develops an architecture based
on cross-modal attention and trains it in a modular fashion using pre-training
and positive and negative mining. A novel product-to-product recommendation
dataset MM-AmazonTitles-300K containing over 300K products was curated from
publicly available amazon.com listings with each product endowed with a title
and multiple images. On the all datasets MUFIN offered at least 3% higher
accuracy than leading text-based, image-based and multi-modal techniques. Code
for MUFIN is available at https://github.com/Extreme-classification/MUFIN