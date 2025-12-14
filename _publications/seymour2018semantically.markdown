---
layout: publication
title: Semantically-aware Attentive Neural Embeddings For Image-based Visual Localization
authors: Zachary Seymour, Karan Sikka, Han-Pang Chiu, Supun Samarasekera, Rakesh Kumar
conference: Arxiv
year: 2018
bibkey: seymour2018semantically
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.03402'}]
tags: [Tools & Libraries, Datasets]
short_authors: Seymour et al.
---
We present an approach that combines appearance and semantic information for
2D image-based localization (2D-VL) across large perceptual changes and time
lags. Compared to appearance features, the semantic layout of a scene is
generally more invariant to appearance variations. We use this intuition and
propose a novel end-to-end deep attention-based framework that utilizes
multimodal cues to generate robust embeddings for 2D-VL. The proposed attention
module predicts a shared channel attention and modality-specific spatial
attentions to guide the embeddings to focus on more reliable image regions. We
evaluate our model against state-of-the-art (SOTA) methods on three challenging
localization datasets. We report an average (absolute) improvement of \(19%\)
over current SOTA for 2D-VL. Furthermore, we present an extensive study
demonstrating the contribution of each component of our model, showing
\(8\)--\(15%\) and \(4%\) improvement from adding semantic information and our
proposed attention module. We finally show the predicted attention maps to
offer useful insights into our model.