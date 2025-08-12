---
layout: publication
title: Enhancing Performance Of Vision Transformers On Small Datasets Through Local
  Inductive Bias Incorporation
authors: Ibrahim Batuhan Akkaya, Senthilkumar S. Kathiresan, Elahe Arani, Bahram Zonooz
conference: Pattern Recognition
year: 2024
bibkey: akkaya2023enhancing
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.08551'}]
tags: ["Datasets"]
short_authors: Akkaya et al.
---
Vision transformers (ViTs) achieve remarkable performance on large datasets,
but tend to perform worse than convolutional neural networks (CNNs) when
trained from scratch on smaller datasets, possibly due to a lack of local
inductive bias in the architecture. Recent studies have therefore added
locality to the architecture and demonstrated that it can help ViTs achieve
performance comparable to CNNs in the small-size dataset regime. Existing
methods, however, are architecture-specific or have higher computational and
memory costs. Thus, we propose a module called Local InFormation Enhancer
(LIFE) that extracts patch-level local information and incorporates it into the
embeddings used in the self-attention block of ViTs. Our proposed module is
memory and computation efficient, as well as flexible enough to process
auxiliary tokens such as the classification and distillation tokens. Empirical
results show that the addition of the LIFE module improves the performance of
ViTs on small image classification datasets. We further demonstrate how the
effect can be extended to downstream tasks, such as object detection and
semantic segmentation. In addition, we introduce a new visualization method,
Dense Attention Roll-Out, specifically designed for dense prediction tasks,
allowing the generation of class-specific attention maps utilizing the
attention maps of all tokens.