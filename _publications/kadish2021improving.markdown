---
layout: publication
title: Improving Object Detection In Art Images Using Only Style Transfer
authors: "David Kadish, Sebastian Risi, Anders Sundnes L\xF8vlie"
conference: 2021 International Joint Conference on Neural Networks (IJCNN)
year: 2021
bibkey: kadish2021improving
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.06529'}]
tags: []
short_authors: "David Kadish, Sebastian Risi, Anders Sundnes L\xF8vlie"
---
Despite recent advances in object detection using deep learning neural
networks, these neural networks still struggle to identify objects in art
images such as paintings and drawings. This challenge is known as the cross
depiction problem and it stems in part from the tendency of neural networks to
prioritize identification of an object's texture over its shape. In this paper
we propose and evaluate a process for training neural networks to localize
objects - specifically people - in art images. We generate a large dataset for
training and validation by modifying the images in the COCO dataset using AdaIn
style transfer. This dataset is used to fine-tune a Faster R-CNN object
detection network, which is then tested on the existing People-Art testing
dataset. The result is a significant improvement on the state of the art and a
new way forward for creating datasets to train neural networks to process art
images.