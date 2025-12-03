---
layout: publication
title: 'LCD: Learned Cross-domain Descriptors For 2D-3D Matching'
authors: Quang-Hieu Pham, Mikaela Angelina Uy, Binh-Son Hua, Duc Thanh Nguyen, Gemma
  Roig, Sai-Kit Yeung
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2019
bibkey: pham2019lcd
citations: 3
additional_links: [{name: Code, url: 'https://hkust-vgd.github.io/lcd'}, {name: Paper,
    url: 'https://arxiv.org/abs/1911.09326'}]
tags: ["AAAI", "Datasets", "Evaluation", "Robustness"]
short_authors: Pham et al.
---
In this work, we present a novel method to learn a local cross-domain
descriptor for 2D image and 3D point cloud matching. Our proposed method is a
dual auto-encoder neural network that maps 2D and 3D input into a shared latent
space representation. We show that such local cross-domain descriptors in the
shared embedding are more discriminative than those obtained from individual
training in 2D and 3D domains. To facilitate the training process, we built a
new dataset by collecting \(\approx 1.4\) millions of 2D-3D correspondences with
various lighting conditions and settings from publicly available RGB-D scenes.
Our descriptor is evaluated in three main experiments: 2D-3D matching,
cross-domain retrieval, and sparse-to-dense depth estimation. Experimental
results confirm the robustness of our approach as well as its competitive
performance not only in solving cross-domain tasks but also in being able to
generalize to solve sole 2D and 3D tasks. Our dataset and code are released
publicly at https://hkust-vgd.github.io/lcd.