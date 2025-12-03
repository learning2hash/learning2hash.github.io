---
layout: publication
title: Building An Open-vocabulary Video CLIP Model With Better Architectures, Optimization
  And Data
authors: Zuxuan Wu, Zejia Weng, Wujian Peng, Xitong Yang, Ang Li, Larry S. Davis,
  Yu-Gang Jiang
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: wu2023building
citations: 14
additional_links: [{name: Code, url: 'https://github.com/wengzejia1/Open-VCLIP'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.05010'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Video Retrieval"]
short_authors: Wu et al.
---
Despite significant results achieved by Contrastive Language-Image
Pretraining (CLIP) in zero-shot image recognition, limited effort has been made
exploring its potential for zero-shot video recognition. This paper presents
Open-VCLIP++, a simple yet effective framework that adapts CLIP to a strong
zero-shot video classifier, capable of identifying novel actions and events
during testing. Open-VCLIP++ minimally modifies CLIP to capture
spatial-temporal relationships in videos, thereby creating a specialized video
classifier while striving for generalization. We formally demonstrate that
training Open-VCLIP++ is tantamount to continual learning with zero historical
data. To address this problem, we introduce Interpolated Weight Optimization, a
technique that leverages the advantages of weight interpolation during both
training and testing. Furthermore, we build upon large language models to
produce fine-grained video descriptions. These detailed descriptions are
further aligned with video features, facilitating a better transfer of CLIP to
the video domain. Our approach is evaluated on three widely used action
recognition datasets, following a variety of zero-shot evaluation protocols.
The results demonstrate that our method surpasses existing state-of-the-art
techniques by significant margins. Specifically, we achieve zero-shot accuracy
scores of 88.1%, 58.7%, and 81.2% on UCF, HMDB, and Kinetics-600 datasets
respectively, outpacing the best-performing alternative methods by 8.5%, 8.2%,
and 12.3%. We also evaluate our approach on the MSR-VTT video-text retrieval
dataset, where it delivers competitive video-to-text and text-to-video
retrieval performance, while utilizing substantially less fine-tuning data
compared to other methods. Code is released at
https://github.com/wengzejia1/Open-VCLIP.