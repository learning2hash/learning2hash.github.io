---
layout: publication
title: 'CHIP: Contrastive Hierarchical Image Pretraining'
authors: Arpit Mittal, Harshil Jhaveri, Swapnil Mallick, Abhishek Ajmera
conference: Arxiv
year: 2023
bibkey: mittal2023chip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.08304'}]
tags: []
short_authors: Mittal et al.
---
Few-shot object classification is the task of classifying objects in an image
with limited number of examples as supervision. We propose a one-shot/few-shot
classification model that can classify an object of any unseen class into a
relatively general category in an hierarchically based classification. Our
model uses a three-level hierarchical contrastive loss based ResNet152
classifier for classifying an object based on its features extracted from Image
embedding, not used during the training phase. For our experimentation, we have
used a subset of the ImageNet (ILSVRC-12) dataset that contains only the animal
classes for training our model and created our own dataset of unseen classes
for evaluating our trained model. Our model provides satisfactory results in
classifying the unknown objects into a generic category which has been later
discussed in greater detail.