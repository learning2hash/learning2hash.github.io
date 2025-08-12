---
layout: publication
title: Enriching Imagenet With Human Similarity Judgments And Psychological Embeddings
authors: Brett D. Roads, Bradley C. Love
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: roads2020enriching
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.11015'}]
tags: ["CVPR", "Datasets"]
short_authors: Brett D. Roads, Bradley C. Love
---
Advances in object recognition flourished in part because of the availability
of high-quality datasets and associated benchmarks. However, these
benchmarks---such as ILSVRC---are relatively task-specific, focusing
predominately on predicting class labels. We introduce a publicly-available
dataset that embodies the task-general capabilities of human perception and
reasoning. The Human Similarity Judgments extension to ImageNet (ImageNet-HSJ)
is composed of human similarity judgments that supplement the ILSVRC validation
set. The new dataset supports a range of task and performance metrics,
including the evaluation of unsupervised learning algorithms. We demonstrate
two methods of assessment: using the similarity judgments directly and using a
psychological embedding trained on the similarity judgments. This embedding
space contains an order of magnitude more points (i.e., images) than previous
efforts based on human judgments. Scaling to the full 50,000 image set was made
possible through a selective sampling process that used variational Bayesian
inference and model ensembles to sample aspects of the embedding space that
were most uncertain. This methodological innovation not only enables scaling,
but should also improve the quality of solutions by focusing sampling where it
is needed. To demonstrate the utility of ImageNet-HSJ, we used the similarity
ratings and the embedding space to evaluate how well several popular models
conform to human similarity judgments. One finding is that more complex models
that perform better on task-specific benchmarks do not better conform to human
semantic judgments. In addition to the human similarity judgments, pre-trained
psychological embeddings and code for inferring variational embeddings are made
publicly available. Collectively, ImageNet-HSJ assets support the appraisal of
internal representations and the development of more human-like models.