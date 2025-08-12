---
layout: publication
title: Text To Artistic Image Generation
authors: Qinghe Tian, Jean-Claude Franchitti
conference: Arxiv
year: 2022
bibkey: tian2022text
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.02439'}]
tags: []
short_authors: Qinghe Tian, Jean-Claude Franchitti
---
Painting is one of the ways for people to express their ideas, but what if
people with disabilities in hands want to paint? To tackle this challenge, we
create an end-to-end solution that can generate artistic images from text
descriptions. However, due to the lack of datasets with paired text description
and artistic images, it is hard to directly train an algorithm which can create
art based on text input. To address this issue, we split our task into three
steps: (1) Generate a realistic image from a text description by using Dynamic
Memory Generative Adversarial Network (arXiv:1904.01310), (2) Classify the
image as a genre that exists in the WikiArt dataset using Resnet (arXiv:
1512.03385), (3) Select a style that is compatible with the genre and transfer
it to the generated image by using neural artistic stylization network
(arXiv:1705.06830).