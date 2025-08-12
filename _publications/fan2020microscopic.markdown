---
layout: publication
title: Microscopic Fine-grained Instance Classification Through Deep Attention
authors: Mengran Fan, Tapabrata Chakrabort, Eric I-Chao Chang, Yan Xu, Jens Rittscher
conference: Lecture Notes in Computer Science
year: 2020
bibkey: fan2020microscopic
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.02818'}]
tags: []
short_authors: Fan et al.
---
Fine-grained classification of microscopic image data with limited samples is
an open problem in computer vision and biomedical imaging. Deep learning based
vision systems mostly deal with high number of low-resolution images, whereas
subtle detail in biomedical images require higher resolution. To bridge this
gap, we propose a simple yet effective deep network that performs two tasks
simultaneously in an end-to-end manner. First, it utilises a gated attention
module that can focus on multiple key instances at high resolution without
extra annotations or region proposals. Second, the global structural features
and local instance features are fused for final image level classification. The
result is a robust but lightweight end-to-end trainable deep network that
yields state-of-the-art results in two separate fine-grained multi-instance
biomedical image classification tasks: a benchmark breast cancer histology
dataset and our new fungi species mycology dataset. In addition, we demonstrate
the interpretability of the proposed model by visualising the concordance of
the learned features with clinically relevant features.