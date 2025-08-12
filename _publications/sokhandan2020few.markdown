---
layout: publication
title: A Few-shot Sequential Approach For Object Counting
authors: Negin Sokhandan, Pegah Kamousi, Alejandro Posada, Eniola Alese, Negar Rostamzadeh
conference: Arxiv
year: 2020
bibkey: sokhandan2020few
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.01899'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Sokhandan et al.
---
In this work, we address the problem of few-shot multi-class object counting
with point-level annotations. The proposed technique leverages a class agnostic
attention mechanism that sequentially attends to objects in the image and
extracts their relevant features. This process is employed on an adapted
prototypical-based few-shot approach that uses the extracted features to
classify each one either as one of the classes present in the support set
images or as background. The proposed technique is trained on point-level
annotations and uses a novel loss function that disentangles class-dependent
and class-agnostic aspects of the model to help with the task of few-shot
object counting. We present our results on a variety of
object-counting/detection datasets, including FSOD and MS COCO. In addition, we
introduce a new dataset that is specifically designed for weakly supervised
multi-class object counting/detection and contains considerably different
classes and distribution of number of classes/instances per image compared to
the existing datasets. We demonstrate the robustness of our approach by testing
our system on a totally different distribution of classes from what it has been
trained on.