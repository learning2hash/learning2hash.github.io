---
layout: publication
title: 'Infogen: Generating Complex Statistical Infographics From Documents'
authors: Akash Ghosh, Aparna Garimella, Pritika Ramu, Sambaran Bandyopadhyay, Sriparna
  Saha
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2025
bibkey: ghosh2025infogen
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.20046'}]
tags: []
short_authors: Ghosh et al.
---
Statistical infographics are powerful tools that simplify complex data into visually engaging and easy-to-understand formats. Despite advancements in AI, particularly with LLMs, existing efforts have been limited to generating simple charts, with no prior work addressing the creation of complex infographics from text-heavy documents that demand a deep understanding of the content. We address this gap by introducing the task of generating statistical infographics composed of multiple sub-charts (e.g., line, bar, pie) that are contextually accurate, insightful, and visually aligned. To achieve this, we define infographic metadata that includes its title and textual insights, along with sub-chart-specific details such as their corresponding data and alignment. We also present Infodat, the first benchmark dataset for text-to-infographic metadata generation, where each sample links a document to its metadata. We propose Infogen, a two-stage framework where fine-tuned LLMs first generate metadata, which is then converted into infographic code. Extensive evaluations on Infodat demonstrate that Infogen achieves state-of-the-art performance, outperforming both closed and open-source LLMs in text-to-statistical infographic generation.