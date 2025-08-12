---
layout: publication
title: 'Sfa-unet: More Attention To Multi-scale Contrast And Contextual Information
  In Infrared Small Object Segmentation'
authors: Imad Ali Shah, Fahad Mumtaz Malik, Muhammad Waqas Ashraf
conference: In 2023 Pattern Recognition and Information Processing (PRIP) pp.147-152
year: 2024
bibkey: shah2024sfa
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.22881'}]
tags: []
short_authors: Imad Ali Shah, Fahad Mumtaz Malik, Muhammad Waqas Ashraf
---
Computer vision researchers have extensively worked on fundamental infrared visual recognition for the past few decades. Among various approaches, deep learning has emerged as the most promising candidate. However, Infrared Small Object Segmentation (ISOS) remains a major focus due to several challenges including: 1) the lack of effective utilization of local contrast and global contextual information; 2) the potential loss of small objects in deep models; and 3) the struggling to capture fine-grained details and ignore noise. To address these challenges, we propose a modified U-Net architecture, named SFA-UNet, by combining Scharr Convolution (SC) and Fast Fourier Convolution (FFC) in addition to vertical and horizontal Attention gates (AG) into UNet. SFA-UNet utilizes double convolution layers with the addition of SC and FFC in its encoder and decoder layers. SC helps to learn the foreground-to-background contrast information whereas FFC provide multi-scale contextual information while mitigating the small objects vanishing problem. Additionally, the introduction of vertical AGs in encoder layers enhances the model's focus on the targeted object by ignoring irrelevant regions. We evaluated the proposed approach on publicly available, SIRST and IRSTD datasets, and achieved superior performance by an average 0.75% with variance of 0.025 of all combined metrics in multiple runs as compared to the existing state-of-the-art methods