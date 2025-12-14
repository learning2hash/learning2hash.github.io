---
layout: publication
title: Three-stream Joint Network For Zero-shot Sketch-based Image Retrieval
authors: Yu-Wei Zhan, Xin Luo, Yongxin Wang, Zhen-Duo Chen, Xin-Shun Xu
conference: Arxiv
year: 2022
bibkey: zhan2022three
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.05666'}]
tags: [Image Retrieval, Few-shot & Zero-shot, Datasets]
short_authors: Zhan et al.
---
The Zero-Shot Sketch-based Image Retrieval (ZS-SBIR) is a challenging task
because of the large domain gap between sketches and natural images as well as
the semantic inconsistency between seen and unseen categories. Previous
literature bridges seen and unseen categories by semantic embedding, which
requires prior knowledge of the exact class names and additional extraction
efforts. And most works reduce domain gap by mapping sketches and natural
images into a common high-level space using constructed sketch-image pairs,
which ignore the unpaired information between images and sketches. To address
these issues, in this paper, we propose a novel Three-Stream Joint Training
Network (3JOIN) for the ZS-SBIR task. To narrow the domain differences between
sketches and images, we extract edge maps for natural images and treat them as
a bridge between images and sketches, which have similar content to images and
similar style to sketches. For exploiting a sufficient combination of sketches,
natural images, and edge maps, a novel three-stream joint training network is
proposed. In addition, we use a teacher network to extract the implicit
semantics of the samples without the aid of other semantics and transfer the
learned knowledge to unseen classes. Extensive experiments conducted on two
real-world datasets demonstrate the superiority of our proposed method.