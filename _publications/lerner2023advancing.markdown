---
layout: publication
title: Advancing Image Retrieval With Few-shot Learning And Relevance Feedback
authors: Boaz Lerner, Nir Darshan, Rami Ben-Ari
conference: Arxiv
year: 2023
bibkey: lerner2023advancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.11078'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Boaz Lerner, Nir Darshan, Rami Ben-Ari
---
With such a massive growth in the number of images stored, efficient search
in a database has become a crucial endeavor managed by image retrieval systems.
Image Retrieval with Relevance Feedback (IRRF) involves iterative human
interaction during the retrieval process, yielding more meaningful outcomes.
This process can be generally cast as a binary classification problem with only
\{\it few\} labeled samples derived from user feedback. The IRRF task frames a
unique few-shot learning characteristics including binary classification of
imbalanced and asymmetric classes, all in an open-set regime. In this paper, we
study this task through the lens of few-shot learning methods. We propose a new
scheme based on a hyper-network, that is tailored to the task and facilitates
swift adjustment to user feedback. Our approach's efficacy is validated through
comprehensive evaluations on multiple benchmarks and two supplementary tasks,
supported by theoretical analysis. We demonstrate the advantage of our model
over strong baselines on 4 different datasets in IRRF, addressing also
retrieval of images with multiple objects. Furthermore, we show that our method
can attain SoTA results in few-shot one-class classification and reach
comparable results in binary classification task of few-shot open-set
recognition.