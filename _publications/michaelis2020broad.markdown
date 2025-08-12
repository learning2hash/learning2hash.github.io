---
layout: publication
title: A Broad Dataset Is All You Need For One-shot Object Detection
authors: Claudio Michaelis, Matthias Bethge, Alexander S. Ecker
conference: Arxiv
year: 2020
bibkey: michaelis2020broad
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.04267'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Claudio Michaelis, Matthias Bethge, Alexander S. Ecker
---
Is it possible to detect arbitrary objects from a single example? A central
problem of all existing attempts at one-shot object detection is the
generalization gap: Object categories used during training are detected much
more reliably than novel ones. We here show that this generalization gap can be
nearly closed by increasing the number of object categories used during
training. Doing so allows us to improve generalization from seen to unseen
classes from 45% to 89% and improve the state-of-the-art on COCO by 5.4 %AP50
(from 22.0 to 27.5). We verify that the effect is caused by the number of
categories and not the number of training samples, and that it holds for
different models, backbones and datasets. This result suggests that the key to
strong few-shot detection models may not lie in sophisticated metric learning
approaches, but instead simply in scaling the number of categories. We hope
that our findings will help to better understand the challenges of few-shot
learning and encourage future data annotation efforts to focus on wider
datasets with a broader set of categories rather than gathering more samples
per category.