---
layout: publication
title: Stylized Face Sketch Extraction Via Generative Prior With Limited Data
authors: Kwan Yun, Kwanggyoon Seo, Chang Wook Seo, Soyeon Yoon, Seongcheol Kim, Soohyun
  Ji, Amirsaman Ashtari, Junyong Noh
conference: Computer Graphics Forum
year: 2024
bibkey: yun2024stylized
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.11263'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yun et al.
---
Facial sketches are both a concise way of showing the identity of a person
and a means to express artistic intention. While a few techniques have recently
emerged that allow sketches to be extracted in different styles, they typically
rely on a large amount of data that is difficult to obtain. Here, we propose
StyleSketch, a method for extracting high-resolution stylized sketches from a
face image. Using the rich semantics of the deep features from a pretrained
StyleGAN, we are able to train a sketch generator with 16 pairs of face and the
corresponding sketch images. The sketch generator utilizes part-based losses
with two-stage learning for fast convergence during training for high-quality
sketch extraction. Through a set of comparisons, we show that StyleSketch
outperforms existing state-of-the-art sketch extraction methods and few-shot
image adaptation methods for the task of extracting high-resolution abstract
face sketches. We further demonstrate the versatility of StyleSketch by
extending its use to other domains and explore the possibility of semantic
editing. The project page can be found in
https://kwanyun.github.io/stylesketch_project.