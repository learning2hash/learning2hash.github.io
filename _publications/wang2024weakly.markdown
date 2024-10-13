---
layout: publication
title: Weakly Supervised Deep Hyperspherical Quantization For Image Retrieval
authors: Wang Jinpeng, Chen Bin, Zhang Qiang, Meng Zaiqiao, Liang Shangsong, Xia Shu-tao
conference: "Arxiv"
year: 2024
bibkey: wang2024weakly
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2404.04998"}
  - {name: "Code", url: "https://github.com/gimpong/AAAI21-WSDHQ"}
tags: ['ARXIV', 'Graph', 'Has Code', 'Image Retrieval', 'Quantisation', 'Supervised', 'Weakly Supervised']
---
<p>Deep quantization methods have shown high efficiency on large-scale
image retrieval. However, current models heavily rely on ground-truth
information, hindering the application of quantization in label-hungry
scenarios. A more realistic demand is to learn from inexhaustible
uploaded images that are associated with informal tags provided by
amateur users. Though such sketchy tags do not obviously reveal the
labels, they actually contain useful semantic information for
supervising deep quantization. To this end, we propose Weakly-Supervised
Deep Hyperspherical Quantization (WSDHQ), which is the first work to
learn deep quantization from weakly tagged images. Specifically, 1) we
use word embeddings to represent the tags and enhance their semantic
information based on a tag correlation graph. 2) To better preserve
semantic information in quantization codes and reduce quantization
error, we jointly learn semantics-preserving embeddings and supervised
quantizer on hypersphere by employing a well-designed fusion layer and
tailor-made loss functions. Extensive experiments show that WSDHQ can
achieve state-of-art performance on weakly-supervised compact coding.
Code is available at https://github.com/gimpong/AAAI21-WSDHQ.</p>
