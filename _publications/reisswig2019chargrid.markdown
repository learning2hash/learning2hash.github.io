---
layout: publication
title: 'Chargrid-ocr: End-to-end Trainable Optical Character Recognition For Printed
  Documents Using Instance Segmentation'
authors: "Christian Reisswig, Anoop R Katti, Marco Spinaci, Johannes H\xF6hne"
conference: Arxiv
year: 2019
bibkey: reisswig2019chargrid
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.04469'}]
tags: ["Datasets"]
short_authors: Reisswig et al.
---
We present an end-to-end trainable approach for Optical Character Recognition
(OCR) on printed documents. Specifically, we propose a model that predicts a) a
two-dimensional character grid (*chargrid*) representation of a document
image as a semantic segmentation task and b) character boxes for delineating
character instances as an object detection task. For training the model, we
build two large-scale datasets without resorting to any manual annotation -
synthetic documents with clean labels and real documents with noisy labels. We
demonstrate experimentally that our method, trained on the combination of these
datasets, (i) outperforms previous state-of-the-art approaches in accuracy (ii)
is easily parallelizable on GPU and is, therefore, significantly faster and
(iii) is easy to train and adapt to a new domain.