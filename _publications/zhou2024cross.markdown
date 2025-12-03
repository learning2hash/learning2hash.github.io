---
layout: publication
title: 'Cross-modal Denoising: A Novel Training Paradigm For Enhancing Speech-image
  Retrieval'
authors: Lifeng Zhou, Yuke Li, Rui Deng, Yuting Yang, Haoqi Zhu
conference: Interspeech 2024
year: 2024
bibkey: zhou2024cross
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.13705'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Image Retrieval", "Interspeech"]
short_authors: Zhou et al.
---
The success of speech-image retrieval relies on establishing an effective
alignment between speech and image. Existing methods often model cross-modal
interaction through simple cosine similarity of the global feature of each
modality, which fall short in capturing fine-grained details within modalities.
To address this issue, we introduce an effective framework and a novel learning
task named cross-modal denoising (CMD) to enhance cross-modal interaction to
achieve finer-level cross-modal alignment. Specifically, CMD is a denoising
task designed to reconstruct semantic features from noisy features within one
modality by interacting features from another modality. Notably, CMD operates
exclusively during model training and can be removed during inference without
adding extra inference time. The experimental results demonstrate that our
framework outperforms the state-of-the-art method by 2.0% in mean R@1 on the
Flickr8k dataset and by 1.7% in mean R@1 on the SpokenCOCO dataset for the
speech-image retrieval tasks, respectively. These experimental results validate
the efficiency and effectiveness of our framework.