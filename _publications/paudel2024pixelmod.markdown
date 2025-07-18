---
layout: publication
title: 'PIXELMOD: Improving Soft Moderation Of Visual Misleading Information On Twitter'
authors: Paudel et al.
conference: 2023 IEEE Symposium on Security and Privacy (SP)
year: 2024
bibkey: paudel2024pixelmod
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.20987'}]
tags: [DATASETS, Evaluation]
---
Images are a powerful and immediate vehicle to carry misleading or outright
false messages, yet identifying image-based misinformation at scale poses
unique challenges. In this paper, we present PIXELMOD, a system that leverages
perceptual hashes, vector databases, and optical character recognition (OCR) to
efficiently identify images that are candidates to receive soft moderation
labels on Twitter. We show that PIXELMOD outperforms existing image similarity
approaches when applied to soft moderation, with negligible performance
overhead. We then test PIXELMOD on a dataset of tweets surrounding the 2020 US
Presidential Election, and find that it is able to identify visually misleading
images that are candidates for soft moderation with 0.99% false detection and
2.06% false negatives.