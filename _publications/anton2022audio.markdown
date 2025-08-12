---
layout: publication
title: 'Audio Barlow Twins: Self-supervised Audio Representation Learning'
authors: Jonah Anton, Harry Coppock, Pancham Shukla, Bjorn W. Schuller
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: anton2022audio
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.14345'}]
tags: ["ICASSP", "Self-Supervised"]
short_authors: Anton et al.
---
The Barlow Twins self-supervised learning objective requires neither negative
samples or asymmetric learning updates, achieving results on a par with the
current state-of-the-art within Computer Vision. As such, we present Audio
Barlow Twins, a novel self-supervised audio representation learning approach,
adapting Barlow Twins to the audio domain. We pre-train on the large-scale
audio dataset AudioSet, and evaluate the quality of the learnt representations
on 18 tasks from the HEAR 2021 Challenge, achieving results which outperform,
or otherwise are on a par with, the current state-of-the-art for instance
discrimination self-supervised learning approaches to audio representation
learning. Code at https://github.com/jonahanton/SSL_audio.