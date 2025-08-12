---
layout: publication
title: Few Shot Learning With No Labels
authors: Aditya Bharti, N. B. Vineeth, C. V. Jawahar
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: bharti2020few
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.13751'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Aditya Bharti, N. B. Vineeth, C. V. Jawahar
---
Few-shot learners aim to recognize new categories given only a small number
of training samples. The core challenge is to avoid overfitting to the limited
data while ensuring good generalization to novel classes. Existing literature
makes use of vast amounts of annotated data by simply shifting the label
requirement from novel classes to base classes. Since data annotation is
time-consuming and costly, reducing the label requirement even further is an
important goal. To that end, our paper presents a more challenging few-shot
setting where no label access is allowed during training or testing. By
leveraging self-supervision for learning image representations and image
similarity for classification at test time, we achieve competitive baselines
while using \textbf\{zero\} labels, which is at least fewer labels than
state-of-the-art. We hope that this work is a step towards developing few-shot
learning methods which do not depend on annotated data at all. Our code will be
publicly released.