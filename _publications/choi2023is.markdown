---
layout: publication
title: Is Cross-modal Information Retrieval Possible Without Training?
authors: Hyunjin Choi, Hyunjae Lee, Seongho Joe, Youngjune L. Gwon
conference: Advances in Information Retrieval 45th European Conference on Information
  Retrieval ECIR 2023 Dublin Ireland Proceedings Part II
year: 2023
bibkey: choi2023is
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11095'}]
tags: [Text Retrieval, ECIR, Self-Supervised, Multimodal Retrieval, Evaluation, Neural
    Hashing]
short_authors: Choi et al.
---
Encoded representations from a pretrained deep learning model (e.g., BERT
text embeddings, penultimate CNN layer activations of an image) convey a rich
set of features beneficial for information retrieval. Embeddings for a
particular modality of data occupy a high-dimensional space of its own, but it
can be semantically aligned to another by a simple mapping without training a
deep neural net. In this paper, we take a simple mapping computed from the
least squares and singular value decomposition (SVD) for a solution to the
Procrustes problem to serve a means to cross-modal information retrieval. That
is, given information in one modality such as text, the mapping helps us locate
a semantically equivalent data item in another modality such as image. Using
off-the-shelf pretrained deep learning models, we have experimented the
aforementioned simple cross-modal mappings in tasks of text-to-image and
image-to-text retrieval. Despite simplicity, our mappings perform reasonably
well reaching the highest accuracy of 77% on recall@10, which is comparable to
those requiring costly neural net training and fine-tuning. We have improved
the simple mappings by contrastive learning on the pretrained models.
Contrastive learning can be thought as properly biasing the pretrained encoders
to enhance the cross-modal mapping quality. We have further improved the
performance by multilayer perceptron with gating (gMLP), a simple neural
architecture.