---
layout: publication
title: End-to-end Optimized Image Compression For Multiple Machine Tasks
authors: "Lahiru D. Chamain, Fabien Racap\xE9, Jean B\xE9gaint, Akshay Pushparaja,\
  \ Simon Feltman"
conference: Arxiv
year: 2021
bibkey: chamain2021end
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04178'}]
tags: ["Evaluation"]
short_authors: Chamain et al.
---
An increasing share of captured images and videos are transmitted for storage
and remote analysis by computer vision algorithms, rather than to be viewed by
humans. Contrary to traditional standard codecs with engineered tools, neural
network based codecs can be trained end-to-end to optimally compress images
with respect to a target rate and any given differentiable performance metric.
Although it is possible to train such compression tools to achieve better
rate-accuracy performance for a particular computer vision task, it could be
practical and relevant to re-use the compressed bit-stream for multiple machine
tasks. For this purpose, we introduce 'Connectors' that are inserted between
the decoder and the task algorithms to enable a direct transformation of the
compressed content, which was previously optimized for a specific task, to
multiple other machine tasks. We demonstrate the effectiveness of the proposed
method by achieving significant rate-accuracy performance improvement for both
image classification and object segmentation, using the same bit-stream,
originally optimized for object detection.