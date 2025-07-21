---
layout: publication
title: Generalized Contrastive Optimization of Siamese Networks for Place Recognition
authors: "Leyva-vallina Mar\xEDa, Strisciuglio Nicola, Petkov Nicolai"
conference: Arxiv
year: 2021
bibkey: leyvavallina2021generalized
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.06638'}]
tags: []
---
Visual place recognition is a challenging task in computer vision and a key
component of camera-based localization and navigation systems. Recently,
Convolutional Neural Networks (CNNs) achieved high results and good
generalization capabilities. They are usually trained using pairs or triplets
of images labeled as either similar or dissimilar, in a binary fashion. In
practice, the similarity between two images is not binary, but continuous.
Furthermore, training these CNNs is computationally complex and involves costly
pair and triplet mining strategies. We propose a Generalized Contrastive loss
(GCL) function that relies on image similarity as a continuous measure, and use
it to train a siamese CNN. Furthermore, we present three techniques for
automatic annotation of image pairs with labels indicating their degree of
similarity, and deploy them to re-annotate the MSLS, TB-Places, and 7Scenes
datasets. We demonstrate that siamese CNNs trained using the GCL function and
the improved annotations consistently outperform their binary counterparts. Our
models trained on MSLS outperform the state-of-the-art methods, including
NetVLAD, NetVLAD-SARE, AP-GeM and Patch-NetVLAD, and generalize well on the
Pittsburgh30k, Tokyo 24/7, RobotCar Seasons v2 and Extended CMU Seasons
datasets. Furthermore, training a siamese network using the GCL function does
not require complex pair mining. We release the source code at
https://github.com/marialeyvallina/generalized_contrastive_loss.