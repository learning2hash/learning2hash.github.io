---
layout: publication
title: How To Extract Fashion Trends From Social Media? A Robust Object Detector With
  Support For Unsupervised Learning
authors: Vijay Gabale, Anand Prabhu Subramanian
conference: Arxiv
year: 2018
bibkey: gabale2018how
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.10787'}]
tags: []
short_authors: Vijay Gabale, Anand Prabhu Subramanian
---
With the proliferation of social media, fashion inspired from celebrities,
reputed designers as well as fashion influencers has shortened the cycle of
fashion design and manufacturing. However, with the explosion of fashion
related content and large number of user generated fashion photos, it is an
arduous task for fashion designers to wade through social media photos and
create a digest of trending fashion. This necessitates deep parsing of fashion
photos on social media to localize and classify multiple fashion items from a
given fashion photo. While object detection competitions such as MSCOCO have
thousands of samples for each of the object categories, it is quite difficult
to get large labeled datasets for fast fashion items. Moreover,
state-of-the-art object detectors do not have any functionality to ingest large
amount of unlabeled data available on social media in order to fine tune object
detectors with labeled datasets. In this work, we show application of a generic
object detector, that can be pretrained in an unsupervised manner, on 24
categories from recently released Open Images V4 dataset. We first train the
base architecture of the object detector using unsupervisd learning on 60K
unlabeled photos from 24 categories gathered from social media, and then
subsequently fine tune it on 8.2K labeled photos from Open Images V4 dataset.
On 300 X 300 image inputs, we achieve 72.7% mAP on a test dataset of 2.4K
photos while performing 11% to 17% better as compared to the state-of-the-art
object detectors. We show that this improvement is due to our choice of
architecture that lets us do unsupervised learning and that performs
significantly better in identifying small objects.