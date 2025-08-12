---
layout: publication
title: 'Weak Novel Categories Without Tears: A Survey On Weak-shot Learning'
authors: Li Niu
conference: Arxiv
year: 2021
bibkey: niu2021weak
citations: 1
additional_links: [{name: Code, url: 'https://github.com/bcmi/Awesome-Weak-Shot-Learning'},
  {name: Paper, url: 'https://arxiv.org/abs/2110.02651'}]
tags: ["Few Shot & Zero Shot", "Survey Paper"]
short_authors: Li Niu
---
Deep learning is a data-hungry approach, which requires massive training
data. However, it is time-consuming and labor-intensive to collect abundant
fully-annotated training data for all categories. Assuming the existence of
base categories with adequate fully-annotated training samples, different
paradigms requiring fewer training samples or weaker annotations for novel
categories have attracted growing research interest. Among them, zero-shot
(resp., few-shot) learning explores using zero (resp., a few) training samples
for novel categories, which lowers the quantity requirement for novel
categories. Instead, weak-shot learning lowers the quality requirement for
novel categories. Specifically, sufficient training samples are collected for
novel categories but they only have weak annotations. In different tasks, weak
annotations are presented in different forms (e.g., noisy labels for image
classification, image labels for object detection, bounding boxes for
segmentation), similar to the definitions in weakly supervised learning.
Therefore, weak-shot learning can also be treated as weakly supervised learning
with auxiliary fully supervised categories. In this paper, we discuss the
existing weak-shot learning methodologies in different tasks and summarize the
codes at https://github.com/bcmi/Awesome-Weak-Shot-Learning.