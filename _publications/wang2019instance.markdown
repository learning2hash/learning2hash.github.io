---
layout: publication
title: Instance Shadow Detection
authors: Tianyu Wang, Xiaowei Hu, Qiong Wang, Pheng-ann Heng, Chi-wing Fu
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: wang2019instance
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07034'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
Instance shadow detection is a brand new problem, aiming to find shadow
instances paired with object instances. To approach it, we first prepare a new
dataset called SOBA, named after Shadow-OBject Association, with 3,623 pairs of
shadow and object instances in 1,000 photos, each with individual labeled
masks. Second, we design LISA, named after Light-guided Instance Shadow-object
Association, an end-to-end framework to automatically predict the shadow and
object instances, together with the shadow-object associations and light
direction. Then, we pair up the predicted shadow and object instances, and
match them with the predicted shadow-object associations to generate the final
results. In our evaluations, we formulate a new metric named the shadow-object
average precision to measure the performance of our results. Further, we
conducted various experiments and demonstrate our method's applicability on
light direction estimation and photo editing.