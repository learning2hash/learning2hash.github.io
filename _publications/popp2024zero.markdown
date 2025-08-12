---
layout: publication
title: 'Zero-shot Distillation For Image Encoders: How To Make Effective Use Of Synthetic
  Data'
authors: Niclas Popp, Jan Hendrik Metzen, Matthias Hein
conference: Arxiv
year: 2024
bibkey: popp2024zero
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.16637'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Niclas Popp, Jan Hendrik Metzen, Matthias Hein
---
Multi-modal foundation models such as CLIP have showcased impressive
zero-shot capabilities. However, their applicability in resource-constrained
environments is limited due to their large number of parameters and high
inference time. While existing approaches have scaled down the entire CLIP
architecture, we focus on training smaller variants of the image encoder, which
suffices for efficient zero-shot classification. The use of synthetic data has
shown promise in distilling representations from larger teachers, resulting in
strong few-shot and linear probe performance. However, we find that this
approach surprisingly fails in true zero-shot settings when using contrastive
losses. We identify the exploitation of spurious features as being responsible
for poor generalization between synthetic and real data. However, by using the
image feature-based L2 distillation loss, we mitigate these problems and train
students that achieve zero-shot performance which on four domain-specific
datasets is on-par with a ViT-B/32 teacher model trained on DataCompXL, while
featuring up to 92% fewer parameters.