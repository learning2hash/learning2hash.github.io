---
layout: publication
title: 'Deephums: Deep Human Motion Signature For 3D Skeletal Sequences'
authors: Neeraj Battan, Abbhinav Venkat, Avinash Sharma
conference: Lecture Notes in Computer Science
year: 2019
bibkey: battan2019deephums
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05750'}]
tags: ["Datasets", "Self-Supervised"]
short_authors: Neeraj Battan, Abbhinav Venkat, Avinash Sharma
---
3D Human Motion Indexing and Retrieval is an interesting problem due to the
rise of several data-driven applications aimed at analyzing and/or re-utilizing
3D human skeletal data, such as data-driven animation, analysis of sports
bio-mechanics, human surveillance etc. Spatio-temporal articulations of humans,
noisy/missing data, different speeds of the same motion etc. make it
challenging and several of the existing state of the art methods use hand-craft
features along with optimization based or histogram based comparison in order
to perform retrieval. Further, they demonstrate it only for very small datasets
and few classes. We make a case for using a learned representation that should
recognize the motion as well as enforce a discriminative ranking. To that end,
we propose, a 3D human motion descriptor learned using a deep network. Our
learned embedding is generalizable and applicable to real-world data -
addressing the aforementioned challenges and further enables sub-motion
searching in its embedding space using another network. Our model exploits the
inter-class similarity using trajectory cues, and performs far superior in a
self-supervised setting. State of the art results on all these fronts is shown
on two large scale 3D human motion datasets - NTU RGB+D and HDM05.