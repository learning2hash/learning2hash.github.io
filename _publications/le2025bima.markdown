---
layout: publication
title: 'Bima: Towards Biases Mitigation For Text-video Retrieval Via Scene Element
  Guidance'
authors: Huy Le, Nhat Chung, Tung Kieu, Anh Nguyen, Ngan Le
conference: Proceedings of the 33rd ACM International Conference on Multimedia
year: 2025
bibkey: le2025bima
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.03589'}]
tags: [Video Retrieval, Evaluation, Tools & Libraries, Datasets]
short_authors: Le et al.
---
Text-video retrieval (TVR) systems often suffer from visual-linguistic biases present in datasets, which cause pre-trained vision-language models to overlook key details. To address this, we propose BiMa, a novel framework designed to mitigate biases in both visual and textual representations. Our approach begins by generating scene elements that characterize each video by identifying relevant entities/objects and activities. For visual debiasing, we integrate these scene elements into the video embeddings, enhancing them to emphasize fine-grained and salient details. For textual debiasing, we introduce a mechanism to disentangle text features into content and bias components, enabling the model to focus on meaningful content while separately handling biased information. Extensive experiments and ablation studies across five major TVR benchmarks (i.e., MSR-VTT, MSVD, LSMDC, ActivityNet, and DiDeMo) demonstrate the competitive performance of BiMa. Additionally, the model's bias mitigation capability is consistently validated by its strong results on out-of-distribution retrieval tasks.