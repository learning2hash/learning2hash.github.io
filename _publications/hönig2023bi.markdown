---
layout: publication
title: Bi-encoder Cascades For Efficient Image Search
authors: "Robert H\xF6nig, Jan Ackermann, Mingyuan Chi"
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: "h\xF6nig2023bi"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.15595'}]
tags: ["ICCV", "Image Retrieval", "Scalability"]
short_authors: "Robert H\xF6nig, Jan Ackermann, Mingyuan Chi"
---
Modern neural encoders offer unprecedented text-image retrieval (TIR)
accuracy, but their high computational cost impedes an adoption to large-scale
image searches. To lower this cost, model cascades use an expensive encoder to
refine the ranking of a cheap encoder. However, existing cascading algorithms
focus on cross-encoders, which jointly process text-image pairs, but do not
consider cascades of bi-encoders, which separately process texts and images. We
introduce the small-world search scenario as a realistic setting where
bi-encoder cascades can reduce costs. We then propose a cascading algorithm
that leverages the small-world search scenario to reduce lifetime image
encoding costs of a TIR system. Our experiments show cost reductions by up to
6x.