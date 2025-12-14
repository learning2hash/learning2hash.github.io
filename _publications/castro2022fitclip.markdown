---
layout: publication
title: 'Fitclip: Refining Large-scale Pretrained Image-text Models For Zero-shot Video
  Understanding Tasks'
authors: Santiago Castro, Fabian Caba Heilbron
conference: Arxiv
year: 2022
bibkey: castro2022fitclip
citations: 7
additional_links: [{name: Code, url: 'https://github.com/bryant1410/fitclip'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.13371'}]
tags: [Video Retrieval, Evaluation, Scalability, Few-shot & Zero-shot]
short_authors: Santiago Castro, Fabian Caba Heilbron
---
Large-scale pretrained image-text models have shown incredible zero-shot
performance in a handful of tasks, including video ones such as action
recognition and text-to-video retrieval. However, these models have not been
adapted to video, mainly because they do not account for the time dimension but
also because video frames are different from the typical images (e.g.,
containing motion blur, and less sharpness). In this paper, we present a
fine-tuning strategy to refine these large-scale pretrained image-text models
for zero-shot video understanding tasks. We show that by carefully adapting
these models we obtain considerable improvements on two zero-shot Action
Recognition tasks and three zero-shot Text-to-video Retrieval tasks. The code
is available at https://github.com/bryant1410/fitclip