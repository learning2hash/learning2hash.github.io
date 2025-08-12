---
layout: publication
title: 'The Artbench Dataset: Benchmarking Generative Models With Artworks'
authors: Peiyuan Liao, Xiuyu Li, Xihui Liu, Kurt Keutzer
conference: Arxiv
year: 2022
bibkey: liao2022artbench
citations: 9
additional_links: [{name: Code, url: 'https://github.com/liaopeiyuan/artbench'}, {
    name: Paper, url: 'https://arxiv.org/abs/2206.11404'}]
tags: ["Datasets"]
short_authors: Liao et al.
---
We introduce ArtBench-10, the first class-balanced, high-quality, cleanly
annotated, and standardized dataset for benchmarking artwork generation. It
comprises 60,000 images of artwork from 10 distinctive artistic styles, with
5,000 training images and 1,000 testing images per style. ArtBench-10 has
several advantages over previous artwork datasets. Firstly, it is
class-balanced while most previous artwork datasets suffer from the long tail
class distributions. Secondly, the images are of high quality with clean
annotations. Thirdly, ArtBench-10 is created with standardized data collection,
annotation, filtering, and preprocessing procedures. We provide three versions
of the dataset with different resolutions (\(32\times32\), \(256\times256\), and
original image size), formatted in a way that is easy to be incorporated by
popular machine learning frameworks. We also conduct extensive benchmarking
experiments using representative image synthesis models with ArtBench-10 and
present in-depth analysis. The dataset is available at
https://github.com/liaopeiyuan/artbench under a Fair Use license.