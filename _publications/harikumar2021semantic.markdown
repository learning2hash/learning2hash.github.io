---
layout: publication
title: Semantic Host-free Trojan Attack
authors: Haripriya Harikumar, Kien Do, Santu Rana, Sunil Gupta, Svetha Venkatesh
conference: Arxiv
year: 2021
bibkey: harikumar2021semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.13414'}]
tags: []
short_authors: Harikumar et al.
---
In this paper, we propose a novel host-free Trojan attack with triggers that
are fixed in the semantic space but not necessarily in the pixel space. In
contrast to existing Trojan attacks which use clean input images as hosts to
carry small, meaningless trigger patterns, our attack considers triggers as
full-sized images belonging to a semantically meaningful object class. Since in
our attack, the backdoored classifier is encouraged to memorize the abstract
semantics of the trigger images than any specific fixed pattern, it can be
later triggered by semantically similar but different looking images. This
makes our attack more practical to be applied in the real-world and harder to
defend against. Extensive experimental results demonstrate that with only a
small number of Trojan patterns for training, our attack can generalize well to
new patterns of the same Trojan class and can bypass state-of-the-art defense
methods.