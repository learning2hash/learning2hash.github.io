---
layout: publication
title: 'POAR: Towards Open Vocabulary Pedestrian Attribute Recognition'
authors: Yue Zhang, Suchen Wang, Shichao Kan, Zhenyu Weng, Yigang Cen, Yap-Peng Tan
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: zhang2023poar
citations: 3
additional_links: [{name: Code, url: 'https://github.com/IvyYZ/POAR.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.14643'}]
tags: ["Datasets", "Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Zhang et al.
---
Pedestrian attribute recognition (PAR) aims to predict the attributes of a
target pedestrian in a surveillance system. Existing methods address the PAR
problem by training a multi-label classifier with predefined attribute classes.
However, it is impossible to exhaust all pedestrian attributes in the real
world. To tackle this problem, we develop a novel pedestrian open-attribute
recognition (POAR) framework. Our key idea is to formulate the POAR problem as
an image-text search problem. We design a Transformer-based image encoder with
a masking strategy. A set of attribute tokens are introduced to focus on
specific pedestrian parts (e.g., head, upper body, lower body, feet, etc.) and
encode corresponding attributes into visual embeddings. Each attribute category
is described as a natural language sentence and encoded by the text encoder.
Then, we compute the similarity between the visual and text embeddings of
attributes to find the best attribute descriptions for the input images.
Different from existing methods that learn a specific classifier for each
attribute category, we model the pedestrian at a part-level and explore the
searching method to handle the unseen attributes. Finally, a many-to-many
contrastive (MTMC) loss with masked tokens is proposed to train the network
since a pedestrian image can comprise multiple attributes. Extensive
experiments have been conducted on benchmark PAR datasets with an
open-attribute setting. The results verified the effectiveness of the proposed
POAR method, which can form a strong baseline for the POAR task. Our code is
available at https://github.com/IvyYZ/POAR.