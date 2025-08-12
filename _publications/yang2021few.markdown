---
layout: publication
title: Few-shot Transformation Of Common Actions Into Time And Space
authors: Pengwan Yang, Pascal Mettes, Cees G. M. Snoek
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: yang2021few
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.02439'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Pengwan Yang, Pascal Mettes, Cees G. M. Snoek
---
This paper introduces the task of few-shot common action localization in time
and space. Given a few trimmed support videos containing the same but unknown
action, we strive for spatio-temporal localization of that action in a long
untrimmed query video. We do not require any class labels, interval bounds, or
bounding boxes. To address this challenging task, we introduce a novel few-shot
transformer architecture with a dedicated encoder-decoder structure optimized
for joint commonality learning and localization prediction, without the need
for proposals. Experiments on our reorganizations of the AVA and UCF101-24
datasets show the effectiveness of our approach for few-shot common action
localization, even when the support videos are noisy. Although we are not
specifically designed for common localization in time only, we also compare
favorably against the few-shot and one-shot state-of-the-art in this setting.
Lastly, we demonstrate that the few-shot transformer is easily extended to
common action localization per pixel.