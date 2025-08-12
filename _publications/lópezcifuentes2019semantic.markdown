---
layout: publication
title: Semantic-aware Scene Recognition
authors: "Alejandro L\xF3pez-cifuentes, Marcos Escudero-vi\xF1olo, Jes\xFAs Besc\xF3\
  s, \xC1lvaro Garc\xEDa-mart\xEDn"
conference: Pattern Recognition
year: 2020
bibkey: "l\xF3pezcifuentes2019semantic"
citations: 101
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.02410'}]
tags: ["Datasets", "Evaluation"]
short_authors: "L\xF3pez-cifuentes et al."
---
Scene recognition is currently one of the top-challenging research fields in
computer vision. This may be due to the ambiguity between classes: images of
several scene classes may share similar objects, which causes confusion among
them. The problem is aggravated when images of a particular scene class are
notably different. Convolutional Neural Networks (CNNs) have significantly
boosted performance in scene recognition, albeit it is still far below from
other recognition tasks (e.g., object or image recognition). In this paper, we
describe a novel approach for scene recognition based on an end-to-end
multi-modal CNN that combines image and context information by means of an
attention module. Context information, in the shape of semantic segmentation,
is used to gate features extracted from the RGB image by leveraging on
information encoded in the semantic representation: the set of scene objects
and stuff, and their relative locations. This gating process reinforces the
learning of indicative scene content and enhances scene disambiguation by
refocusing the receptive fields of the CNN towards them. Experimental results
on four publicly available datasets show that the proposed approach outperforms
every other state-of-the-art method while significantly reducing the number of
network parameters. All the code and data used along this paper is available at
https://github.com/vpulab/Semantic-Aware-Scene-Recognition