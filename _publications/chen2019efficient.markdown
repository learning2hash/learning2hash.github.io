---
layout: publication
title: Efficient Object Embedding for Spliced Image Retrieval
authors: Chen Bor-chun, Wu Zuxuan, Davis Larry S., Lim Ser-nam
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: chen2019efficient
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.11903'}]
tags: ["CVPR", "Evaluation", "Tools-&-Libraries", "Image-Retrieval"]
short_authors: Chen et al.
---
Detecting spliced images is one of the emerging challenges in computer
vision. Unlike prior methods that focus on detecting low-level artifacts
generated during the manipulation process, we use an image retrieval approach
to tackle this problem. When given a spliced query image, our goal is to
retrieve the original image from a database of authentic images. To achieve
this goal, we propose representing an image by its constituent objects based on
the intuition that the finest granularity of manipulations is oftentimes at the
object-level. We introduce a framework, object embeddings for spliced image
retrieval (OE-SIR), that utilizes modern object detectors to localize object
regions. Each region is then embedded and collectively used to represent the
image. Further, we propose a student-teacher training paradigm for learning
discriminative embeddings within object regions to avoid expensive multiple
forward passes. Detailed analysis of the efficacy of different feature
embedding models is also provided in this study. Extensive experimental results
show that the OE-SIR achieves state-of-the-art performance in spliced image
retrieval.