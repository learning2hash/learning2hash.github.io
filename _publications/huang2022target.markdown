---
layout: publication
title: Target-oriented Sentiment Classification With Sequential Cross-modal Semantic
  Graph
authors: Yufeng Huang, Zhuo Chen, Jiaoyan Chen, Jeff Z. Pan, Zhen Yao, Wen Zhang
conference: Lecture Notes in Computer Science
year: 2023
bibkey: huang2022target
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09417'}]
tags: []
short_authors: Huang et al.
---
Multi-modal aspect-based sentiment classification (MABSC) is task of
classifying the sentiment of a target entity mentioned in a sentence and an
image. However, previous methods failed to account for the fine-grained
semantic association between the image and the text, which resulted in limited
identification of fine-grained image aspects and opinions. To address these
limitations, in this paper we propose a new approach called SeqCSG, which
enhances the encoder-decoder sentiment classification framework using
sequential cross-modal semantic graphs. SeqCSG utilizes image captions and
scene graphs to extract both global and local fine-grained image information
and considers them as elements of the cross-modal semantic graph along with
tokens from tweets. The sequential cross-modal semantic graph is represented as
a sequence with a multi-modal adjacency matrix indicating relationships between
elements. Experimental results show that the approach outperforms existing
methods and achieves state-of-the-art performance on two standard datasets.
Further analysis has demonstrated that the model can implicitly learn the
correlation between fine-grained information of the image and the text with the
given target. Our code is available at https://github.com/zjukg/SeqCSG.