---
layout: publication
title: 'Colored Kimia Path24 Dataset: Configurations And Benchmarks With Deep Embeddings'
authors: Sobhan Shafiei, Morteza Babaie, Shivam Kalra, H. R. Tizhoosh
conference: Arxiv
year: 2021
bibkey: shafiei2021colored
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.07611'}]
tags: [Image Retrieval, Evaluation, Datasets]
short_authors: Shafiei et al.
---
The Kimia Path24 dataset has been introduced as a classification and
retrieval dataset for digital pathology. Although it provides multi-class data,
the color information has been neglected in the process of extracting patches.
The staining information plays a major role in the recognition of tissue
patterns. To address this drawback, we introduce the color version of Kimia
Path24 by recreating sample patches from all 24 scans to propose Kimia Path24C.
We run extensive experiments to determine the best configuration for selected
patches. To provide preliminary results for setting a benchmark for the new
dataset, we utilize VGG16, InceptionV3 and DenseNet-121 model as feature
extractors. Then, we use these feature vectors to retrieve test patches. The
accuracy of image retrieval using DenseNet was 95.92% while the highest
accuracy using InceptionV3 and VGG16 reached 92.45% and 92%, respectively. We
also experimented with "deep barcodes" and established that with a small loss
in accuracy (e.g., 93.43% for binarized features for DenseNet instead of 95.92%
when the features themselves are used), the search operations can be
significantly accelerated.