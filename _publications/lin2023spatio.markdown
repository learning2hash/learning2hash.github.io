---
layout: publication
title: Spatio-temporal Co-attention Fusion Network For Video Splicing Localization
authors: Man Lin, Gang Cao, Zijie Lou
conference: Journal of Electronic Imaging
year: 2024
bibkey: lin2023spatio
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.09482'}]
tags: []
short_authors: Man Lin, Gang Cao, Zijie Lou
---
Digital video splicing has become easy and ubiquitous. Malicious users copy
some regions of a video and paste them to another video for creating realistic
forgeries. It is significant to blindly detect such forgery regions in videos.
In this paper, a spatio-temporal co-attention fusion network (SCFNet) is
proposed for video splicing localization. Specifically, a three-stream network
is used as an encoder to capture manipulation traces across multiple frames.
The deep interaction and fusion of spatio-temporal forensic features are
achieved by the novel parallel and cross co-attention fusion modules. A
lightweight multilayer perceptron (MLP) decoder is adopted to yield a
pixel-level tampering localization map. A new large-scale video splicing
dataset is created for training the SCFNet. Extensive tests on benchmark
datasets show that the localization and generalization performances of our
SCFNet outperform the state-of-the-art. Code and datasets will be available at
https://github.com/multimediaFor/SCFNet.