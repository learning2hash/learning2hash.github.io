---
layout: publication
title: Learning Tri-modal Embeddings For Zero-shot Soundscape Mapping
authors: Subash Khanal, Srikumar Sastry, Aayush Dhakal, Nathan Jacobs
conference: Arxiv
year: 2023
bibkey: khanal2023learning
citations: 1
additional_links: [{name: Code, url: 'https://github.com/mvrl/geoclap'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.10667'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Khanal et al.
---
We focus on the task of soundscape mapping, which involves predicting the
most probable sounds that could be perceived at a particular geographic
location. We utilise recent state-of-the-art models to encode geotagged audio,
a textual description of the audio, and an overhead image of its capture
location using contrastive pre-training. The end result is a shared embedding
space for the three modalities, which enables the construction of soundscape
maps for any geographic region from textual or audio queries. Using the
SoundingEarth dataset, we find that our approach significantly outperforms the
existing SOTA, with an improvement of image-to-audio Recall@100 from 0.256 to
0.450. Our code is available at https://github.com/mvrl/geoclap.