---
layout: publication
title: 'CSMCIR: Cot-enhanced Symmetric Alignment With Memory Bank For Composed Image
  Retrieval'
authors: Zhipeng Qian, Zihan Liang, Yufei Ma, Ben Chen, Huangyu Dai, Yiwei Ma, Jiayi
  Ji, Chenyi Lei, Han Li, Xiaoshuai Sun
conference: Arxiv
year: 2026
bibkey: qian2026csmcir
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2601.03728'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Image Retrieval", "Tools & Libraries"]
short_authors: Qian et al.
---
Composed Image Retrieval (CIR) enables users to search for target images using both a reference image and manipulation text, offering substantial advantages over single-modality retrieval systems. However, existing CIR methods suffer from representation space fragmentation: queries and targets comprise heterogeneous modalities and are processed by distinct encoders, forcing models to bridge misaligned representation spaces only through post-hoc alignment, which fundamentally limits retrieval performance. This architectural asymmetry manifests as three distinct, well-separated clusters in the feature space, directly demonstrating how heterogeneous modalities create fundamentally misaligned representation spaces from initialization. In this work, we propose CSMCIR, a unified representation framework that achieves efficient query-target alignment through three synergistic components. First, we introduce a Multi-level Chain-of-Thought (MCoT) prompting strategy that guides Multimodal Large Language Models to generate discriminative, semantically compatible captions for target images, establishing modal symmetry. Building upon this, we design a symmetric dual-tower architecture where both query and target sides utilize the identical shared-parameter Q-Former for cross-modal encoding, ensuring consistent feature representations and further reducing the alignment gap. Finally, this architectural symmetry enables an entropy-based, temporally dynamic Memory Bank strategy that provides high-quality negative samples while maintaining consistency with the evolving model state. Extensive experiments on four benchmark datasets demonstrate that our CSMCIR achieves state-of-the-art performance with superior training efficiency. Comprehensive ablation studies further validate the effectiveness of each proposed component.