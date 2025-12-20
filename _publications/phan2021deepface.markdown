---
layout: publication
title: 'Deepface-emd: Re-ranking Using Patch-wise Earth Mover''s Distance Improves
  Out-of-distribution Face Identification'
authors: Hai Phan, Anh Nguyen
conference: Arxiv
year: 2021
bibkey: phan2021deepface
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04016'}]
tags: ["Distance Metric Learning", "Evaluation", "Hybrid ANN Methods", "Re-Ranking", "Robustness"]
short_authors: Hai Phan, Anh Nguyen
---
Face identification (FI) is ubiquitous and drives many high-stake decisions
made by law enforcement. State-of-the-art FI approaches compare two images by
taking the cosine similarity between their image embeddings. Yet, such an
approach suffers from poor out-of-distribution (OOD) generalization to new
types of images (e.g., when a query face is masked, cropped, or rotated) not
included in the training set or the gallery. Here, we propose a re-ranking
approach that compares two faces using the Earth Mover's Distance on the deep,
spatial features of image patches. Our extra comparison stage explicitly
examines image similarity at a fine-grained level (e.g., eyes to eyes) and is
more robust to OOD perturbations and occlusions than traditional FI.
Interestingly, without finetuning feature extractors, our method consistently
improves the accuracy on all tested OOD queries: masked, cropped, rotated, and
adversarial while obtaining similar results on in-distribution images.