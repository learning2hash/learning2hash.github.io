---
layout: publication
title: The Forchheim Image Database For Camera Identification In The Wild
authors: Benjamin Hadwiger, Christian Riess
conference: Lecture Notes in Computer Science
year: 2021
bibkey: hadwiger2020forchheim
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.02241'}]
tags: ["Datasets"]
short_authors: Benjamin Hadwiger, Christian Riess
---
Image provenance can represent crucial knowledge in criminal investigation
and journalistic fact checking. In the last two decades, numerous algorithms
have been proposed for obtaining information on the source camera and
distribution history of an image. For a fair ranking of these techniques, it is
important to rigorously assess their performance on practically relevant test
cases. To this end, a number of datasets have been proposed. However, we argue
that there is a gap in existing databases: to our knowledge, there is currently
no dataset that simultaneously satisfies two goals, namely a) to cleanly
separate scene content and forensic traces, and b) to support realistic
post-processing like social media recompression. In this work, we propose the
Forchheim Image Database (FODB) to close this gap. It consists of more than
23,000 images of 143 scenes by 27 smartphone cameras, and it allows to cleanly
separate image content from forensic artifacts. Each image is provided in 6
different qualities: the original camera-native version, and five copies from
social networks. We demonstrate the usefulness of FODB in an evaluation of
methods for camera identification. We report three findings. First, the
recently proposed general-purpose EfficientNet remarkably outperforms several
dedicated forensic CNNs both on clean and compressed images. Second,
classifiers obtain a performance boost even on unknown post-processing after
augmentation by artificial degradations. Third, FODB's clean separation of
scene content and forensic traces imposes important, rigorous boundary
conditions for algorithm benchmarking.