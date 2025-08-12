---
layout: publication
title: Automatic Tagging Using Deep Convolutional Neural Networks
authors: Keunwoo Choi, George Fazekas, Mark Sandler
conference: Arxiv
year: 2016
bibkey: choi2016automatic
citations: 221
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.00298'}]
tags: ["Datasets", "Evaluation"]
short_authors: Keunwoo Choi, George Fazekas, Mark Sandler
---
We present a content-based automatic music tagging algorithm using fully
convolutional neural networks (FCNs). We evaluate different architectures
consisting of 2D convolutional layers and subsampling layers only. In the
experiments, we measure the AUC-ROC scores of the architectures with different
complexities and input types using the MagnaTagATune dataset, where a 4-layer
architecture shows state-of-the-art performance with mel-spectrogram input.
Furthermore, we evaluated the performances of the architectures with varying
the number of layers on a larger dataset (Million Song Dataset), and found that
deeper models outperformed the 4-layer architecture. The experiments show that
mel-spectrogram is an effective time-frequency representation for automatic
tagging and that more complex models benefit from more training data.