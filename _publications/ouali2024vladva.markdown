---
layout: publication
title: 'Vladva: Discriminative Fine-tuning Of Lvlms'
authors: Yassine Ouali, Adrian Bulat, Alexandros Xenos, Anestis Zaganidis, Ioannis
  Maniadis Metaxas, Brais Martinez, Georgios Tzimiropoulos
conference: Arxiv
year: 2024
bibkey: ouali2024vladva
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.04378'}]
tags: ["Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Ouali et al.
---
Contrastively-trained Vision-Language Models (VLMs) like CLIP have become the de facto approach for discriminative vision-language representation learning. However, these models have limited language understanding, often exhibiting a "bag of words" behavior. At the same time, Large Vision-Language Models (LVLMs), which combine vision encoders with LLMs, have been shown to be capable of detailed vision-language reasoning, yet their autoregressive nature renders them less suitable for discriminative tasks.
  In this work, we propose to combine "the best of both worlds": a new training approach for discriminative fine-tuning of LVLMs that results in strong discriminative and compositional capabilities. Essentially, our approach converts a generative LVLM into a discriminative one, unlocking its capability for powerful image-text discrimination combined with enhanced language understanding.
  Our contributions include (1) a carefully designed training/optimization framework that utilizes image-text pairs of variable length and granularity for training the model with both contrastive and next-token prediction losses. This is accompanied by ablation studies that justify the necessity of our framework's components; (2) a parameter-efficient adaptation method using a combination of soft prompting and LoRA adapters; (3) significant improvements over state-of-the-art CLIP-like models of similar size, including standard image-text retrieval benchmarks and notable gains in compositionality.