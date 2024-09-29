---
layout: publication
title: Contextual Similarity Aggregation With Self45;attention For Visual Re45;ranking
authors: Jianbo Ouyang, Hui Wu, Min Wang, Wengang Zhou, Houqiang Li
conference: "Neural Information Processing Systems"
year: 2021
bibkey: ouyang2021contextual
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/18d10dc6e666eab6de9215ae5b3d54df-Abstract.html"}
tags: ['Image Retrieval', 'NEURIPS']
---
In content45;based image retrieval the first45;round retrieval result by simple visual feature comparison may be unsatisfactory which can be refined by visual re45;ranking techniques. In image retrieval it is observed that the contextual similarity among the top45;ranked images is an important clue to distinguish the semantic relevance. Inspired by this observation in this paper we propose a visual re45;ranking method by contextual similarity aggregation with self45;attention. In our approach for each image in the top45;K ranking list we represent it into an affinity feature vector by comparing it with a set of anchor images. Then the affinity features of the top45;K images are refined by aggregating the contextual information with a transformer encoder. Finally the affinity features are used to recalculate the similarity scores between the query and the top45;K images for re45;ranking of the latter. To further improve the robustness of our re45;ranking model and enhance the performance of our method a new data augmentation scheme is designed. Since our re45;ranking model is not directly involved with the visual feature used in the initial retrieval it is ready to be applied to retrieval result lists obtained from various retrieval algorithms. We conduct comprehensive experiments on four benchmark datasets to demonstrate the generality and effectiveness of our proposed visual re45;ranking method.
