---
layout: publication
title: 'Taxabind: A Unified Embedding Space For Ecological Applications'
authors: Srikumar Sastry, Subash Khanal, Aayush Dhakal, Adeel Ahmad, Nathan Jacobs
conference: Arxiv
year: 2024
bibkey: sastry2024taxabind
citations: 2
additional_links: [{name: Code, url: 'https://github.com/mvrl/TaxaBind'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.00683'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Neural Hashing"]
short_authors: Sastry et al.
---
We present TaxaBind, a unified embedding space for characterizing any species
of interest. TaxaBind is a multimodal embedding space across six modalities:
ground-level images of species, geographic location, satellite image, text,
audio, and environmental features, useful for solving ecological problems. To
learn this joint embedding space, we leverage ground-level images of species as
a binding modality. We propose multimodal patching, a technique for effectively
distilling the knowledge from various modalities into the binding modality. We
construct two large datasets for pretraining: iSatNat with species images and
satellite images, and iSoundNat with species images and audio. Additionally, we
introduce TaxaBench-8k, a diverse multimodal dataset with six paired modalities
for evaluating deep learning models on ecological tasks. Experiments with
TaxaBind demonstrate its strong zero-shot and emergent capabilities on a range
of tasks including species classification, cross-model retrieval, and audio
classification. The datasets and models are made available at
https://github.com/mvrl/TaxaBind.