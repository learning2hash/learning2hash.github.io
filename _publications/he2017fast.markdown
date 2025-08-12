---
layout: publication
title: Fast Fine-grained Image Classification Via Weakly Supervised Discriminative
  Localization
authors: Xiangteng He, Yuxin Peng, Junjie Zhao
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2018
bibkey: he2017fast
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01168'}]
tags: []
short_authors: Xiangteng He, Yuxin Peng, Junjie Zhao
---
Fine-grained image classification is to recognize hundreds of subcategories
in each basic-level category. Existing methods employ discriminative
localization to find the key distinctions among subcategories. However, they
generally have two limitations: (1) Discriminative localization relies on
region proposal methods to hypothesize the locations of discriminative regions,
which are time-consuming. (2) The training of discriminative localization
depends on object or part annotations, which are heavily labor-consuming. It is
highly challenging to address the two key limitations simultaneously, and
existing methods only focus on one of them. Therefore, we propose a weakly
supervised discriminative localization approach (WSDL) for fast fine-grained
image classification to address the two limitations at the same time, and its
main advantages are: (1) n-pathway end-to-end discriminative localization
network is designed to improve classification speed, which simultaneously
localizes multiple different discriminative regions for one image to boost
classification accuracy, and shares full-image convolutional features generated
by region proposal network to accelerate the process of generating region
proposals as well as reduce the computation of convolutional operation. (2)
Multi-level attention guided localization learning is proposed to localize
discriminative regions with different focuses automatically, without using
object and part annotations, avoiding the labor consumption. Different level
attentions focus on different characteristics of the image, which are
complementary and boost the classification accuracy. Both are jointly employed
to simultaneously improve classification speed and eliminate dependence on
object and part annotations. Compared with state-of-the-art methods on 2
widely-used fine-grained image classification datasets, our WSDL approach
achieves the best performance.