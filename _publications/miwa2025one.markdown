---
layout: publication
title: 'One-d-piece: Image Tokenizer Meets Quality-controllable Compression'
authors: Keita Miwa, Kento Sasaki, Hidehisa Arai, Tsubasa Takahashi, Yu Yamaguchi
conference: Arxiv
year: 2025
bibkey: miwa2025one
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.10064'}]
tags: ["Efficiency"]
short_authors: Miwa et al.
---
Current image tokenization methods require a large number of tokens to
capture the information contained within images. Although the amount of
information varies across images, most image tokenizers only support
fixed-length tokenization, leading to inefficiency in token allocation. In this
study, we introduce One-D-Piece, a discrete image tokenizer designed for
variable-length tokenization, achieving quality-controllable mechanism. To
enable variable compression rate, we introduce a simple but effective
regularization mechanism named "Tail Token Drop" into discrete one-dimensional
image tokenizers. This method encourages critical information to concentrate at
the head of the token sequence, enabling support of variadic tokenization,
while preserving state-of-the-art reconstruction quality. We evaluate our
tokenizer across multiple reconstruction quality metrics and find that it
delivers significantly better perceptual quality than existing
quality-controllable compression methods, including JPEG and WebP, at smaller
byte sizes. Furthermore, we assess our tokenizer on various downstream computer
vision tasks, including image classification, object detection, semantic
segmentation, and depth estimation, confirming its adaptability to numerous
applications compared to other variable-rate methods. Our approach demonstrates
the versatility of variable-length discrete image tokenization, establishing a
new paradigm in both compression efficiency and reconstruction performance.
Finally, we validate the effectiveness of tail token drop via detailed analysis
of tokenizers.