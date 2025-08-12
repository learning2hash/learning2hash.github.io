---
layout: publication
title: Personalizing Pre-trained Models
authors: Mina Khan, P Srivatsa, Advait Rane, Shriram Chenniappa, Asadali Hazariwala,
  Pattie Maes
conference: Arxiv
year: 2021
bibkey: khan2021personalizing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.01499'}]
tags: []
short_authors: Khan et al.
---
Self-supervised or weakly supervised models trained on large-scale datasets
have shown sample-efficient transfer to diverse datasets in few-shot settings.
We consider how upstream pretrained models can be leveraged for downstream
few-shot, multilabel, and continual learning tasks. Our model CLIPPER (CLIP
PERsonalized) uses image representations from CLIP, a large-scale image
representation learning model trained using weak natural language supervision.
We developed a technique, called Multi-label Weight Imprinting (MWI), for
multi-label, continual, and few-shot learning, and CLIPPER uses MWI with image
representations from CLIP. We evaluated CLIPPER on 10 single-label and 5
multi-label datasets. Our model shows robust and competitive performance, and
we set new benchmarks for few-shot, multi-label, and continual learning. Our
lightweight technique is also compute-efficient and enables privacy-preserving
applications as the data is not sent to the upstream model for fine-tuning.