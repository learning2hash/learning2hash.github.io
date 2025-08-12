---
layout: publication
title: Visual-semantic Contrastive Alignment For Few-shot Image Classification
authors: Mohamed Afham, Ranga Rodrigo
conference: Arxiv
year: 2022
bibkey: afham2022visual
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.11000'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Mohamed Afham, Ranga Rodrigo
---
Few-Shot learning aims to train and optimize a model that can adapt to unseen
visual classes with only a few labeled examples. The existing few-shot learning
(FSL) methods, heavily rely only on visual data, thus fail to capture the
semantic attributes to learn a more generalized version of the visual concept
from very few examples. However, it is a known fact that human visual learning
benefits immensely from inputs from multiple modalities such as vision,
language, and audio. Inspired by the human learning nature of encapsulating the
existing knowledge of a visual category which is in the form of language, we
introduce a contrastive alignment mechanism for visual and semantic feature
vectors to learn much more generalized visual concepts for few-shot learning.
Our method simply adds an auxiliary contrastive learning objective which
captures the contextual knowledge of a visual category from a strong textual
encoder in addition to the existing training mechanism. Hence, the approach is
more generalized and can be plugged into any existing FSL method. The
pre-trained semantic feature extractor (learned from a large-scale text
corpora) we use in our approach provides a strong contextual prior knowledge to
assist FSL. The experimental results done in popular FSL datasets show that our
approach is generic in nature and provides a strong boost to the existing FSL
baselines.