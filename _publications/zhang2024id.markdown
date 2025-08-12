---
layout: publication
title: 'Id-patch: Robust ID Association For Group Photo Personalization'
authors: Yimeng Zhang, Tiancheng Zhi, Jing Liu, Shen Sang, Liming Jiang, Qing Yan,
  Sijia Liu, Linjie Luo
conference: Arxiv
year: 2024
bibkey: zhang2024id
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.13632'}]
tags: []
short_authors: Zhang et al.
---
The ability to synthesize personalized group photos and specify the positions
of each identity offers immense creative potential. While such imagery can be
visually appealing, it presents significant challenges for existing
technologies. A persistent issue is identity (ID) leakage, where injected
facial features interfere with one another, resulting in low face resemblance,
incorrect positioning, and visual artifacts. Existing methods suffer from
limitations such as the reliance on segmentation models, increased runtime, or
a high probability of ID leakage. To address these challenges, we propose
ID-Patch, a novel method that provides robust association between identities
and 2D positions. Our approach generates an ID patch and ID embeddings from the
same facial features: the ID patch is positioned on the conditional image for
precise spatial control, while the ID embeddings integrate with text embeddings
to ensure high resemblance. Experimental results demonstrate that ID-Patch
surpasses baseline methods across metrics, such as face ID resemblance,
ID-position association accuracy, and generation efficiency. Project Page is:
https://byteaigc.github.io/ID-Patch/