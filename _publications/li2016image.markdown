---
layout: publication
title: Image Co-localization By Mimicking A Good Detector's Confidence Score Distribution
authors: Yao Li, Linqiao Liu, Chunhua Shen, Anton van Den Hengel
conference: Arxiv
year: 2016
bibkey: li2016image
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.04619'}]
tags: []
short_authors: Li et al.
---
Given a set of images containing objects from the same category, the task of
image co-localization is to identify and localize each instance. This paper
shows that this problem can be solved by a simple but intriguing idea, that is,
a common object detector can be learnt by making its detection confidence
scores distributed like those of a strongly supervised detector. More
specifically, we observe that given a set of object proposals extracted from an
image that contains the object of interest, an accurate strongly supervised
object detector should give high scores to only a small minority of proposals,
and low scores to most of them. Thus, we devise an entropy-based objective
function to enforce the above property when learning the common object
detector. Once the detector is learnt, we resort to a segmentation approach to
refine the localization. We show that despite its simplicity, our approach
outperforms state-of-the-art methods.