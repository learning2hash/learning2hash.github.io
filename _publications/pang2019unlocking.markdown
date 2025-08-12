---
layout: publication
title: Unlocking The Full Potential Of Small Data With Diverse Supervision
authors: Ziqi Pang, Zhiyuan Hu, Pavel Tokmakov, Yu-xiong Wang, Martial Hebert
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: pang2019unlocking
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.12911'}]
tags: ["CVPR", "Datasets", "Few Shot & Zero Shot"]
short_authors: Pang et al.
---
Virtually all of deep learning literature relies on the assumption of large
amounts of available training data. Indeed, even the majority of few-shot
learning methods rely on a large set of "base classes" for pretraining. This
assumption, however, does not always hold. For some tasks, annotating a large
number of classes can be infeasible, and even collecting the images themselves
can be a challenge in some scenarios. In this paper, we study this problem and
call it "Small Data" setting, in contrast to "Big Data". To unlock the full
potential of small data, we propose to augment the models with annotations for
other related tasks, thus increasing their generalization abilities. In
particular, we use the richly annotated scene parsing dataset ADE20K to
construct our realistic Long-tail Recognition with Diverse Supervision (LRDS)
benchmark by splitting the object categories into head and tail based on their
distribution. Following the standard few-shot learning protocol, we use the
head classes for representation learning and the tail classes for evaluation.
Moreover, we further subsample the head categories and images to generate two
novel settings which we call "Scarce-Class" and "Scarce-Image", respectively
corresponding to the shortage of samples for rare classes and training images.
Finally, we analyze the effect of applying various additional supervision
sources under the proposed settings. Our experiments demonstrate that densely
labeling a small set of images can indeed largely remedy the small data
constraints.