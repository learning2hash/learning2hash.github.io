---
layout: publication
title: 'Towards Artistic Image Aesthetics Assessment: A Large-scale Dataset And A
  New Method'
authors: Ran Yi, Haoyuan Tian, Zhihao Gu, Yu-Kun Lai, Paul L. Rosin
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: yi2023towards
citations: 28
additional_links: [{name: Code, url: 'https://github.com/Dreemurr-T/BAID.git'}, {
    name: Paper, url: 'https://arxiv.org/abs/2303.15166'}]
tags: ["CVPR", "Datasets"]
short_authors: Yi et al.
---
Image aesthetics assessment (IAA) is a challenging task due to its highly
subjective nature. Most of the current studies rely on large-scale datasets
(e.g., AVA and AADB) to learn a general model for all kinds of photography
images. However, little light has been shed on measuring the aesthetic quality
of artistic images, and the existing datasets only contain relatively few
artworks. Such a defect is a great obstacle to the aesthetic assessment of
artistic images. To fill the gap in the field of artistic image aesthetics
assessment (AIAA), we first introduce a large-scale AIAA dataset: Boldbrush
Artistic Image Dataset (BAID), which consists of 60,337 artistic images
covering various art forms, with more than 360,000 votes from online users. We
then propose a new method, SAAN (Style-specific Art Assessment Network), which
can effectively extract and utilize style-specific and generic aesthetic
information to evaluate artistic images. Experiments demonstrate that our
proposed approach outperforms existing IAA methods on the proposed BAID dataset
according to quantitative comparisons. We believe the proposed dataset and
method can serve as a foundation for future AIAA works and inspire more
research in this field. Dataset and code are available at:
https://github.com/Dreemurr-T/BAID.git