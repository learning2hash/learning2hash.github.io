---
layout: publication
title: An Efficient Post-hoc Framework For Reducing Task Discrepancy Of Text Encoders
  For Composed Image Retrieval
authors: Jaeseok Byun, Seokhyeon Jeong, Wonjae Kim, Sanghyuk Chun, Taesup Moon
conference: Arxiv
year: 2024
bibkey: byun2024an
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.09188'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval", "Self-Supervised", "Supervised", "Text Retrieval"]
short_authors: Byun et al.
---
Composed Image Retrieval (CIR) aims to retrieve a target image based on a
reference image and conditioning text, enabling controllable image searches.
The mainstream Zero-Shot (ZS) CIR methods bypass the need for expensive
training CIR triplets by projecting image embeddings into the text token
embedding space, forming a composed query for retrieval. However, we highlight
an inherent limitation in these projection-based CIR: a task discrepancy of
text encoders between the original pre-training task of the encoders (text
\(\leftrightarrow\) image) and the target CIR task (image + text
\(\leftrightarrow\) image), which potentially negatively impacts CIR performance.
To reduce such a discrepancy, a naive solution would be to train both image and
text encoders with CIR triplets in a supervised manner. Instead, we introduce
Reducing Task Discrepancy of Text Encoders (RTD), an efficient text-only
post-hoc framework that complements projection-based CIR methods. We devise a
novel target-anchored text contrastive learning designed to enhance the
capability of the text encoder for CIR. We also propose two key enhancements:
(1) a hard negative-based refined batch sampling strategy and (2) a refined
concatenation scheme to further mitigate training-inference discrepancy.
Integrating RTD into state-of-the-art projection-based methods achieves
performance comparable to, or even surpassing, resource-intensive
state-of-the-art synthetic CIR triplet-based approaches only with 23 minutes of
additional training on 4 A100 GPUs (up to \(100\times\) faster in training). Our
code will be available upon acceptance.