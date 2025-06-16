---
layout: publication
title: All You Need To Know About Training Image Retrieval Models
authors: Gabriele Berton, Kevin Musgrave, Carlo Masone
conference: Arxiv
year: 2025
citations: 0
bibkey: berton2025all
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.13045'}, {name: Code,
    url: 'https://github.com/gmberton/image-retrieval'}]
tags: [Applications, Evaluation Metrics, Tools and Libraries]
---
Image retrieval is the task of finding images in a database that are most
similar to a given query image. The performance of an image retrieval pipeline
depends on many training-time factors, including the embedding model
architecture, loss function, data sampler, mining function, learning rate(s),
and batch size. In this work, we run tens of thousands of training runs to
understand the effect each of these factors has on retrieval accuracy. We also
discover best practices that hold across multiple datasets. The code is
available at https://github.com/gmberton/image-retrieval