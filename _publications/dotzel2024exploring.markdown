---
layout: publication
title: Exploring The Limits Of Semantic Image Compression At Micro-bits Per Pixel
authors: Jordan Dotzel, Bahaa Kotb, James Dotzel, Mohamed Abdelfattah, Zhiru Zhang
conference: Arxiv
year: 2024
bibkey: dotzel2024exploring
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.13536'}]
tags: ["Efficiency", "Image Retrieval", "Quantization"]
short_authors: Dotzel et al.
---
Traditional methods, such as JPEG, perform image compression by operating on
structural information, such as pixel values or frequency content. These
methods are effective to bitrates around one bit per pixel (bpp) and higher at
standard image sizes. In contrast, text-based semantic compression directly
stores concepts and their relationships using natural language, which has
evolved with humans to efficiently represent these salient concepts. These
methods can operate at extremely low bitrates by disregarding structural
information like location, size, and orientation. In this work, we use GPT-4V
and DALL-E3 from OpenAI to explore the quality-compression frontier for image
compression and identify the limitations of current technology. We push
semantic compression as low as 100 \(\mu\)bpp (up to \(10,000\times\) smaller than
JPEG) by introducing an iterative reflection process to improve the decoded
image. We further hypothesize this 100 \(\mu\)bpp level represents a soft limit
on semantic compression at standard image resolutions.