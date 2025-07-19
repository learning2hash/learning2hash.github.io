---
layout: publication
title: 'Expressing Objects Just Like Words: Recurrent Visual Embedding For Image-text
  Matching'
authors: Chen Tianlang, Luo Jiebo
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: chen2020expressing
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.08510'}]
tags: [AAAI]
---
Existing image-text matching approaches typically infer the similarity of an
image-text pair by capturing and aggregating the affinities between the text
and each independent object of the image. However, they ignore the connections
between the objects that are semantically related. These objects may
collectively determine whether the image corresponds to a text or not. To
address this problem, we propose a Dual Path Recurrent Neural Network (DP-RNN)
which processes images and sentences symmetrically by recurrent neural networks
(RNN). In particular, given an input image-text pair, our model reorders the
image objects based on the positions of their most related words in the text.
In the same way as extracting the hidden features from word embeddings, the
model leverages RNN to extract high-level object features from the reordered
object inputs. We validate that the high-level object features contain useful
joint information of semantically related objects, which benefit the retrieval
task. To compute the image-text similarity, we incorporate a Multi-attention
Cross Matching Model into DP-RNN. It aggregates the affinity between objects
and words with cross-modality guided attention and self-attention. Our model
achieves the state-of-the-art performance on Flickr30K dataset and competitive
performance on MS-COCO dataset. Extensive experiments demonstrate the
effectiveness of our model.