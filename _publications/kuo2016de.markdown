---
layout: publication
title: 'De-hashing: Server-side Context-aware Feature Reconstruction For Mobile Visual
  Search'
authors: Yin-hsi Kuo, Winston H. Hsu
conference: Arxiv
year: 2016
bibkey: kuo2016de
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.08999'}]
tags: ["Compact Codes", "Hashing Methods", "Image Retrieval", "Video Retrieval"]
short_authors: Yin-hsi Kuo, Winston H. Hsu
---
Due to the prevalence of mobile devices, mobile search becomes a more
convenient way than desktop search. Different from the traditional desktop
search, mobile visual search needs more consideration for the limited resources
on mobile devices (e.g., bandwidth, computing power, and memory consumption).
The state-of-the-art approaches show that bag-of-words (BoW) model is robust
for image and video retrieval; however, the large vocabulary tree might not be
able to be loaded on the mobile device. We observe that recent works mainly
focus on designing compact feature representations on mobile devices for
bandwidth-limited network (e.g., 3G) and directly adopt feature matching on
remote servers (cloud). However, the compact (binary) representation might fail
to retrieve target objects (images, videos). Based on the hashed binary codes,
we propose a de-hashing process that reconstructs BoW by leveraging the
computing power of remote servers. To mitigate the information loss from binary
codes, we further utilize contextual information (e.g., GPS) to reconstruct a
context-aware BoW for better retrieval results. Experiment results show that
the proposed method can achieve competitive retrieval accuracy as BoW while
only transmitting few bits from mobile devices.