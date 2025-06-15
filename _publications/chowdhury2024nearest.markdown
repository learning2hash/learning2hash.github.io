---
layout: publication
title: 'Nearest Neighbor Normalization Improves Multimodal Retrieval'
authors: Neil Chowdhury et al.
conference: "EMNLP 2024"
year: 2024
citations: 0
bibkey: chowdhury2024nearest
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2410.24114'}
tags: ['Cross-Modal', 'Retrieval Models', 'Shallow', 'Datasets', 'Supervised', 'Training Strategy', 'Applications']
---
Multimodal models leverage large-scale pre-training to achieve strong but
still imperfect performance on tasks such as image captioning, visual question
answering, and cross-modal retrieval. In this paper, we present a simple and
efficient method for correcting errors in trained contrastive image-text
retrieval models with no additional training, called Nearest Neighbor
Normalization (NNN). We show an improvement on retrieval metrics in both text
retrieval and image retrieval for all of the contrastive models that we tested
(CLIP, BLIP, ALBEF, SigLIP, BEiT) and for both of the datasets that we used
(MS-COCO and Flickr30k). NNN requires a reference database, but does not
require any training on this database, and can even increase the retrieval
accuracy of a model after finetuning.
