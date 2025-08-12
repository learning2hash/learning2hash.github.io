---
layout: publication
title: Saliency-guided Attention Network For Image-sentence Matching
authors: Zhong Ji, Haoran Wang, Jungong Han, Yanwei Pang
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: ji2019saliency
citations: 101
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.09471'}]
tags: ["ICCV"]
short_authors: Ji et al.
---
This paper studies the task of matching image and sentence, where learning
appropriate representations across the multi-modal data appears to be the main
challenge. Unlike previous approaches that predominantly deploy symmetrical
architecture to represent both modalities, we propose Saliency-guided Attention
Network (SAN) that asymmetrically employs visual and textual attention modules
to learn the fine-grained correlation intertwined between vision and language.
The proposed SAN mainly includes three components: saliency detector,
Saliency-weighted Visual Attention (SVA) module, and Saliency-guided Textual
Attention (STA) module. Concretely, the saliency detector provides the visual
saliency information as the guidance for the two attention modules. SVA is
designed to leverage the advantage of the saliency information to improve
discrimination of visual representations. By fusing the visual information from
SVA and textual information as a multi-modal guidance, STA learns
discriminative textual representations that are highly sensitive to visual
clues. Extensive experiments demonstrate SAN can substantially improve the
state-of-the-art results on the benchmark Flickr30K and MSCOCO datasets by a
large margin.