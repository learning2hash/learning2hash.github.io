---
layout: publication
title: 'SVIA: A Street View Image Anonymization Framework For Self-driving Applications'
authors: Dongyu Liu, Xuhong Wang, Cen Chen, Yanhao Wang, Shengyue Yao, Yilun Lin
conference: Arxiv
year: 2025
bibkey: liu2025svia
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.09393'}]
tags: ["Privacy & Security"]
short_authors: Liu et al.
---
In recent years, there has been an increasing interest in image
anonymization, particularly focusing on the de-identification of faces and
individuals. However, for self-driving applications, merely de-identifying
faces and individuals might not provide sufficient privacy protection since
street views like vehicles and buildings can still disclose locations,
trajectories, and other sensitive information. Therefore, it remains crucial to
extend anonymization techniques to street view images to fully preserve the
privacy of users, pedestrians, and vehicles. In this paper, we propose a Street
View Image Anonymization (SVIA) framework for self-driving applications. The
SVIA framework consists of three integral components: a semantic segmenter to
segment an input image into functional regions, an inpainter to generate
alternatives to privacy-sensitive regions, and a harmonizer to seamlessly
stitch modified regions to guarantee visual coherence. Compared to existing
methods, SVIA achieves a much better trade-off between image generation quality
and privacy protection, as evidenced by experimental results for five common
metrics on two widely used public datasets.