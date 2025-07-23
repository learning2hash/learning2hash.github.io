---
layout: publication
title: A Probabilistic Approach For Learning Embeddings Without Supervision
authors: Dutta Ujjal Kr, Harandi Mehrtash, Chellu Chandra Sekhar
conference: Arxiv
year: 2019
bibkey: dutta2019probabilistic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08275'}]
tags: ["Distance Metric Learning", "Few-shot & Zero-shot", "Unsupervised"]
short_authors: Dutta Ujjal Kr, Harandi Mehrtash, Chellu Chandra Sekhar
---
For challenging machine learning problems such as zero-shot learning and
fine-grained categorization, embedding learning is the machinery of choice
because of its ability to learn generic notions of similarity, as opposed to
class-specific concepts in standard classification models. Embedding learning
aims at learning discriminative representations of data such that similar
examples are pulled closer, while pushing away dissimilar ones. Despite their
exemplary performances, supervised embedding learning approaches require huge
number of annotations for training. This restricts their applicability for
large datasets in new applications where obtaining labels require extensive
manual efforts and domain knowledge. In this paper, we propose to learn an
embedding in a completely unsupervised manner without using any class labels.
Using a graph-based clustering approach to obtain pseudo-labels, we form
triplet-based constraints following a metric learning paradigm. Our novel
embedding learning approach uses a probabilistic notion, that intuitively
minimizes the chances of each triplet violating a geometric constraint. Due to
nature of the search space, we learn the parameters of our approach using
Riemannian geometry. Our proposed approach performs competitive to
state-of-the-art approaches.