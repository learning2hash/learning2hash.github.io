---
layout: publication
title: Discrete Few-shot Learning For Pan Privacy
authors: Roei Gelbhart, Benjamin I. P. Rubinstein
conference: Arxiv
year: 2020
citations: 1
bibkey: gelbhart2020discrete
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.13120'}]
tags: [Hashing Methods]
---
In this paper we present the first baseline results for the task of few-shot
learning of discrete embedding vectors for image recognition. Few-shot learning
is a highly researched task, commonly leveraged by recognition systems that are
resource constrained to train on a small number of images per class. Few-shot
systems typically store a continuous embedding vector of each class, posing a
risk to privacy where system breaches or insider threats are a concern. Using
discrete embedding vectors, we devise a simple cryptographic protocol, which
uses one-way hash functions in order to build recognition systems that do not
store their users' embedding vectors directly, thus providing the guarantee of
computational pan privacy in a practical and wide-spread setting.