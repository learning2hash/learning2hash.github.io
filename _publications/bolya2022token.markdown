---
layout: publication
title: 'Token Merging: Your Vit But Faster'
authors: Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer,
  Judy Hoffman
conference: Arxiv
year: 2022
bibkey: bolya2022token
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.09461'}]
tags: []
short_authors: Bolya et al.
---
We introduce Token Merging (ToMe), a simple method to increase the throughput
of existing ViT models without needing to train. ToMe gradually combines
similar tokens in a transformer using a general and light-weight matching
algorithm that is as fast as pruning while being more accurate. Off-the-shelf,
ToMe can 2x the throughput of state-of-the-art ViT-L @ 512 and ViT-H @ 518
models on images and 2.2x the throughput of ViT-L on video with only a 0.2-0.3%
accuracy drop in each case. ToMe can also easily be applied during training,
improving in practice training speed up to 2x for MAE fine-tuning on video.
Training with ToMe further minimizes accuracy drop, leading to 2x the
throughput of ViT-B on audio for only a 0.4% mAP drop. Qualitatively, we find
that ToMe merges object parts into one token, even over multiple frames of
video. Overall, ToMe's accuracy and speed are competitive with state-of-the-art
on images, video, and audio.