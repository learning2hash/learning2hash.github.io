---
layout: publication
title: Towards Book Cover Design Via Layout Graphs
authors: Wensheng Zhang, Yan Zheng, Taiga Miyazono, Seiichi Uchida, Brian Kenji Iwana
conference: Lecture Notes in Computer Science
year: 2021
bibkey: zhang2021towards
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.11088'}]
tags: []
short_authors: Zhang et al.
---
Book covers are intentionally designed and provide an introduction to a book.
However, they typically require professional skills to design and produce the
cover images. Thus, we propose a generative neural network that can produce
book covers based on an easy-to-use layout graph. The layout graph contains
objects such as text, natural scene objects, and solid color spaces. This
layout graph is embedded using a graph convolutional neural network and then
used with a mask proposal generator and a bounding-box generator and filled
using an object proposal generator. Next, the objects are compiled into a
single image and the entire network is trained using a combination of
adversarial training, perceptual training, and reconstruction. Finally, a Style
Retention Network (SRNet) is used to transfer the learned font style onto the
desired text. Using the proposed method allows for easily controlled and unique
book covers.