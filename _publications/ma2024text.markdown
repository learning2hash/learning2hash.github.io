---
layout: publication
title: Text-region Matching For Multi-label Image Recognition With Missing Labels
authors: Leilei Ma, Hongxing Xie, Lei Wang, Yanping Fu, Dengdi Sun, Haifeng Zhao
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: ma2024text
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yu-gi-oh-leilei/TRM-ML'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.18520'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ma et al.
---
Recently, large-scale visual language pre-trained (VLP) models have
demonstrated impressive performance across various downstream tasks. Motivated
by these advancements, pioneering efforts have emerged in multi-label image
recognition with missing labels, leveraging VLP prompt-tuning technology.
However, they usually cannot match text and vision features well, due to
complicated semantics gaps and missing labels in a multi-label image. To tackle
this challenge, we propose \(\textbf\{T\}\)ext-\(\textbf\{R\}\)egion
\(\textbf\{M\}\)atching for optimizing \(\textbf\{M\}\)ulti-\(\textbf\{L\}\)abel prompt
tuning, namely TRM-ML, a novel method for enhancing meaningful cross-modal
matching. Compared to existing methods, we advocate exploring the information
of category-aware regions rather than the entire image or pixels, which
contributes to bridging the semantic gap between textual and visual
representations in a one-to-one matching manner. Concurrently, we further
introduce multimodal contrastive learning to narrow the semantic gap between
textual and visual modalities and establish intra-class and inter-class
relationships. Additionally, to deal with missing labels, we propose a
multimodal category prototype that leverages intra- and inter-category semantic
relationships to estimate unknown labels, facilitating pseudo-label generation.
Extensive experiments on the MS-COCO, PASCAL VOC, Visual Genome, NUS-WIDE, and
CUB-200-211 benchmark datasets demonstrate that our proposed framework
outperforms the state-of-the-art methods by a significant margin. Our code is
available here: https://github.com/yu-gi-oh-leilei/TRM-ML.