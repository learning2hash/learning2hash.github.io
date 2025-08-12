---
layout: publication
title: Large Scale Open-set Deep Logo Detection
authors: Muhammet Bastan, Hao-Yu Wu, Tian Cao, Bhargava Kota, Mehmet Tek
conference: Arxiv
year: 2019
bibkey: bastan2019large
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07440'}]
tags: ["Datasets"]
short_authors: Bastan et al.
---
We present an open-set logo detection (OSLD) system, which can detect
(localize and recognize) any number of unseen logo classes without re-training;
it only requires a small set of canonical logo images for each logo class. We
achieve this using a two-stage approach: (1) Generic logo detection to detect
candidate logo regions in an image. (2) Logo matching for matching the detected
logo regions to a set of canonical logo images to recognize them.
  We constructed an open-set logo detection dataset with 12.1k logo classes and
released it for research purposes.We demonstrate the effectiveness of OSLD on
our dataset and on the standard Flickr-32 logo dataset, outperforming the
state-of-the-art open-set and closed-set logo detection methods by a large
margin. OSLD is scalable to millions of logo classes.