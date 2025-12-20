---
layout: publication
title: 'Photochat: A Human-human Dialogue Dataset With Photo Sharing Behavior For
  Joint Image-text Modeling'
authors: Xiaoxue Zang, Lijuan Liu, Maria Wang, Yang Song, Hao Zhang, Jindong Chen
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: zang2021photochat
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.01453'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Zang et al.
---
We present a new human-human dialogue dataset - PhotoChat, the first dataset
that casts light on the photo sharing behavior in onlin emessaging. PhotoChat
contains 12k dialogues, each of which is paired with a user photo that is
shared during the conversation. Based on this dataset, we propose two tasks to
facilitate research on image-text modeling: a photo-sharing intent prediction
task that predicts whether one intends to share a photo in the next
conversation turn, and a photo retrieval task that retrieves the most relevant
photo according to the dialogue context. In addition, for both tasks, we
provide baseline models using the state-of-the-art models and report their
benchmark performances. The best image retrieval model achieves 10.4% recall@1
(out of 1000 candidates) and the best photo intent prediction model achieves
58.1% F1 score, indicating that the dataset presents interesting yet
challenging real-world problems. We are releasing PhotoChat to facilitate
future research work among the community.