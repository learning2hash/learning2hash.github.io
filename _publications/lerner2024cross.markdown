---
layout: publication
title: Cross-modal Retrieval For Knowledge-based Visual Question Answering
authors: Paul Lerner, Olivier Ferret, Camille Guinaudeau
conference: Lecture Notes in Computer Science
year: 2024
bibkey: lerner2024cross
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.05736'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Paul Lerner, Olivier Ferret, Camille Guinaudeau
---
Knowledge-based Visual Question Answering about Named Entities is a
challenging task that requires retrieving information from a multimodal
Knowledge Base. Named entities have diverse visual representations and are
therefore difficult to recognize. We argue that cross-modal retrieval may help
bridge the semantic gap between an entity and its depictions, and is foremost
complementary with mono-modal retrieval. We provide empirical evidence through
experiments with a multimodal dual encoder, namely CLIP, on the recent ViQuAE,
InfoSeek, and Encyclopedic-VQA datasets. Additionally, we study three different
strategies to fine-tune such a model: mono-modal, cross-modal, or joint
training. Our method, which combines mono-and cross-modal retrieval, is
competitive with billion-parameter models on the three datasets, while being
conceptually simpler and computationally cheaper.