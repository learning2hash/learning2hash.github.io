---
layout: publication
title: 'Megdet: A Large Mini-batch Object Detector'
authors: Chao Peng, Tete Xiao, Zeming Li, Yuning Jiang, Xiangyu Zhang, Kai Jia, Gang
  Yu, Jian Sun
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: peng2017megdet
citations: 329
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.07240'}]
tags: ["CVPR"]
short_authors: Peng et al.
---
The improvements in recent CNN-based object detection works, from R-CNN [11],
Fast/Faster R-CNN [10, 31] to recent Mask R-CNN [14] and RetinaNet [24], mainly
come from new network, new framework, or novel loss design. But mini-batch
size, a key factor in the training, has not been well studied. In this paper,
we propose a Large MiniBatch Object Detector (MegDet) to enable the training
with much larger mini-batch size than before (e.g. from 16 to 256), so that we
can effectively utilize multiple GPUs (up to 128 in our experiments) to
significantly shorten the training time. Technically, we suggest a learning
rate policy and Cross-GPU Batch Normalization, which together allow us to
successfully train a large mini-batch detector in much less time (e.g., from 33
hours to 4 hours), and achieve even better accuracy. The MegDet is the backbone
of our submission (mmAP 52.5%) to COCO 2017 Challenge, where we won the 1st
place of Detection task.