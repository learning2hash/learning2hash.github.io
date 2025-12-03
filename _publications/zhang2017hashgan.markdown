---
layout: publication
title: Hashgan:attention-aware Deep Adversarial Hashing For Cross Modal Retrieval
authors: Xi Zhang, Siyu Zhou, Jiashi Feng, Hanjiang Lai, Bo Li, Yan Pan, Jian Yin,
  Shuicheng Yan
conference: Arxiv
year: 2017
bibkey: zhang2017hashgan
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.09347'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Zhang et al.
---
As the rapid growth of multi-modal data, hashing methods for cross-modal
retrieval have received considerable attention. Deep-networks-based cross-modal
hashing methods are appealing as they can integrate feature learning and hash
coding into end-to-end trainable frameworks. However, it is still challenging
to find content similarities between different modalities of data due to the
heterogeneity gap. To further address this problem, we propose an adversarial
hashing network with attention mechanism to enhance the measurement of content
similarities by selectively focusing on informative parts of multi-modal data.
The proposed new adversarial network, HashGAN, consists of three building
blocks: 1) the feature learning module to obtain feature representations, 2)
the generative attention module to generate an attention mask, which is used to
obtain the attended (foreground) and the unattended (background) feature
representations, 3) the discriminative hash coding module to learn hash
functions that preserve the similarities between different modalities. In our
framework, the generative module and the discriminative module are trained in
an adversarial way: the generator is learned to make the discriminator cannot
preserve the similarities of multi-modal data w.r.t. the background feature
representations, while the discriminator aims to preserve the similarities of
multi-modal data w.r.t. both the foreground and the background feature
representations. Extensive evaluations on several benchmark datasets
demonstrate that the proposed HashGAN brings substantial improvements over
other state-of-the-art cross-modal hashing methods.