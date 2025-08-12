---
layout: publication
title: 'Cfl-net: Image Forgery Localization Using Contrastive Learning'
authors: Fahim Faisal Niloy, Kishor Kumar Bhaumik, Simon S. Woo
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: niloy2022cfl
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.02182'}]
tags: ["Self-Supervised"]
short_authors: Fahim Faisal Niloy, Kishor Kumar Bhaumik, Simon S. Woo
---
Conventional forgery localizing methods usually rely on different forgery
footprints such as JPEG artifacts, edge inconsistency, camera noise, etc., with
cross-entropy loss to locate manipulated regions. However, these methods have
the disadvantage of over-fitting and focusing on only a few specific forgery
footprints. On the other hand, real-life manipulated images are generated via a
wide variety of forgery operations and thus, leave behind a wide variety of
forgery footprints. Therefore, we need a more general approach for image
forgery localization that can work well on a variety of forgery conditions. A
key assumption in underlying forged region localization is that there remains a
difference of feature distribution between untampered and manipulated regions
in each forged image sample, irrespective of the forgery type. In this paper,
we aim to leverage this difference of feature distribution to aid in image
forgery localization. Specifically, we use contrastive loss to learn mapping
into a feature space where the features between untampered and manipulated
regions are well-separated for each image. Also, our method has the advantage
of localizing manipulated region without requiring any prior knowledge or
assumption about the forgery type. We demonstrate that our work outperforms
several existing methods on three benchmark image manipulation datasets. Code
is available at https://github.com/niloy193/CFLNet.