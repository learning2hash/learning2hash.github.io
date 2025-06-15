---
layout: publication
title: 'SCENIR: Visual Semantic Clarity Through Unsupervised Scene Graph Retrieval'
authors: Nikolaos Chaidos, Angeliki Dimitriou, Maria Lymperaiou, Giorgos Stamou
conference: "ICML 2025"
year: 2025
citations: 0
bibkey: chaidos2025visual
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2505.15867'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Efficiency', 'Retrieval Models', 'Evaluation', 'Datasets', 'Vector Indexing', 'Supervised', 'Training Strategy', 'Applications']
---
Despite the dominance of convolutional and transformer-based architectures in image-to-image retrieval, these models are prone to biases arising from low-level visual features, such as color. Recognizing the lack of semantic understanding as a key limitation, we propose a novel scene graph-based retrieval framework that emphasizes semantic content over superficial image characteristics. Prior approaches to scene graph retrieval predominantly rely on supervised Graph Neural Networks (GNNs), which require ground truth graph pairs driven from image captions. However, the inconsistency of caption-based supervision stemming from variable text encodings undermine retrieval reliability. To address these, we present SCENIR, a Graph Autoencoder-based unsupervised retrieval framework, which eliminates the dependence on labeled training data. Our model demonstrates superior performance across metrics and runtime efficiency, outperforming existing vision-based, multimodal, and supervised GNN approaches. We further advocate for Graph Edit Distance (GED) as a deterministic and robust ground truth measure for scene graph similarity, replacing the inconsistent caption-based alternatives for the first time in image-to-image retrieval evaluation. Finally, we validate the generalizability of our method by applying it to unannotated datasets via automated scene graph generation, while substantially contributing in advancing state-of-the-art in counterfactual image retrieval.
