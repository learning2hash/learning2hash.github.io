---
layout: publication
title: 'SCL-RAI: Span-based Contrastive Learning With Retrieval Augmented Inference
  For Unlabeled Entity Problem In NER'
authors: Shuzheng Si, Shuang Zeng, Jiaxing Lin, Baobao Chang
conference: Arxiv
year: 2022
bibkey: si2022scl
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.01646'}]
tags: ["Self-Supervised"]
short_authors: Si et al.
---
Named Entity Recognition is the task to locate and classify the entities in
the text. However, Unlabeled Entity Problem in NER datasets seriously hinders
the improvement of NER performance. This paper proposes SCL-RAI to cope with
this problem. Firstly, we decrease the distance of span representations with
the same label while increasing it for different ones via span-based
contrastive learning, which relieves the ambiguity among entities and improves
the robustness of the model over unlabeled entities. Then we propose retrieval
augmented inference to mitigate the decision boundary shifting problem. Our
method significantly outperforms the previous SOTA method by 4.21% and 8.64%
F1-score on two real-world datasets.