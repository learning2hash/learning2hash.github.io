---
layout: publication
title: Anti-compression Contrastive Facial Forgery Detection
authors: Jiajun Huang, Xinqi Zhu, Chengbin Du, Siqi Ma, Surya Nepal, Chang Xu
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: huang2023anti
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06183'}]
tags: ["Self-Supervised"]
short_authors: Huang et al.
---
Forgery facial images and videos have increased the concern of digital
security. It leads to the significant development of detecting forgery data
recently. However, the data, especially the videos published on the Internet,
are usually compressed with lossy compression algorithms such as H.264. The
compressed data could significantly degrade the performance of recent detection
algorithms. The existing anti-compression algorithms focus on enhancing the
performance in detecting heavily compressed data but less consider the
compression adaption to the data from various compression levels. We believe
creating a forgery detection model that can handle the data compressed with
unknown levels is important. To enhance the performance for such models, we
consider the weak compressed and strong compressed data as two views of the
original data and they should have similar representation and relationships
with other samples. We propose a novel anti-compression forgery detection
framework by maintaining closer relations within data under different
compression levels. Specifically, the algorithm measures the pair-wise
similarity within data as the relations, and forcing the relations of weak and
strong compressed data close to each other, thus improving the discriminate
power for detecting strong compressed data. To achieve a better strong
compressed data relation guided by the less compressed one, we apply video
level contrastive learning for weak compressed data, which forces the model to
produce similar representations within the same video and far from the negative
samples. The experiment results show that the proposed algorithm could boost
performance for strong compressed data while improving the accuracy rate when
detecting the clean data.