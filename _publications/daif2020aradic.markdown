---
layout: publication
title: 'Aradic: Arabic Document Classification Using Image-based Character Embeddings
  And Class-balanced Loss'
authors: Mahmoud Daif, Shunsuke Kitada, Hitoshi Iyatomi
conference: 'Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics: Student Research Workshop'
year: 2020
bibkey: daif2020aradic
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11586'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Mahmoud Daif, Shunsuke Kitada, Hitoshi Iyatomi
---
Classical and some deep learning techniques for Arabic text classification
often depend on complex morphological analysis, word segmentation, and
hand-crafted feature engineering. These could be eliminated by using
character-level features. We propose a novel end-to-end Arabic document
classification framework, Arabic document image-based classifier (AraDIC),
inspired by the work on image-based character embeddings. AraDIC consists of an
image-based character encoder and a classifier. They are trained in an
end-to-end fashion using the class balanced loss to deal with the long-tailed
data distribution problem. To evaluate the effectiveness of AraDIC, we created
and published two datasets, the Arabic Wikipedia title (AWT) dataset and the
Arabic poetry (AraP) dataset. To the best of our knowledge, this is the first
image-based character embedding framework addressing the problem of Arabic text
classification. We also present the first deep learning-based text classifier
widely evaluated on modern standard Arabic, colloquial Arabic and classical
Arabic. AraDIC shows performance improvement over classical and deep learning
baselines by 12.29% and 23.05% for the micro and macro F-score, respectively.