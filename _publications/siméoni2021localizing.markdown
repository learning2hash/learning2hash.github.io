---
layout: publication
title: Localizing Objects With Self-supervised Transformers And No Labels
authors: "Oriane Sim\xE9oni, Gilles Puy, Huy V. Vo, Simon Roburin, Spyros Gidaris,\
  \ Andrei Bursuc, Patrick P\xE9rez, Renaud Marlet, Jean Ponce"
conference: BMVC 2021
year: 2021
bibkey: "sim\xE9oni2021localizing"
citations: 51
additional_links: [{name: Code, url: 'https://github.com/valeoai/LOST'}, {name: Paper,
    url: 'https://arxiv.org/abs/2109.14279'}]
tags: ["Self-Supervised"]
short_authors: "Sim\xE9oni et al."
---
Localizing objects in image collections without supervision can help to avoid
expensive annotation campaigns. We propose a simple approach to this problem,
that leverages the activation features of a vision transformer pre-trained in a
self-supervised manner. Our method, LOST, does not require any external object
proposal nor any exploration of the image collection; it operates on a single
image. Yet, we outperform state-of-the-art object discovery methods by up to 8
CorLoc points on PASCAL VOC 2012. We also show that training a class-agnostic
detector on the discovered objects boosts results by another 7 points.
Moreover, we show promising results on the unsupervised object discovery task.
The code to reproduce our results can be found at
https://github.com/valeoai/LOST.