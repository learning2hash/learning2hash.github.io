---
layout: publication
title: 'Zerosearch: Local Image Search From Text With Zero Shot Learning'
authors: Jatin Nainani, Abhishek Mazumdar, Viraj Sheth
conference: Arxiv
year: 2023
bibkey: nainani2023zerosearch
citations: 0
additional_links: [{name: Code, url: 'https://github.com/NainaniJatinZ/zero-search'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.00715'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Distance Metric Learning,
  Datasets]
short_authors: Jatin Nainani, Abhishek Mazumdar, Viraj Sheth
---
The problem of organizing and finding images in a user's directory has become
increasingly challenging due to the rapid growth in the number of images
captured on personal devices. This paper presents a solution that utilizes zero
shot learning to create image queries with only user provided text
descriptions. The paper's primary contribution is the development of an
algorithm that utilizes pre-trained models to extract features from images. The
algorithm uses OWL to check for the presence of bounding boxes and sorts images
based on cosine similarity scores. The algorithm's output is a list of images
sorted in descending order of similarity, helping users to locate specific
images more efficiently. The paper's experiments were conducted using a custom
dataset to simulate a user's image directory and evaluated the accuracy,
inference time, and size of the models. The results showed that the VGG model
achieved the highest accuracy, while the Resnet50 and InceptionV3 models had
the lowest inference time and size. The papers proposed algorithm provides an
effective and efficient solution for organizing and finding images in a users
local directory. The algorithm's performance and flexibility make it suitable
for various applications, including personal image organization and search
engines. Code and dataset for zero-search are available at:
https://github.com/NainaniJatinZ/zero-search