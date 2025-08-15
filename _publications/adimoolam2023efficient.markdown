---
layout: publication
title: Efficient Deduplication And Leakage Detection In Large Scale Image Datasets
  With A Focus On The Crowdai Mapping Challenge Dataset
authors: Yeshwanth Kumar Adimoolam, Bodhiswatta Chatterjee, Charalambos Poullis, Melinos
  Averkiou
conference: Arxiv
year: 2023
bibkey: adimoolam2023efficient
citations: 1
additional_links: [{name: Code, url: 'https://github.com/yeshwanth95/CrowdAI_Hash_and_search'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.02296'}]
tags: ["Datasets", "Hashing Methods"]
short_authors: Adimoolam et al.
---
Recent advancements in deep learning and computer vision have led to
widespread use of deep neural networks to extract building footprints from
remote-sensing imagery. The success of such methods relies on the availability
of large databases of high-resolution remote sensing images with high-quality
annotations. The CrowdAI Mapping Challenge Dataset is one of these datasets
that has been used extensively in recent years to train deep neural networks.
This dataset consists of \( \sim\ \)280k training images and \( \sim\ \)60k testing
images, with polygonal building annotations for all images. However, issues
such as low-quality and incorrect annotations, extensive duplication of image
samples, and data leakage significantly reduce the utility of deep neural
networks trained on the dataset. Therefore, it is an imperative pre-condition
to adopt a data validation pipeline that evaluates the quality of the dataset
prior to its use. To this end, we propose a drop-in pipeline that employs
perceptual hashing techniques for efficient de-duplication of the dataset and
identification of instances of data leakage between training and testing
splits. In our experiments, we demonstrate that nearly 250k(\( \sim\ \)90%)
images in the training split were identical. Moreover, our analysis on the
validation split demonstrates that roughly 56k of the 60k images also appear in
the training split, resulting in a data leakage of 93%. The source code used
for the analysis and de-duplication of the CrowdAI Mapping Challenge dataset is
publicly available at https://github.com/yeshwanth95/CrowdAI_Hash_and_search .