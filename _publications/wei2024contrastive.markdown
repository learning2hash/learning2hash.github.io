---
layout: publication
title: Contrastive Masked Auto-encoders Based Self-supervised Hashing For 2D Image
  And 3D Point Cloud Cross-modal Retrieval
authors: Rukai Wei, Heng Cui, Yu Liu, Yufeng Hou, Yanzhao Xie, Ke Zhou
conference: Arxiv
year: 2024
bibkey: wei2024contrastive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.05711'}]
tags: ["Hashing Methods", "Self-Supervised"]
short_authors: Wei et al.
---
Implementing cross-modal hashing between 2D images and 3D point-cloud data is
a growing concern in real-world retrieval systems. Simply applying existing
cross-modal approaches to this new task fails to adequately capture latent
multi-modal semantics and effectively bridge the modality gap between 2D and
3D. To address these issues without relying on hand-crafted labels, we propose
contrastive masked autoencoders based self-supervised hashing (CMAH) for
retrieval between images and point-cloud data. We start by contrasting 2D-3D
pairs and explicitly constraining them into a joint Hamming space. This
contrastive learning process ensures robust discriminability for the generated
hash codes and effectively reduces the modality gap. Moreover, we utilize
multi-modal auto-encoders to enhance the model's understanding of multi-modal
semantics. By completing the masked image/point-cloud data modeling task, the
model is encouraged to capture more localized clues. In addition, the proposed
multi-modal fusion block facilitates fine-grained interactions among different
modalities. Extensive experiments on three public datasets demonstrate that the
proposed CMAH significantly outperforms all baseline methods.