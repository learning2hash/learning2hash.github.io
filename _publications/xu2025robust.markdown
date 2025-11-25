---
layout: publication
title: Robust Multi-view Learning Via Representation Fusion Of Sample-level Attention
  And Alignment Of Simulated Perturbation
authors: Jie Xu, Na Zhao, Gang Niu, Masashi Sugiyama, Xiaofeng Zhu
conference: Arxiv
year: 2025
bibkey: xu2025robust
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.04151'}]
tags: ["Robustness", "Self-Supervised", "Unsupervised"]
short_authors: Xu et al.
---
Recently, multi-view learning (MVL) has garnered significant attention due to
its ability to fuse discriminative information from multiple views. However,
real-world multi-view datasets are often heterogeneous and imperfect, which
usually makes MVL methods designed for specific combinations of views lack
application potential and limits their effectiveness. To address this issue, we
propose a novel robust MVL method (namely RML) with simultaneous representation
fusion and alignment. Specifically, we introduce a simple yet effective
multi-view transformer fusion network where we transform heterogeneous
multi-view data into homogeneous word embeddings, and then integrate multiple
views by the sample-level attention mechanism to obtain a fused representation.
Furthermore, we propose a simulated perturbation based multi-view contrastive
learning framework that dynamically generates the noise and unusable
perturbations for simulating imperfect data conditions. The simulated noisy and
unusable data obtain two distinct fused representations, and we utilize
contrastive learning to align them for learning discriminative and robust
representations. Our RML is self-supervised and can also be applied for
downstream tasks as a regularization. In experiments, we employ it in
unsupervised multi-view clustering, noise-label classification, and as a
plug-and-play module for cross-modal hashing retrieval. Extensive comparison
experiments and ablation studies validate the effectiveness of RML.