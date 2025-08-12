---
layout: publication
title: A Coarse-to-fine Deep Convolutional Neural Network Framework For Frame Duplication
  Detection And Localization In Forged Videos
authors: Chengjiang Long, Arslan Basharat, Anthony Hoogs
conference: Arxiv
year: 2018
bibkey: long2018coarse
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.10762'}]
tags: []
short_authors: Chengjiang Long, Arslan Basharat, Anthony Hoogs
---
Videos can be manipulated by duplicating a sequence of consecutive frames
with the goal of concealing or imitating a specific content in the same video.
In this paper, we propose a novel coarse-to-fine framework based on deep
Convolutional Neural Networks to automatically detect and localize such frame
duplication. First, an I3D network finds coarse-level matches between candidate
duplicated frame sequences and the corresponding selected original frame
sequences. Then a Siamese network based on ResNet architecture identifies
fine-level correspondences between an individual duplicated frame and the
corresponding selected frame. We also propose a robust statistical approach to
compute a video-level score indicating the likelihood of manipulation or
forgery. Additionally, for providing manipulation localization information we
develop an inconsistency detector based on the I3D network to distinguish the
duplicated frames from the selected original frames. Quantified evaluation on
two challenging video forgery datasets clearly demonstrates that this approach
performs significantly better than four recent state-of-the-art methods.