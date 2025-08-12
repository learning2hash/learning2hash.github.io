---
layout: publication
title: Visual Aware Hierarchy Based Food Recognition
authors: Runyu Mao, Jiangpeng He, Zeman Shao, Sri Kalyan Yarlagadda, Fengqing Zhu
conference: Lecture Notes in Computer Science
year: 2021
bibkey: mao2020visual
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.03368'}]
tags: []
short_authors: Mao et al.
---
Food recognition is one of the most important components in image-based
dietary assessment. However, due to the different complexity level of food
images and inter-class similarity of food categories, it is challenging for an
image-based food recognition system to achieve high accuracy for a variety of
publicly available datasets. In this work, we propose a new two-step food
recognition system that includes food localization and hierarchical food
classification using Convolutional Neural Networks (CNNs) as the backbone
architecture. The food localization step is based on an implementation of the
Faster R-CNN method to identify food regions. In the food classification step,
visually similar food categories can be clustered together automatically to
generate a hierarchical structure that represents the semantic visual relations
among food categories, then a multi-task CNN model is proposed to perform the
classification task based on the visual aware hierarchical structure. Since the
size and quality of dataset is a key component of data driven methods, we
introduce a new food image dataset, VIPER-FoodNet (VFN) dataset, consists of 82
food categories with 15k images based on the most commonly consumed foods in
the United States. A semi-automatic crowdsourcing tool is used to provide the
ground-truth information for this dataset including food object bounding boxes
and food object labels. Experimental results demonstrate that our system can
significantly improve both classification and recognition performance on 4
publicly available datasets and the new VFN dataset.