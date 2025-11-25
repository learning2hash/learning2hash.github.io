---
layout: publication
title: 'Globaldoc: A Cross-modal Vision-language Framework For Real-world Document
  Image Retrieval And Classification'
authors: "Souhail Bakkali, Sanket Biswas, Zuheng Ming, Micka\xEBl Coustaty, Mar\xE7\
  al Rusi\xF1ol, Oriol Ramos Terrades, Josep Llad\xF3s"
conference: Arxiv
year: 2023
bibkey: bakkali2023globaldoc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.05756'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval", "Robustness", "Self-Supervised"]
short_authors: Bakkali et al.
---
Visual document understanding (VDU) has rapidly advanced with the development
of powerful multi-modal language models. However, these models typically
require extensive document pre-training data to learn intermediate
representations and often suffer a significant performance drop in real-world
online industrial settings. A primary issue is their heavy reliance on OCR
engines to extract local positional information within document pages, which
limits the models' ability to capture global information and hinders their
generalizability, flexibility, and robustness. In this paper, we introduce
GlobalDoc, a cross-modal transformer-based architecture pre-trained in a
self-supervised manner using three novel pretext objective tasks. GlobalDoc
improves the learning of richer semantic concepts by unifying language and
visual representations, resulting in more transferable models. For proper
evaluation, we also propose two novel document-level downstream VDU tasks,
Few-Shot Document Image Classification (DIC) and Content-based Document Image
Retrieval (DIR), designed to simulate industrial scenarios more closely.
Extensive experimentation has been conducted to demonstrate GlobalDoc's
effectiveness in practical settings.