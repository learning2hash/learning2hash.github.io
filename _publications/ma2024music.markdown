---
layout: publication
title: 'Music Auto-tagging In The Long Tail: A Few-shot Approach'
authors: T. Aleksandra Ma, Alexander Lerch
conference: Arxiv
year: 2024
bibkey: ma2024music
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.07730'}]
tags: ["Few Shot & Zero Shot"]
short_authors: T. Aleksandra Ma, Alexander Lerch
---
In the realm of digital music, using tags to efficiently organize and
retrieve music from extensive databases is crucial for music catalog owners.
Human tagging by experts is labor-intensive but mostly accurate, whereas
automatic tagging through supervised learning has approached satisfying
accuracy but is restricted to a predefined set of training tags. Few-shot
learning offers a viable solution to expand beyond this small set of predefined
tags by enabling models to learn from only a few human-provided examples to
understand tag meanings and subsequently apply these tags autonomously. We
propose to integrate few-shot learning methodology into multi-label music
auto-tagging by using features from pre-trained models as inputs to a
lightweight linear classifier, also known as a linear probe. We investigate
different popular pre-trained features, as well as different few-shot
parametrizations with varying numbers of classes and samples per class. Our
experiments demonstrate that a simple model with pre-trained features can
achieve performance close to state-of-the-art models while using significantly
less training data, such as 20 samples per tag. Additionally, our linear probe
performs competitively with leading models when trained on the entire training
dataset. The results show that this transfer learning-based few-shot approach
could effectively address the issue of automatically assigning long-tail tags
with only limited labeled data.