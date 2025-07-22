---
layout: publication
title: How To Make Cross Encoder A Good Teacher For Efficient Image-text Retrieval?
authors: Chen Yuxin, Ma Zongyang, Zhang Ziqi, Qi Zhongang, Yuan Chunfeng, Li Bing,
  Pu Junfu, Shan Ying, Qi Xiaojuan, Hu Weiming
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: chen2024how
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.07479'}]
tags: ["Efficiency", "CVPR", "Text-Retrieval"]
short_authors: Chen et al.
---
Dominant dual-encoder models enable efficient image-text retrieval but suffer
from limited accuracy while the cross-encoder models offer higher accuracy at
the expense of efficiency. Distilling cross-modality matching knowledge from
cross-encoder to dual-encoder provides a natural approach to harness their
strengths. Thus we investigate the following valuable question: how to make
cross-encoder a good teacher for dual-encoder? Our findings are threefold:(1)
Cross-modal similarity score distribution of cross-encoder is more concentrated
while the result of dual-encoder is nearly normal making vanilla logit
distillation less effective. However ranking distillation remains practical as
it is not affected by the score distribution.(2) Only the relative order
between hard negatives conveys valid knowledge while the order information
between easy negatives has little significance.(3) Maintaining the coordination
between distillation loss and dual-encoder training loss is beneficial for
knowledge transfer. Based on these findings we propose a novel Contrastive
Partial Ranking Distillation (CPRD) method which implements the objective of
mimicking relative order between hard negative samples with contrastive
learning. This approach coordinates with the training of the dual-encoder
effectively transferring valid knowledge from the cross-encoder to the
dual-encoder. Extensive experiments on image-text retrieval and ranking tasks
show that our method surpasses other distillation methods and significantly
improves the accuracy of dual-encoder.