---
layout: publication
title: Prototypical Region Proposal Networks For Few-shot Localization And Classification
authors: Elliott Skomski, Aaron Tuor, Andrew Avila, Lauren Phillips, Zachary New,
  Henry Kvinge, Courtney D. Corley, Nathan Hodas
conference: Arxiv
year: 2021
bibkey: skomski2021prototypical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.03496'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Skomski et al.
---
Recently proposed few-shot image classification methods have generally
focused on use cases where the objects to be classified are the central subject
of images. Despite success on benchmark vision datasets aligned with this use
case, these methods typically fail on use cases involving densely-annotated,
busy images: images common in the wild where objects of relevance are not the
central subject, instead appearing potentially occluded, small, or among other
incidental objects belonging to other classes of potential interest. To
localize relevant objects, we employ a prototype-based few-shot segmentation
model which compares the encoded features of unlabeled query images with
support class centroids to produce region proposals indicating the presence and
location of support set classes in a query image. These region proposals are
then used as additional conditioning input to few-shot image classifiers. We
develop a framework to unify the two stages (segmentation and classification)
into an end-to-end classification model -- PRoPnet -- and empirically
demonstrate that our methods improve accuracy on image datasets with natural
scenes containing multiple object classes.