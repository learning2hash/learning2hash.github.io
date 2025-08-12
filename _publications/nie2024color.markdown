---
layout: publication
title: Color Space Learning For Cross-color Person Re-identification
authors: Jiahao Nie, Shan Lin, Alex C. Kot
conference: 2024 IEEE International Conference on Multimedia and Expo (ICME)
year: 2024
bibkey: nie2024color
citations: 3
additional_links: [{name: Code, url: 'https://github.com/niejiahao1998/CSL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2405.09487'}]
tags: ["Evaluation", "Robustness"]
short_authors: Jiahao Nie, Shan Lin, Alex C. Kot
---
The primary color profile of the same identity is assumed to remain
consistent in typical Person Re-identification (Person ReID) tasks. However,
this assumption may be invalid in real-world situations and images hold variant
color profiles, because of cross-modality cameras or identity with different
clothing. To address this issue, we propose Color Space Learning (CSL) for
those Cross-Color Person ReID problems. Specifically, CSL guides the model to
be less color-sensitive with two modules: Image-level Color-Augmentation and
Pixel-level Color-Transformation. The first module increases the color
diversity of the inputs and guides the model to focus more on the non-color
information. The second module projects every pixel of input images onto a new
color space. In addition, we introduce a new Person ReID benchmark across RGB
and Infrared modalities, NTU-Corridor, which is the first with privacy
agreements from all participants. To evaluate the effectiveness and robustness
of our proposed CSL, we evaluate it on several Cross-Color Person ReID
benchmarks. Our method surpasses the state-of-the-art methods consistently. The
code and benchmark are available at: https://github.com/niejiahao1998/CSL