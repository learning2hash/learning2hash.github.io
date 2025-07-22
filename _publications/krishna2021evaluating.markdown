---
layout: publication
title: Evaluating Contrastive Models For Instance-based Image Retrieval
authors: Krishna Tarun, Mcguinness Kevin, O'connor Noel
conference: Proceedings of the 2021 International Conference on Multimedia Retrieval
year: 2021
bibkey: krishna2021evaluating
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14939'}]
tags: ["Multimodal-Retrieval", "Supervised", "Image-Retrieval", "Evaluation"]
short_authors: Krishna Tarun, Mcguinness Kevin, O'connor Noel
---
In this work, we evaluate contrastive models for the task of image retrieval.
We hypothesise that models that are learned to encode semantic similarity among
instances via discriminative learning should perform well on the task of image
retrieval, where relevancy is defined in terms of instances of the same object.
Through our extensive evaluation, we find that representations from models
trained using contrastive methods perform on-par with (and outperforms) a
pre-trained supervised baseline trained on the ImageNet labels in retrieval
tasks under various configurations. This is remarkable given that the
contrastive models require no explicit supervision. Thus, we conclude that
these models can be used to bootstrap base models to build more robust image
retrieval engines.