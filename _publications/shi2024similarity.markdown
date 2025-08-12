---
layout: publication
title: Similarity Distance-based Label Assignment For Tiny Object Detection
authors: Shuohao Shi, Qiang Fang, Tong Zhao, Xin Xu
conference: 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2024
bibkey: shi2024similarity
citations: 5
additional_links: [{name: Code, url: 'https://github.com/cszzshi/SimD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2407.02394'}]
tags: ["IROS"]
short_authors: Shi et al.
---
Tiny object detection is becoming one of the most challenging tasks in
computer vision because of the limited object size and lack of information. The
label assignment strategy is a key factor affecting the accuracy of object
detection. Although there are some effective label assignment strategies for
tiny objects, most of them focus on reducing the sensitivity to the bounding
boxes to increase the number of positive samples and have some fixed
hyperparameters need to set. However, more positive samples may not necessarily
lead to better detection results, in fact, excessive positive samples may lead
to more false positives. In this paper, we introduce a simple but effective
strategy named the Similarity Distance (SimD) to evaluate the similarity
between bounding boxes. This proposed strategy not only considers both location
and shape similarity but also learns hyperparameters adaptively, ensuring that
it can adapt to different datasets and various object sizes in a dataset. Our
approach can be simply applied in common anchor-based detectors in place of the
IoU for label assignment and Non Maximum Suppression (NMS). Extensive
experiments on four mainstream tiny object detection datasets demonstrate
superior performance of our method, especially, 1.8 AP points and 4.1 AP points
of very tiny higher than the state-of-the-art competitors on AI-TOD. Code is
available at: https://github.com/cszzshi/SimD.