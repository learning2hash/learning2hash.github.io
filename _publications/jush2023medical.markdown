---
layout: publication
title: Medical Image Retrieval Using Pretrained Embeddings
authors: Farnaz Khun Jush, Tuan Truong, Steffen Vogler, Matthias Lenga
conference: 2024 IEEE International Symposium on Biomedical Imaging (ISBI)
year: 2023
bibkey: jush2023medical
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.13547'}]
tags: ["Evaluation", "Image Retrieval", "Scalability", "Similarity Search"]
short_authors: Jush et al.
---
A wide range of imaging techniques and data formats available for medical
images make accurate retrieval from image databases challenging.
  Efficient retrieval systems are crucial in advancing medical research,
enabling large-scale studies and innovative diagnostic tools. Thus, addressing
the challenges of medical image retrieval is essential for the continued
enhancement of healthcare and research.
  In this study, we evaluated the feasibility of employing four
state-of-the-art pretrained models for medical image retrieval at modality,
body region, and organ levels and compared the results of two similarity
indexing approaches. Since the employed networks take 2D images, we analyzed
the impacts of weighting and sampling strategies to incorporate 3D information
during retrieval of 3D volumes. We showed that medical image retrieval is
feasible using pretrained networks without any additional training or
fine-tuning steps. Using pretrained embeddings, we achieved a recall of 1 for
various tasks at modality, body region, and organ level.