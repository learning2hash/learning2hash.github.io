---
layout: publication
title: Look-ups Are Not (yet) All You Need For Deep Learning Inference
authors: Calvin Mccarter, Nicholas Dronen
conference: Arxiv
year: 2022
citations: 1
bibkey: mccarter2022look
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05808'}]
tags: [Hashing Methods]
---
Fast approximations to matrix multiplication have the potential to
dramatically reduce the cost of neural network inference. Recent work on
approximate matrix multiplication proposed to replace costly multiplications
with table-lookups by fitting a fast hash function from training data. In this
work, we propose improvements to this previous work, targeted to the deep
learning inference setting, where one has access to both training data and
fixed (already learned) model weight matrices. We further propose a fine-tuning
procedure for accelerating entire neural networks while minimizing loss in
accuracy. Finally, we analyze the proposed method on a simple image
classification task. While we show improvements to prior work, overall
classification accuracy remains substantially diminished compared to exact
matrix multiplication. Our work, despite this negative result, points the way
towards future efforts to accelerate inner products with fast nonlinear hashing
methods.