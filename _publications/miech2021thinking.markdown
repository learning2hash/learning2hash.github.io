---
layout: publication
title: 'Thinking Fast And Slow: Efficient Text-to-visual Retrieval With Transformers'
authors: Antoine Miech, Jean-Baptiste Alayrac, Ivan Laptev, Josef Sivic, Andrew Zisserman
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: miech2021thinking
citations: 111
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16553'}]
tags: ["CVPR", "Similarity Search"]
short_authors: Miech et al.
---
Our objective is language-based search of large-scale image and video
datasets. For this task, the approach that consists of independently mapping
text and vision to a joint embedding space, a.k.a. dual encoders, is attractive
as retrieval scales and is efficient for billions of images using approximate
nearest neighbour search. An alternative approach of using vision-text
transformers with cross-attention gives considerable improvements in accuracy
over the joint embeddings, but is often inapplicable in practice for
large-scale retrieval given the cost of the cross-attention mechanisms required
for each sample at test time. This work combines the best of both worlds. We
make the following three contributions. First, we equip transformer-based
models with a new fine-grained cross-attention architecture, providing
significant improvements in retrieval accuracy whilst preserving scalability.
Second, we introduce a generic approach for combining a Fast dual encoder model
with our Slow but accurate transformer-based model via distillation and
re-ranking. Finally, we validate our approach on the Flickr30K image dataset
where we show an increase in inference speed by several orders of magnitude
while having results competitive to the state of the art. We also extend our
method to the video domain, improving the state of the art on the VATEX
dataset.