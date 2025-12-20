---
layout: publication
title: 'MVAM: Multi-view Attention Method For Fine-grained Image-text Matching'
authors: Wanqing Cui, Rui Cheng, Jiafeng Guo, Xueqi Cheng
conference: Arxiv
year: 2024
bibkey: cui2024mvam
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17237'}]
tags: ["Evaluation"]
short_authors: Cui et al.
---
Existing two-stream models, such as CLIP, encode images and text through
independent representations, showing good performance while ensuring retrieval
speed, have attracted attention from industry and academia. However, the single
representation often struggles to capture complex content fully. Such models
may ignore fine-grained information during matching, resulting in suboptimal
retrieval results. To overcome this limitation and enhance the performance of
two-stream models, we propose a Multi-view Attention Method (MVAM) for
image-text matching. This approach leverages diverse attention heads with
unique view codes to learn multiple representations for images and text, which
are then concatenated for matching. We also incorporate a diversity objective
to explicitly encourage attention heads to focus on distinct aspects of the
input data, capturing complementary fine-grained details. This diversity
enables the model to represent image-text pairs from multiple perspectives,
ensuring a more comprehensive understanding and alignment of critical content.
Our method allows models to encode images and text from different perspectives
and focus on more critical details, leading to better matching performance. Our
experiments on MSCOCO and Flickr30K demonstrate enhancements over existing
models, and further case studies reveal that different attention heads can
focus on distinct content, achieving more comprehensive representations.