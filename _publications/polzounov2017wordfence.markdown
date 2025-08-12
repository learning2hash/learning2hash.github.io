---
layout: publication
title: 'Wordfence: Text Detection In Natural Images With Border Awareness'
authors: Andrei Polzounov, Artsiom Ablavatski, Sergio Escalera, Shijian Lu, Jianfei
  Cai
conference: 2017 IEEE International Conference on Image Processing (ICIP)
year: 2017
bibkey: polzounov2017wordfence
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.05483'}]
tags: []
short_authors: Polzounov et al.
---
In recent years, text recognition has achieved remarkable success in
recognizing scanned document text. However, word recognition in natural images
is still an open problem, which generally requires time consuming
post-processing steps. We present a novel architecture for individual word
detection in scene images based on semantic segmentation. Our contributions are
twofold: the concept of WordFence, which detects border areas surrounding each
individual word and a novel pixelwise weighted softmax loss function which
penalizes background and emphasizes small text regions. WordFence ensures that
each word is detected individually, and the new loss function provides a strong
training signal to both text and word border localization. The proposed
technique avoids intensive post-processing, producing an end-to-end word
detection system. We achieve superior localization recall on common benchmark
datasets - 92% recall on ICDAR11 and ICDAR13 and 63% recall on SVT.
Furthermore, our end-to-end word recognition system achieves state-of-the-art
86% F-Score on ICDAR13.