---
layout: publication
title: Context-aware Attentional Pooling (CAP) For Fine-grained Visual Classification
authors: Ardhendu Behera, Zachary Wharton, Pradeep Hewage, Asish Bera
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: behera2021context
citations: 91
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.06635'}]
tags: ["AAAI"]
short_authors: Behera et al.
---
Deep convolutional neural networks (CNNs) have shown a strong ability in
mining discriminative object pose and parts information for image recognition.
For fine-grained recognition, context-aware rich feature representation of
object/scene plays a key role since it exhibits a significant variance in the
same subcategory and subtle variance among different subcategories. Finding the
subtle variance that fully characterizes the object/scene is not
straightforward. To address this, we propose a novel context-aware attentional
pooling (CAP) that effectively captures subtle changes via sub-pixel gradients,
and learns to attend informative integral regions and their importance in
discriminating different subcategories without requiring the bounding-box
and/or distinguishable part annotations. We also introduce a novel feature
encoding by considering the intrinsic consistency between the informativeness
of the integral regions and their spatial structures to capture the semantic
correlation among them. Our approach is simple yet extremely effective and can
be easily applied on top of a standard classification backbone network. We
evaluate our approach using six state-of-the-art (SotA) backbone networks and
eight benchmark datasets. Our method significantly outperforms the SotA
approaches on six datasets and is very competitive with the remaining two.