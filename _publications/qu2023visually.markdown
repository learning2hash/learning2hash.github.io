---
layout: publication
title: Visually-aware Context Modeling For News Image Captioning
authors: Tingyu Qu, Tinne Tuytelaars, Marie-Francine Moens
conference: Arxiv
year: 2023
bibkey: qu2023visually
citations: 1
additional_links: [{name: Code, url: 'https://github.com/tingyu215/VACNIC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2308.08325'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Tingyu Qu, Tinne Tuytelaars, Marie-Francine Moens
---
News Image Captioning aims to create captions from news articles and images,
emphasizing the connection between textual context and visual elements.
Recognizing the significance of human faces in news images and the face-name
co-occurrence pattern in existing datasets, we propose a face-naming module for
learning better name embeddings. Apart from names, which can be directly linked
to an image area (faces), news image captions mostly contain context
information that can only be found in the article. We design a retrieval
strategy using CLIP to retrieve sentences that are semantically close to the
image, mimicking human thought process of linking articles to images.
Furthermore, to tackle the problem of the imbalanced proportion of article
context and image context in captions, we introduce a simple yet effective
method Contrasting with Language Model backbone (CoLaM) to the training
pipeline. We conduct extensive experiments to demonstrate the efficacy of our
framework. We out-perform the previous state-of-the-art (without external data)
by 7.97/5.80 CIDEr scores on GoodNews/NYTimes800k. Our code is available at
https://github.com/tingyu215/VACNIC.