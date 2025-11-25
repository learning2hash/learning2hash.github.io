---
layout: publication
title: 'Poshaknet: Framework For Matching Dresses From Real-life Photos Using GAN
  And Siamese Network'
authors: Abhigyan Khaund, Daksh Thapar, Aditya Nigam
conference: Arxiv
year: 2019
bibkey: khaund2019poshaknet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.04237'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Abhigyan Khaund, Daksh Thapar, Aditya Nigam
---
Online garment shopping has gained many customers in recent years. Describing
a dress using keywords does not always yield the proper results, which in turn
leads to dissatisfaction of customers. A visual search based system will be
enormously beneficent to the industry. Hence, we propose a framework that can
retrieve similar clothes that can be found in an image. The first task is to
extract the garment from the input image (street photo). There are various
challenges for that, including pose, illumination, and background clutter. We
use a Generative Adversarial Network for the task of retrieving the garment
that the person in the image was wearing. It has been shown that GAN can
retrieve the garment very efficiently despite the challenges of street photos.
Finally, a siamese based matching system takes the retrieved cloth image and
matches it with the clothes in the dataset, giving us the top k matches. We
take a pre-trained inception-ResNet v1 module as a siamese network (trained
using triplet loss for face detection) and fine-tune it on the shopping dataset
using center loss. The dataset has been collected inhouse. For training the
GAN, we use the LookBook dataset, which is publically available.