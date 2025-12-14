---
layout: publication
title: 'Scaleface: Uncertainty-aware Deep Metric Learning'
authors: Roman Kail, Kirill Fedyanin, Nikita Muravev, Alexey Zaytsev, Maxim Panov
conference: Arxiv
year: 2022
bibkey: kail2022scaleface
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.01880'}]
tags: [Evaluation, Image Retrieval, Neural Hashing, Distance Metric Learning, Multimodal
    Retrieval]
short_authors: Kail et al.
---
The performance of modern deep learning-based systems dramatically depends on
the quality of input objects. For example, face recognition quality would be
lower for blurry or corrupted inputs. However, it is hard to predict the
influence of input quality on the resulting accuracy in more complex scenarios.
We propose an approach for deep metric learning that allows direct estimation
of the uncertainty with almost no additional computational cost. The developed
\textit\{ScaleFace\} algorithm uses trainable scale values that modify
similarities in the space of embeddings. These input-dependent scale values
represent a measure of confidence in the recognition result, thus allowing
uncertainty estimation. We provide comprehensive experiments on face
recognition tasks that show the superior performance of ScaleFace compared to
other uncertainty-aware face recognition approaches. We also extend the results
to the task of text-to-image retrieval showing that the proposed approach beats
the competitors with significant margin.