---
layout: publication
title: Contrastive Masked Auto45;encoders Based Self45;supervised Hashing For 2D Image And 3D Point Cloud Cross45;modal Retrieval
authors: Wei Rukai, Cui Heng, Liu Yu, Hou Yufeng, Xie Yanzhao, Zhou Ke
conference: "Arxiv"
year: 2024
bibkey: wei2024contrastive
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2408.05711"}
tags: ['ARXIV', 'Supervised']
---
Implementing cross45;modal hashing between 2D images and 3D point45;cloud data is a growing concern in real45;world retrieval systems. Simply applying existing cross45;modal approaches to this new task fails to adequately capture latent multi45;modal semantics and effectively bridge the modality gap between 2D and 3D. To address these issues without relying on hand45;crafted labels we propose contrastive masked autoencoders based self45;supervised hashing (CMAH) for retrieval between images and point45;cloud data. We start by contrasting 2D45;3D pairs and explicitly constraining them into a joint Hamming space. This contrastive learning process ensures robust discriminability for the generated hash codes and effectively reduces the modality gap. Moreover we utilize multi45;modal auto45;encoders to enhance the models understanding of multi45;modal semantics. By completing the masked image/point45;cloud data modeling task the model is encouraged to capture more localized clues. In addition the proposed multi45;modal fusion block facilitates fine45;grained interactions among different modalities. Extensive experiments on three public datasets demonstrate that the proposed CMAH significantly outperforms all baseline methods.
