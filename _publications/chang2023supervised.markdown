---
layout: publication
title: Supervised Contrastive Learning For Fine-grained Chromosome Recognition
authors: Ruijia Chang, Suncheng Xiang, Chengyu Zhou, Kui Su, Dahong Qian, Jun Wang
conference: Arxiv
year: 2023
bibkey: chang2023supervised
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.07623'}]
tags: ["Self-Supervised", "Supervised"]
short_authors: Chang et al.
---
Chromosome recognition is an essential task in karyotyping, which plays a
vital role in birth defect diagnosis and biomedical research. However, existing
classification methods face significant challenges due to the inter-class
similarity and intra-class variation of chromosomes. To address this issue, we
propose a supervised contrastive learning strategy that is tailored to train
model-agnostic deep networks for reliable chromosome classification. This
method enables extracting fine-grained chromosomal embeddings in latent space.
These embeddings effectively expand inter-class boundaries and reduce
intra-class variations, enhancing their distinctiveness in predicting
chromosome types. On top of two large-scale chromosome datasets, we
comprehensively validate the power of our contrastive learning strategy in
boosting cutting-edge deep networks such as Transformers and ResNets. Extensive
results demonstrate that it can significantly improve models' generalization
performance, with an accuracy improvement up to +4.5%. Codes and pretrained
models will be released upon acceptance of this work.