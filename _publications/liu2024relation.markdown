---
layout: publication
title: Relation-aware Meta-learning For Zero-shot Sketch-based Image Retrieval
authors: Yang Liu, Jiale Du, Xinbo Gao, Jungong Han
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2025
bibkey: liu2024relation
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.00120'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Tools & Libraries"]
short_authors: Liu et al.
---
Sketch-based image retrieval (SBIR) relies on free-hand sketches to retrieve
natural photos within the same class. However, its practical application is
limited by its inability to retrieve classes absent from the training set. To
address this limitation, the task has evolved into Zero-Shot Sketch-Based Image
Retrieval (ZS-SBIR), where model performance is evaluated on unseen categories.
Traditional SBIR primarily focuses on narrowing the domain gap between photo
and sketch modalities. However, in the zero-shot setting, the model not only
needs to address this cross-modal discrepancy but also requires a strong
generalization capability to transfer knowledge to unseen categories. To this
end, we propose a novel framework for ZS-SBIR that employs a pair-based
relation-aware quadruplet loss to bridge feature gaps. By incorporating two
negative samples from different modalities, the approach prevents positive
features from becoming disproportionately distant from one modality while
remaining close to another, thus enhancing inter-class separability. We also
propose a Relation-Aware Meta-Learning Network (RAMLN) to obtain the margin, a
hyper-parameter of cross-modal quadruplet loss, to improve the generalization
ability of the model. RAMLN leverages external memory to store feature
information, which it utilizes to assign optimal margin values. Experimental
results obtained on the extended Sketchy and TU-Berlin datasets show a sharp
improvement over existing state-of-the-art methods in ZS-SBIR.