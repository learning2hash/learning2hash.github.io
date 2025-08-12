---
layout: publication
title: Interactive Video Stylization Using Few-shot Patch-based Training
authors: "Ond\u0159ej Texler, David Futschik, Michal Ku\u010Dera, Ond\u0159ej Jamri\u0161\
  ka, \u0160\xE1rka Sochorov\xE1, Menglei Chai, Sergey Tulyakov, Daniel S\xFDkora"
conference: ACM Transactions on Graphics
year: 2020
bibkey: texler2020interactive
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.14489'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Texler et al.
---
In this paper, we present a learning-based method to the keyframe-based video
stylization that allows an artist to propagate the style from a few selected
keyframes to the rest of the sequence. Its key advantage is that the resulting
stylization is semantically meaningful, i.e., specific parts of moving objects
are stylized according to the artist's intention. In contrast to previous style
transfer techniques, our approach does not require any lengthy pre-training
process nor a large training dataset. We demonstrate how to train an appearance
translation network from scratch using only a few stylized exemplars while
implicitly preserving temporal consistency. This leads to a video stylization
framework that supports real-time inference, parallel processing, and random
access to an arbitrary output frame. It can also merge the content from
multiple keyframes without the need to perform an explicit blending operation.
We demonstrate its practical utility in various interactive scenarios, where
the user paints over a selected keyframe and sees her style transferred to an
existing recorded sequence or a live video stream.