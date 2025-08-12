---
layout: publication
title: 'Ctp-net: Character Texture Perception Network For Document Image Forgery Localization'
authors: Xin Liao, Siliang Chen, Jiaxin Chen, Tianyi Wang, Xiehua Li
conference: Arxiv
year: 2023
bibkey: liao2023ctp
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.02158'}]
tags: []
short_authors: Liao et al.
---
Due to the progression of information technology in recent years, document
images have been widely disseminated on social networks. With the help of
powerful image editing tools, document images are easily forged without leaving
visible manipulation traces, which leads to severe issues if significant
information is falsified for malicious use. Therefore, the research of document
image forensics is worth further exploring. In this paper, we propose a
Character Texture Perception Network (CTP-Net) to localize the forged regions
in document images. Specifically, considering the characters with semantics in
a document image are highly vulnerable, capturing the forgery traces is the key
to localize the forged regions. We design a Character Texture Stream (CTS)
based on optical character recognition to capture features of text areas that
are essential components of a document image. Meanwhile, texture features of
the whole document image are exploited by an Image Texture Stream (ITS).
Combining the features extracted from the CTS and the ITS, the CTP-Net can
reveal more subtle forgery traces from document images. Moreover, to overcome
the challenge caused by the lack of fake document images, we design a data
generation strategy that is utilized to construct a Fake Chinese Trademark
dataset (FCTM). Experimental results on different datasets demonstrate that the
proposed CTP-Net is able to localize multi-scale forged areas in document
images, and outperform the state-of-the-art forgery localization methods, even
though post-processing operations are applied.