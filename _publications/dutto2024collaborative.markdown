---
layout: publication
title: Collaborative Visual Place Recognition Through Federated Learning
authors: "Mattia Dutto, Gabriele Berton, Debora Caldarola, Eros Fan\xEC, Gabriele\
  \ Trivigno, Carlo Masone"
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2024
bibkey: dutto2024collaborative
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.13324'}]
tags: [Self-Supervised, CVPR, Image Retrieval, Tools & Libraries]
short_authors: Dutto et al.
---
Visual Place Recognition (VPR) aims to estimate the location of an image by
treating it as a retrieval problem. VPR uses a database of geo-tagged images
and leverages deep neural networks to extract a global representation, called
descriptor, from each image. While the training data for VPR models often
originates from diverse, geographically scattered sources (geo-tagged images),
the training process itself is typically assumed to be centralized. This
research revisits the task of VPR through the lens of Federated Learning (FL),
addressing several key challenges associated with this adaptation. VPR data
inherently lacks well-defined classes, and models are typically trained using
contrastive learning, which necessitates a data mining step on a centralized
database. Additionally, client devices in federated systems can be highly
heterogeneous in terms of their processing capabilities. The proposed FedVPR
framework not only presents a novel approach for VPR but also introduces a new,
challenging, and realistic task for FL research, paving the way to other image
retrieval tasks in FL.