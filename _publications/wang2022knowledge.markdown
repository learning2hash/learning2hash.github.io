---
layout: publication
title: Knowledge Mining With Scene Text For Fine-grained Recognition
authors: Hao Wang, Junchao Liao, Tianheng Cheng, Zewen Gao, Hao Liu, Bo Ren, Xiang
  Bai, Wenyu Liu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: wang2022knowledge
citations: 15
additional_links: [{name: Code, url: 'https://github.com/lanfeng4659/KnowledgeMiningWithSceneText'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.14215'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
Recently, the semantics of scene text has been proven to be essential in
fine-grained image classification. However, the existing methods mainly exploit
the literal meaning of scene text for fine-grained recognition, which might be
irrelevant when it is not significantly related to objects/scenes. We propose
an end-to-end trainable network that mines implicit contextual knowledge behind
scene text image and enhance the semantics and correlation to fine-tune the
image representation. Unlike the existing methods, our model integrates three
modalities: visual feature extraction, text semantics extraction, and
correlating background knowledge to fine-grained image classification.
Specifically, we employ KnowBert to retrieve relevant knowledge for semantic
representation and combine it with image features for fine-grained
classification. Experiments on two benchmark datasets, Con-Text, and Drink
Bottle, show that our method outperforms the state-of-the-art by 3.72% mAP and
5.39% mAP, respectively. To further validate the effectiveness of the proposed
method, we create a new dataset on crowd activity recognition for the
evaluation. The source code and new dataset of this work are available at
https://github.com/lanfeng4659/KnowledgeMiningWithSceneText.