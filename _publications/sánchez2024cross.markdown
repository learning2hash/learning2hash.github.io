---
layout: publication
title: Cross-modal Coordination Across A Diverse Set Of Input Modalities
authors: "Jorge S\xE1nchez, Rodrigo Laguna"
conference: Arxiv
year: 2024
bibkey: "s\xE1nchez2024cross"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.16347'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: "Jorge S\xE1nchez, Rodrigo Laguna"
---
Cross-modal retrieval is the task of retrieving samples of a given modality
by using queries of a different one. Due to the wide range of practical
applications, the problem has been mainly focused on the vision and language
case, e.g. text to image retrieval, where models like CLIP have proven
effective in solving such tasks. The dominant approach to learning such
coordinated representations consists of projecting them onto a common space
where matching views stay close and those from non-matching pairs are pushed
away from each other. Although this cross-modal coordination has been applied
also to other pairwise combinations, extending it to an arbitrary number of
diverse modalities is a problem that has not been fully explored in the
literature. In this paper, we propose two different approaches to the problem.
The first is based on an extension of the CLIP contrastive objective to an
arbitrary number of input modalities, while the second departs from the
contrastive formulation and tackles the coordination problem by regressing the
cross-modal similarities towards a target that reflects two simple and
intuitive constraints of the cross-modal retrieval task. We run experiments on
two different datasets, over different combinations of input modalities and
show that the approach is not only simple and effective but also allows for
tackling the retrieval problem in novel ways. Besides capturing a more diverse
set of pair-wise interactions, we show that we can use the learned
representations to improve retrieval performance by combining the embeddings
from two or more such modalities.