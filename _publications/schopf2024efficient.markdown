---
layout: publication
title: Efficient Few-shot Learning For Multi-label Classification Of Scientific Documents
  With Many Classes
authors: Tim Schopf, Alexander Blatzheim, Nektarios MacHner, Florian Matthes
conference: Arxiv
year: 2024
bibkey: schopf2024efficient
citations: 0
additional_links: [{name: Code, url: 'https://github.com/sebischair/FusionSent'},
  {name: Paper, url: 'https://arxiv.org/abs/2410.05770'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Schopf et al.
---
Scientific document classification is a critical task and often involves many
classes. However, collecting human-labeled data for many classes is expensive
and usually leads to label-scarce scenarios. Moreover, recent work has shown
that sentence embedding model fine-tuning for few-shot classification is
efficient, robust, and effective. In this work, we propose FusionSent
(Fusion-based Sentence Embedding Fine-tuning), an efficient and prompt-free
approach for few-shot classification of scientific documents with many classes.
FusionSent uses available training examples and their respective label texts to
contrastively fine-tune two different sentence embedding models. Afterward, the
parameters of both fine-tuned models are fused to combine the complementary
knowledge from the separate fine-tuning steps into a single model. Finally, the
resulting sentence embedding model is frozen to embed the training instances,
which are then used as input features to train a classification head. Our
experiments show that FusionSent significantly outperforms strong baselines by
an average of \(6.0\) \(F_\{1\}\) points across multiple scientific document
classification datasets. In addition, we introduce a new dataset for
multi-label classification of scientific documents, which contains 203,961
scientific articles and 130 classes from the arXiv category taxonomy. Code and
data are available at https://github.com/sebischair/FusionSent.