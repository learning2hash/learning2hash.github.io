---
layout: publication
title: Improving Natural-language-based Audio Retrieval With Transfer Learning And
  Audio & Text Augmentations
authors: Paul Primus, Gerhard Widmer
conference: Arxiv
year: 2022
bibkey: primus2022improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.11460'}]
tags: ["Audio Retrieval", "Datasets", "Evaluation", "Neural Hashing"]
short_authors: Paul Primus, Gerhard Widmer
---
The absence of large labeled datasets remains a significant challenge in many
application areas of deep learning. Researchers and practitioners typically
resort to transfer learning and data augmentation to alleviate this issue. We
study these strategies in the context of audio retrieval with natural language
queries (Task 6b of the DCASE 2022 Challenge). Our proposed system uses
pre-trained embedding models to project recordings and textual descriptions
into a shared audio-caption space in which related examples from different
modalities are close. We employ various data augmentation techniques on audio
and text inputs and systematically tune their corresponding hyperparameters
with sequential model-based optimization. Our results show that the used
augmentations strategies reduce overfitting and improve retrieval performance.