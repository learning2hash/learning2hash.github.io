---
layout: publication
title: Exploring Fine-grained Retail Product Discrimination With Zero-shot Object
  Classification Using Vision-language Models
authors: Anil Osman Tur, Alessandro Conti, Cigdem Beyan, Davide Boscaini, Roberto
  Larcher, Stefano Messelodi, Fabio Poiesi, Elisa Ricci
conference: 2024 IEEE 8th Forum on Research and Technologies for Society and Industry
  Innovation (RTSI)
year: 2024
bibkey: tur2024exploring
citations: 0
additional_links: [{name: Code, url: 'https://github.com/AnilOsmanTur/Zero-shot-Retail-Product-Classification'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.14963'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tur et al.
---
In smart retail applications, the large number of products and their frequent
turnover necessitate reliable zero-shot object classification methods. The
zero-shot assumption is essential to avoid the need for re-training the
classifier every time a new product is introduced into stock or an existing
product undergoes rebranding. In this paper, we make three key contributions.
Firstly, we introduce the MIMEX dataset, comprising 28 distinct product
categories. Unlike existing datasets in the literature, MIMEX focuses on
fine-grained product classification and includes a diverse range of retail
products. Secondly, we benchmark the zero-shot object classification
performance of state-of-the-art vision-language models (VLMs) on the proposed
MIMEX dataset. Our experiments reveal that these models achieve unsatisfactory
fine-grained classification performance, highlighting the need for specialized
approaches. Lastly, we propose a novel ensemble approach that integrates
embeddings from CLIP and DINOv2 with dimensionality reduction techniques to
enhance classification performance. By combining these components, our ensemble
approach outperforms VLMs, effectively capturing visual cues crucial for
fine-grained product discrimination. Additionally, we introduce a class
adaptation method that utilizes visual prototyping with limited samples in
scenarios with scarce labeled data, addressing a critical need in retail
environments where product variety frequently changes. To encourage further
research into zero-shot object classification for smart retail applications, we
will release both the MIMEX dataset and benchmark to the research community.
Interested researchers can contact the authors for details on the terms and
conditions of use. The code is available:
https://github.com/AnilOsmanTur/Zero-shot-Retail-Product-Classification.