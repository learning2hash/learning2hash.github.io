---
layout: publication
title: Molecular Graph Representation Learning Via Structural Similarity Information
authors: Chengyu Yao, Hong Huang, Hang Gao, Fengge Wu, Haiming Chen, Junsuo Zhao
conference: Lecture Notes in Computer Science
year: 2024
bibkey: yao2024molecular
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yaoyao-yaoyao-cell/MSSM-GNN'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.08580'}]
tags: []
short_authors: Yao et al.
---
Graph Neural Networks (GNNs) have been widely employed for feature
representation learning in molecular graphs. Therefore, it is crucial to
enhance the expressiveness of feature representation to ensure the
effectiveness of GNNs. However, a significant portion of current research
primarily focuses on the structural features within individual molecules, often
overlooking the structural similarity between molecules, which is a crucial
aspect encapsulating rich information on the relationship between molecular
properties and structural characteristics. Thus, these approaches fail to
capture the rich semantic information at the molecular structure level. To
bridge this gap, we introduce the \textbf\{Molecular Structural Similarity Motif
GNN (MSSM-GNN)\}, a novel molecular graph representation learning method that
can capture structural similarity information among molecules from a global
perspective. In particular, we propose a specially designed graph that
leverages graph kernel algorithms to represent the similarity between molecules
quantitatively. Subsequently, we employ GNNs to learn feature representations
from molecular graphs, aiming to enhance the accuracy of property prediction by
incorporating additional molecular representation information. Finally, through
a series of experiments conducted on both small-scale and large-scale molecular
datasets, we demonstrate that our model consistently outperforms eleven
state-of-the-art baselines. The codes are available at
https://github.com/yaoyao-yaoyao-cell/MSSM-GNN.