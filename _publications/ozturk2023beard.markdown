---
layout: publication
title: Beard Segmentation And Recognition Bias
authors: Kagan Ozturk, Grace Bezold, Aman Bhatta, Haiyu Wu, Kevin Bowyer
conference: Arxiv
year: 2023
bibkey: ozturk2023beard
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15740'}]
tags: ["Evaluation"]
short_authors: Ozturk et al.
---
A person's facial hairstyle, such as presence and size of beard, can
significantly impact face recognition accuracy. There are publicly-available
deep networks that achieve reasonable accuracy at binary attribute
classification, such as beard / no beard, but few if any that segment the
facial hair region. To investigate the effect of facial hair in a rigorous
manner, we first created a set of fine-grained facial hair annotations to train
a segmentation model and evaluate its accuracy across African-American and
Caucasian face images. We then use our facial hair segmentations to categorize
image pairs according to the degree of difference or similarity in the facial
hairstyle. We find that the False Match Rate (FMR) for image pairs with
different categories of facial hairstyle varies by a factor of over 10 for
African-American males and over 25 for Caucasian males. To reduce the bias
across image pairs with different facial hairstyles, we propose a scheme for
adaptive thresholding based on facial hairstyle similarity. Evaluation on a
subject-disjoint set of images shows that adaptive similarity thresholding
based on facial hairstyles of the image pair reduces the ratio between the
highest and lowest FMR across facial hairstyle categories for African-American
from 10.7 to 1.8 and for Caucasians from 25.9 to 1.3. Facial hair annotations
and facial hair segmentation model will be publicly available.