---
layout: publication
title: CLIP For All Things Zero-shot Sketch-based Image Retrieval, Fine-grained Or
  Not
authors: Aneeshan Sain, Ayan Kumar Bhunia, Pinaki Nath Chowdhury, Subhadeep Koley,
  Tao Xiang, Yi-Zhe Song
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: sain2023clip
citations: 93
additional_links: [{name: Other, url: 'https://aneeshan95.github.io/Sketch_LVM/'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.13440'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Distance Metric Learning,
  CVPR]
short_authors: Sain et al.
---
In this paper, we leverage CLIP for zero-shot sketch based image retrieval
(ZS-SBIR). We are largely inspired by recent advances on foundation models and
the unparalleled generalisation ability they seem to offer, but for the first
time tailor it to benefit the sketch community. We put forward novel designs on
how best to achieve this synergy, for both the category setting and the
fine-grained setting ("all"). At the very core of our solution is a prompt
learning setup. First we show just via factoring in sketch-specific prompts, we
already have a category-level ZS-SBIR system that overshoots all prior arts, by
a large margin (24.8%) - a great testimony on studying the CLIP and ZS-SBIR
synergy. Moving onto the fine-grained setup is however trickier, and requires a
deeper dive into this synergy. For that, we come up with two specific designs
to tackle the fine-grained matching nature of the problem: (i) an additional
regularisation loss to ensure the relative separation between sketches and
photos is uniform across categories, which is not the case for the gold
standard standalone triplet loss, and (ii) a clever patch shuffling technique
to help establishing instance-level structural correspondences between
sketch-photo pairs. With these designs, we again observe significant
performance gains in the region of 26.9% over previous state-of-the-art. The
take-home message, if any, is the proposed CLIP and prompt learning paradigm
carries great promise in tackling other sketch-related tasks (not limited to
ZS-SBIR) where data scarcity remains a great challenge. Project page:
https://aneeshan95.github.io/Sketch_LVM/