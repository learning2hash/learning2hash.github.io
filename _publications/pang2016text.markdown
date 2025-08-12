---
layout: publication
title: Text Matching As Image Recognition
authors: Liang Pang, Yanyan Lan, Jiafeng Guo, Jun Xu, Shengxian Wan, Xueqi Cheng
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2016
bibkey: pang2016text
citations: 447
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.06359'}]
tags: ["AAAI"]
short_authors: Pang et al.
---
Matching two texts is a fundamental problem in many natural language
processing tasks. An effective way is to extract meaningful matching patterns
from words, phrases, and sentences to produce the matching score. Inspired by
the success of convolutional neural network in image recognition, where neurons
can capture many complicated patterns based on the extracted elementary visual
patterns such as oriented edges and corners, we propose to model text matching
as the problem of image recognition. Firstly, a matching matrix whose entries
represent the similarities between words is constructed and viewed as an image.
Then a convolutional neural network is utilized to capture rich matching
patterns in a layer-by-layer way. We show that by resembling the compositional
hierarchies of patterns in image recognition, our model can successfully
identify salient signals such as n-gram and n-term matchings. Experimental
results demonstrate its superiority against the baselines.