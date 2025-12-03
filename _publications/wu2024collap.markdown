---
layout: publication
title: 'Collap: Contrastive Long-form Language-audio Pretraining With Musical Temporal
  Structure Augmentation'
authors: Junda Wu, Warren Li, Zachary Novack, Amit Namburi, Carol Chen, Julian McAuley
conference: Arxiv
year: 2024
bibkey: wu2024collap
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.02271'}]
tags: ["Datasets", "Evaluation", "Scalability", "Self-Supervised", "Text Retrieval"]
short_authors: Wu et al.
---
Modeling temporal characteristics plays a significant role in the
representation learning of audio waveform. We propose Contrastive Long-form
Language-Audio Pretraining (\textbf\{CoLLAP\}) to significantly extend the
perception window for both the input audio (up to 5 minutes) and the language
descriptions (exceeding 250 words), while enabling contrastive learning across
modalities and temporal dynamics. Leveraging recent Music-LLMs to generate
long-form music captions for full-length songs, augmented with musical temporal
structures, we collect 51.3K audio-text pairs derived from the large-scale
AudioSet training dataset, where the average audio length reaches 288 seconds.
We propose a novel contrastive learning architecture that fuses language
representations with structured audio representations by segmenting each song
into clips and extracting their embeddings. With an attention mechanism, we
capture multimodal temporal correlations, allowing the model to automatically
weigh and enhance the final fusion score for improved contrastive alignment.
Finally, we develop two variants of the CoLLAP model with different types of
backbone language models. Through comprehensive experiments on multiple
long-form music-text retrieval datasets, we demonstrate consistent performance
improvement in retrieval accuracy compared with baselines. We also show the
pretrained CoLLAP models can be transferred to various music information
retrieval tasks, with heterogeneous long-form multimodal contexts.