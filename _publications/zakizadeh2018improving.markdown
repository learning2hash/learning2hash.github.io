---
layout: publication
title: Improving The Annotation Of Deepfashion Images For Fine-grained Attribute Recognition
authors: Roshanak Zakizadeh, Michele Sasdelli, Yu Qian, Eduard Vazquez
conference: Arxiv
year: 2018
bibkey: zakizadeh2018improving
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.11674'}]
tags: ["Datasets"]
short_authors: Zakizadeh et al.
---
DeepFashion is a widely used clothing dataset with 50 categories and more
than overall 200k images where each image is annotated with fine-grained
attributes. This dataset is often used for clothes recognition and although it
provides comprehensive annotations, the attributes distribution is unbalanced
and repetitive specially for training fine-grained attribute recognition
models. In this work, we tailored DeepFashion for fine-grained attribute
recognition task by focusing on each category separately. After selecting
categories with sufficient number of images for training, we remove very scarce
attributes and merge the duplicate ones in each category, then we clean the
dataset based on the new list of attributes. We use a bilinear convolutional
neural network with pairwise ranking loss function for multi-label fine-grained
attribute recognition and show that the new annotations improve the results for
such a task. The detailed annotations for each of the selected categories are
provided for public use.