---
layout: publication
title: Robust And Lightweight Audio Fingerprint For Automatic Content Recognition
authors: Anoubhav Agarwaal, Prabhat Kanaujia, Sartaki Sinha Roy, Susmita Ghose
conference: Arxiv
year: 2023
bibkey: agarwaal2023robust
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.09559'}]
tags: ["Memory Efficiency", "Robustness", "Similarity Search"]
short_authors: Agarwaal et al.
---
This research paper presents a novel audio fingerprinting system for
Automatic Content Recognition (ACR). By using signal processing techniques and
statistical transformations, our proposed method generates compact fingerprints
of audio segments that are robust to noise degradations present in real-world
audio. The system is designed to be highly scalable, with the ability to
identify thousands of hours of content using fingerprints generated from
millions of TVs. The fingerprint's high temporal correlation and utilization of
existing GPU-compatible Approximate Nearest Neighbour (ANN) search algorithms
make this possible. Furthermore, the fingerprint generation can run on
low-power devices with limited compute, making it accessible to a wide range of
applications. Experimental results show improvements in our proposed system
compared to a min-hash based audio fingerprint on all evaluated metrics,
including accuracy on proprietary ACR datasets, retrieval speed, memory usage,
and robustness to various noises. For similar retrieval accuracy, our system is
30x faster and uses 6x fewer fingerprints than the min-hash method.