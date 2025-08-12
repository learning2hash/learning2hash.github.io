---
layout: publication
title: Binary Patterns Encoded Convolutional Neural Networks For Texture Recognition
  And Remote Sensing Scene Classification
authors: Rao Muhammad Anwer, Fahad Shahbaz Khan, Joost van de Weijer, Matthieu Molinier,
  Jorma Laaksonen
conference: ISPRS Journal of Photogrammetry and Remote Sensing
year: 2018
bibkey: anwer2017binary
citations: 263
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.01171'}]
tags: []
short_authors: Anwer et al.
---
Designing discriminative powerful texture features robust to realistic
imaging conditions is a challenging computer vision problem with many
applications, including material recognition and analysis of satellite or
aerial imagery. In the past, most texture description approaches were based on
dense orderless statistical distribution of local features. However, most
recent approaches to texture recognition and remote sensing scene
classification are based on Convolutional Neural Networks (CNNs). The d facto
practice when learning these CNN models is to use RGB patches as input with
training performed on large amounts of labeled data (ImageNet). In this paper,
we show that Binary Patterns encoded CNN models, codenamed TEX-Nets, trained
using mapped coded images with explicit texture information provide
complementary information to the standard RGB deep models. Additionally, two
deep architectures, namely early and late fusion, are investigated to combine
the texture and color information. To the best of our knowledge, we are the
first to investigate Binary Patterns encoded CNNs and different deep network
fusion architectures for texture recognition and remote sensing scene
classification. We perform comprehensive experiments on four texture
recognition datasets and four remote sensing scene classification benchmarks:
UC-Merced with 21 scene categories, WHU-RS19 with 19 scene classes, RSSCN7 with
7 categories and the recently introduced large scale aerial image dataset (AID)
with 30 aerial scene types. We demonstrate that TEX-Nets provide complementary
information to standard RGB deep model of the same network architecture. Our
late fusion TEX-Net architecture always improves the overall performance
compared to the standard RGB network on both recognition problems. Our final
combination outperforms the state-of-the-art without employing fine-tuning or
ensemble of RGB network architectures.