---
layout: publication
title: Ambiguity-aware And High-order Relation Learning For Multi-grained Image-text
  Matching
authors: Junyu Chen, Yihua Gao, Mingyuan Ge, Mingyong Li
conference: Knowledge-Based Systems
year: 2025
bibkey: chen2025ambiguity
citations: 1
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2507.09256'}]
tags: ["Datasets", "Efficiency", "Self-Supervised", "Tools & Libraries"]
short_authors: Chen et al.
---
Image-text matching is crucial for bridging the semantic gap between computer vision and natural language processing. However, existing methods still face challenges in handling high-order associations and semantic ambiguities among similar instances. These ambiguities arise from subtle differences between soft positive samples (semantically similar but incorrectly labeled) and soft negative samples (locally matched but globally inconsistent), creating matching uncertainties. Furthermore, current methods fail to fully utilize the neighborhood relationships among semantically similar instances within training batches, limiting the model's ability to learn high-order shared knowledge. This paper proposes the Ambiguity-Aware and High-order Relation learning framework (AAHR) to address these issues. AAHR constructs a unified representation space through dynamic clustering prototype contrastive learning, effectively mitigating the soft positive sample problem. The framework introduces global and local feature extraction mechanisms and an adaptive aggregation network, significantly enhancing full-grained semantic understanding capabilities. Additionally, AAHR employs intra-modal and inter-modal correlation matrices to investigate neighborhood relationships among sample instances thoroughly. It incorporates GNN to enhance semantic interactions between instances. Furthermore, AAHR integrates momentum contrastive learning to expand the negative sample set. These combined strategies significantly improve the model's ability to discriminate between features. Experimental results demonstrate that AAHR outperforms existing state-of-the-art methods on Flickr30K, MSCOCO, and ECCV Caption datasets, considerably improving the accuracy and efficiency of image-text matching. The code and model checkpoints for this research are available at https://github.com/Image-Text-Matching/AAHR .