---
layout: publication
title: 'Matchxml: An Efficient Text-label Matching Framework For Extreme Multi-label
  Text Classification'
authors: Hui Ye, Rajshekhar Sunderraman, Shihao Ji
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2024
bibkey: ye2023matchxml
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.13139'}]
tags: []
short_authors: Hui Ye, Rajshekhar Sunderraman, Shihao Ji
---
The eXtreme Multi-label text Classification(XMC) refers to training a
classifier that assigns a text sample with relevant labels from an extremely
large-scale label set (e.g., millions of labels). We propose MatchXML, an
efficient text-label matching framework for XMC. We observe that the label
embeddings generated from the sparse Term Frequency-Inverse Document
Frequency(TF-IDF) features have several limitations. We thus propose label2vec
to effectively train the semantic dense label embeddings by the Skip-gram
model. The dense label embeddings are then used to build a Hierarchical Label
Tree by clustering. In fine-tuning the pre-trained encoder Transformer, we
formulate the multi-label text classification as a text-label matching problem
in a bipartite graph. We then extract the dense text representations from the
fine-tuned Transformer. Besides the fine-tuned dense text embeddings, we also
extract the static dense sentence embeddings from a pre-trained Sentence
Transformer. Finally, a linear ranker is trained by utilizing the sparse TF-IDF
features, the fine-tuned dense text representations and static dense sentence
features. Experimental results demonstrate that MatchXML achieves
state-of-the-art accuracy on five out of six datasets. As for the speed,
MatchXML outperforms the competing methods on all the six datasets. Our source
code is publicly available at https://github.com/huiyegit/MatchXML.