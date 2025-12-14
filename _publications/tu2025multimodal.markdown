---
layout: publication
title: Multimodal Reasoning Agent For Zero-shot Composed Image Retrieval
authors: Rong-Cheng Tu, Wenhao Sun, Hanzhe You, Yingjie Wang, Jiaxing Huang, Li Shen,
  Dacheng Tao
conference: Arxiv
year: 2025
bibkey: tu2025multimodal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.19952'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Self-Supervised, Datasets,
  Tools & Libraries]
short_authors: Tu et al.
---
Zero-Shot Composed Image Retrieval (ZS-CIR) aims to retrieve target images given a compositional query, consisting of a reference image and a modifying text-without relying on annotated training data. Existing approaches often generate a synthetic target text using large language models (LLMs) to serve as an intermediate anchor between the compositional query and the target image. Models are then trained to align the compositional query with the generated text, and separately align images with their corresponding texts using contrastive learning. However, this reliance on intermediate text introduces error propagation, as inaccuracies in query-to-text and text-to-image mappings accumulate, ultimately degrading retrieval performance. To address these problems, we propose a novel framework by employing a Multimodal Reasoning Agent (MRA) for ZS-CIR. MRA eliminates the dependence on textual intermediaries by directly constructing triplets, <reference image, modification text, target image>, using only unlabeled image data. By training on these synthetic triplets, our model learns to capture the relationships between compositional queries and candidate images directly. Extensive experiments on three standard CIR benchmarks demonstrate the effectiveness of our approach. On the FashionIQ dataset, our method improves Average R@10 by at least 7.5% over existing baselines; on CIRR, it boosts R@1 by 9.6%; and on CIRCO, it increases mAP@5 by 9.5%.