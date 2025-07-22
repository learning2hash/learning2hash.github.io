---
layout: publication
title: 'ALADIN: Distilling Fine-grained Alignment Scores For Efficient Image-text
  Matching And Retrieval'
authors: Messina Nicola, Stefanini Matteo, Cornia Marcella, Baraldi Lorenzo, Falchi
  Fabrizio, Amato Giuseppe, Cucchiara Rita
conference: Proceedings of the 19th International Conference on Content-based Multimedia
  Indexing
year: 2022
bibkey: messina2022aladin
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.14757'}]
tags: ["Efficiency", "Multimodal-Retrieval", "Similarity-Search", "Scalability"]
short_authors: Messina et al.
---
Image-text matching is gaining a leading role among tasks involving the joint
understanding of vision and language. In literature, this task is often used as
a pre-training objective to forge architectures able to jointly deal with
images and texts. Nonetheless, it has a direct downstream application:
cross-modal retrieval, which consists in finding images related to a given
query text or vice-versa. Solving this task is of critical importance in
cross-modal search engines. Many recent methods proposed effective solutions to
the image-text matching problem, mostly using recent large vision-language (VL)
Transformer networks. However, these models are often computationally
expensive, especially at inference time. This prevents their adoption in
large-scale cross-modal retrieval scenarios, where results should be provided
to the user almost instantaneously. In this paper, we propose to fill in the
gap between effectiveness and efficiency by proposing an ALign And DIstill
Network (ALADIN). ALADIN first produces high-effective scores by aligning at
fine-grained level images and texts. Then, it learns a shared embedding space -
where an efficient kNN search can be performed - by distilling the relevance
scores obtained from the fine-grained alignments. We obtained remarkable
results on MS-COCO, showing that our method can compete with state-of-the-art
VL Transformers while being almost 90 times faster. The code for reproducing
our results is available at https://github.com/mesnico/ALADIN.