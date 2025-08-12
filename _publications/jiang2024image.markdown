---
layout: publication
title: 'Image Copy-move Forgery Detection And Localization Scheme: How To Avoid Missed
  Detection And False Alarm'
authors: Li Jiang, Zhaowei Lu, Yuebing Gao, Yifan Wang
conference: Arxiv
year: 2024
bibkey: jiang2024image
citations: 0
additional_links: [{name: Code, url: 'https://github.com/LUZW1998/CMFDL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.03271'}]
tags: ["Evaluation"]
short_authors: Jiang et al.
---
Image copy-move is an operation that replaces one part of the image with
another part of the same image, which can be used for illegal purposes due to
the potential semantic changes. Recent studies have shown that keypoint-based
algorithms achieved excellent and robust localization performance even when
small or smooth tampered areas were involved. However, when the input image is
low-resolution, most existing keypoint-based algorithms are difficult to
generate sufficient keypoints, resulting in more missed detections. In
addition, existing algorithms are usually unable to distinguish between Similar
but Genuine Objects (SGO) images and tampered images, resulting in more false
alarms. This is mainly due to the lack of further verification of local
homography matrix in forgery localization stage. To tackle these problems, this
paper firstly proposes an excessive keypoint extraction strategy to overcome
missed detection. Subsequently, a group matching algorithm is used to speed up
the matching of excessive keypoints. Finally, a new iterative forgery
localization algorithm is introduced to quickly form pixel-level localization
results while ensuring a lower false alarm. Extensive experimental results show
that our scheme has superior performance than state-of-the-art algorithms in
overcoming missed detection and false alarm. Our code is available at
https://github.com/LUZW1998/CMFDL.