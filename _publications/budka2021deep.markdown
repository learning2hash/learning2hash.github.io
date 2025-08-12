---
layout: publication
title: Deep Multilabel CNN For Forensic Footwear Impression Descriptor Identification
authors: Marcin Budka, Akanda Wahid Ul Ashraf, Scott Neville, Alun MacKrill, Matthew
  Bennett
conference: Applied Soft Computing
year: 2021
bibkey: budka2021deep
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.05090'}]
tags: []
short_authors: Budka et al.
---
In recent years deep neural networks have become the workhorse of computer
vision. In this paper, we employ a deep learning approach to classify footwear
impression's features known as *descriptors* for forensic use cases.
Within this process, we develop and evaluate an effective technique for feeding
downsampled greyscale impressions to a neural network pre-trained on data from
a different domain. Our approach relies on learnable preprocessing layer paired
with multiple interpolation methods used in parallel. We empirically show that
this technique outperforms using a single type of interpolated image without
learnable preprocessing, and can help to avoid the computational penalty
related to using high resolution inputs, by making more efficient use of the
low resolution inputs. We also investigate the effect of preserving the aspect
ratio of the inputs, which leads to considerable boost in accuracy without
increasing the computational budget with respect to squished rectangular
images. Finally, we formulate a set of best practices for transfer learning
with greyscale inputs, potentially widely applicable in computer vision tasks
ranging from footwear impression classification to medical imaging.