---
layout: publication
title: 'Safe-clip: Removing NSFW Concepts From Vision-and-language Models'
authors: Samuele Poppi, Tobia Poppi, Federico Cocchi, Marcella Cornia, Lorenzo Baraldi,
  Rita Cucchiara
conference: Lecture Notes in Computer Science
year: 2023
bibkey: poppi2023safe
citations: 14
additional_links: [{name: Code, url: 'https://github.com/aimagelab/safe-clip'}, {
    name: Paper, url: 'https://arxiv.org/abs/2311.16254'}]
tags: ["Multimodal Retrieval", "Privacy & Security"]
short_authors: Poppi et al.
---
Large-scale vision-and-language models, such as CLIP, are typically trained
on web-scale data, which can introduce inappropriate content and lead to the
development of unsafe and biased behavior. This, in turn, hampers their
applicability in sensitive and trustworthy contexts and could raise significant
concerns in their adoption. Our research introduces a novel approach to
enhancing the safety of vision-and-language models by diminishing their
sensitivity to NSFW (not safe for work) inputs. In particular, our methodology
seeks to sever "toxic" linguistic and visual concepts, unlearning the linkage
between unsafe linguistic or visual items and unsafe regions of the embedding
space. We show how this can be done by fine-tuning a CLIP model on synthetic
data obtained from a large language model trained to convert between safe and
unsafe sentences, and a text-to-image generator. We conduct extensive
experiments on the resulting embedding space for cross-modal retrieval,
text-to-image, and image-to-text generation, where we show that our model can
be remarkably employed with pre-trained generative models. Our source code and
trained models are available at: https://github.com/aimagelab/safe-clip.