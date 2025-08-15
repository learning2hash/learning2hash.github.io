---
layout: publication
title: 'JIST: Joint Image And Sequence Training For Sequential Visual Place Recognition'
authors: Gabriele Berton, Gabriele Trivigno, Barbara Caputo, Carlo Masone
conference: Arxiv
year: 2024
bibkey: berton2024jist
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ga1i13o/JIST'}, {name: Paper,
    url: 'https://arxiv.org/abs/2403.19787'}]
tags: ["Tools & Libraries"]
short_authors: Berton et al.
---
Visual Place Recognition aims at recognizing previously visited places by
relying on visual clues, and it is used in robotics applications for SLAM and
localization. Since typically a mobile robot has access to a continuous stream
of frames, this task is naturally cast as a sequence-to-sequence localization
problem. Nevertheless, obtaining sequences of labelled data is much more
expensive than collecting isolated images, which can be done in an automated
way with little supervision. As a mitigation to this problem, we propose a
novel Joint Image and Sequence Training protocol (JIST) that leverages large
uncurated sets of images through a multi-task learning framework. With JIST we
also introduce SeqGeM, an aggregation layer that revisits the popular GeM
pooling to produce a single robust and compact embedding from a sequence of
single-frame embeddings. We show that our model is able to outperform previous
state of the art while being faster, using 8 times smaller descriptors, having
a lighter architecture and allowing to process sequences of various lengths.
Code is available at https://github.com/ga1i13o/JIST