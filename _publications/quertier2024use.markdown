---
layout: publication
title: Use Of Multi-cnns For Section Analysis In Static Malware Detection
authors: "Tony Quertier, Gr\xE9goire Barru\xE9"
conference: Arxiv
year: 2024
bibkey: quertier2024use
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.04102'}]
tags: []
short_authors: "Tony Quertier, Gr\xE9goire Barru\xE9"
---
Existing research on malware detection focuses almost exclusively on the
detection rate. However, in some cases, it is also important to understand the
results of our algorithm, or to obtain more information, such as where to
investigate in the file for an analyst. In this aim, we propose a new model to
analyze Portable Executable files. Our method consists in splitting the files
in different sections, then transform each section into an image, in order to
train convolutional neural networks to treat specifically each identified
section. Then we use all these scores returned by CNNs to compute a final
detection score, using models that enable us to improve our analysis of the
importance of each section in the final score.