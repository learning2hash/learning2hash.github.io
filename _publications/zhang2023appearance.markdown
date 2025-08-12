---
layout: publication
title: Appearance Codes Using Joint Embedding Learning Of Multiple Modalities
authors: Alex Zhang, Evan Dogariu
conference: Arxiv
year: 2023
bibkey: zhang2023appearance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.11427'}]
tags: ["Distance Metric Learning"]
short_authors: Alex Zhang, Evan Dogariu
---
The use of appearance codes in recent work on generative modeling has enabled
novel view renders with variable appearance and illumination, such as day-time
and night-time renders of a scene. A major limitation of this technique is the
need to re-train new appearance codes for every scene on inference, so in this
work we address this problem proposing a framework that learns a joint
embedding space for the appearance and structure of the scene by enforcing a
contrastive loss constraint between different modalities. We apply our
framework to a simple Variational Auto-Encoder model on the RADIATE dataset
\cite\{sheeny2021radiate\} and qualitatively demonstrate that we can generate new
renders of night-time photos using day-time appearance codes without additional
optimization iterations. Additionally, we compare our model to a baseline VAE
that uses the standard per-image appearance code technique and show that our
approach achieves generations of similar quality without learning appearance
codes for any unseen images on inference.