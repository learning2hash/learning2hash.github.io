---
layout: publication
title: 'SMIC: Semantic Multi-item Compression Based On CLIP Dictionary'
authors: Tom Bachard, Thomas Maugey
conference: Arxiv
year: 2024
bibkey: bachard2024smic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05035'}]
tags: ["Efficiency", "Hashing Methods", "Multimodal Retrieval", "Quantization", "Similarity Search"]
short_authors: Tom Bachard, Thomas Maugey
---
Semantic compression, a compression scheme where the distortion metric,
typically MSE, is replaced with semantic fidelity metrics, tends to become more
and more popular. Most recent semantic compression schemes rely on the
foundation model CLIP. In this work, we extend such a scheme to image
collection compression, where inter-item redundancy is taken into account
during the coding phase. For that purpose, we first show that CLIP's latent
space allows for easy semantic additions and subtractions. From this property,
we define a dictionary-based multi-item codec that outperforms state-of-the-art
generative codec in terms of compression rate, around \(10^\{-5\}\) BPP per image,
while not sacrificing semantic fidelity. We also show that the learned
dictionary is of a semantic nature and works as a semantic projector for the
semantic content of images.