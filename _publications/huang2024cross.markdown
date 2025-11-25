---
layout: publication
title: Cross-modal And Uni-modal Soft-label Alignment For Image-text Retrieval
authors: Hailang Huang, Zhijie Nie, Ziqiao Wang, Ziyu Shang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: huang2024cross
citations: 23
additional_links: [{name: Code, url: 'https://github.com/lerogo/aaai24_itr_cusa'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.05261'}]
tags: ["AAAI", "Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Huang et al.
---
Current image-text retrieval methods have demonstrated impressive performance
in recent years. However, they still face two problems: the inter-modal
matching missing problem and the intra-modal semantic loss problem. These
problems can significantly affect the accuracy of image-text retrieval. To
address these challenges, we propose a novel method called Cross-modal and
Uni-modal Soft-label Alignment (CUSA). Our method leverages the power of
uni-modal pre-trained models to provide soft-label supervision signals for the
image-text retrieval model. Additionally, we introduce two alignment
techniques, Cross-modal Soft-label Alignment (CSA) and Uni-modal Soft-label
Alignment (USA), to overcome false negatives and enhance similarity recognition
between uni-modal samples. Our method is designed to be plug-and-play, meaning
it can be easily applied to existing image-text retrieval models without
changing their original architectures. Extensive experiments on various
image-text retrieval models and datasets, we demonstrate that our method can
consistently improve the performance of image-text retrieval and achieve new
state-of-the-art results. Furthermore, our method can also boost the uni-modal
retrieval performance of image-text retrieval models, enabling it to achieve
universal retrieval. The code and supplementary files can be found at
https://github.com/lerogo/aaai24_itr_cusa.