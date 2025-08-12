---
layout: publication
title: 'Epillid Dataset: A Low-shot Fine-grained Benchmark For Pill Identification'
authors: Naoto Usuyama, Natalia Larios Delgado, Amanda K. Hall, Jessica Lundin
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: usuyama2020epillid
citations: 8
additional_links: [{name: Code, url: 'https://github.com/usuyama/ePillID-benchmark'},
  {name: Paper, url: 'https://arxiv.org/abs/2005.14288'}]
tags: ["CVPR", "Datasets"]
short_authors: Usuyama et al.
---
Identifying prescription medications is a frequent task for patients and
medical professionals; however, this is an error-prone task as many pills have
similar appearances (e.g. white round pills), which increases the risk of
medication errors. In this paper, we introduce ePillID, the largest public
benchmark on pill image recognition, composed of 13k images representing 9804
appearance classes (two sides for 4902 pill types). For most of the appearance
classes, there exists only one reference image, making it a challenging
low-shot recognition setting. We present our experimental setup and evaluation
results of various baseline models on the benchmark. The best baseline using a
multi-head metric-learning approach with bilinear features performed remarkably
well; however, our error analysis suggests that they still fail to distinguish
particularly confusing classes. The code and data are available at
https://github.com/usuyama/ePillID-benchmark.