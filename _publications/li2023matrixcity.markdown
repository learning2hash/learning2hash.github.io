---
layout: publication
title: 'Matrixcity: A Large-scale City Dataset For City-scale Neural Rendering And
  Beyond'
authors: Yixuan Li, Lihan Jiang, Linning Xu, Yuanbo Xiangli, Zhenzhi Wang, Dahua Lin,
  Bo Dai
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: li2023matrixcity
citations: 18
additional_links: [{name: Code, url: 'https://city-super.github.io/matrixcity/'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.16553'}]
tags: ["Datasets", "Evaluation", "ICCV"]
short_authors: Li et al.
---
Neural radiance fields (NeRF) and its subsequent variants have led to
remarkable progress in neural rendering. While most of recent neural rendering
works focus on objects and small-scale scenes, developing neural rendering
methods for city-scale scenes is of great potential in many real-world
applications. However, this line of research is impeded by the absence of a
comprehensive and high-quality dataset, yet collecting such a dataset over real
city-scale scenes is costly, sensitive, and technically difficult. To this end,
we build a large-scale, comprehensive, and high-quality synthetic dataset for
city-scale neural rendering researches. Leveraging the Unreal Engine 5 City
Sample project, we develop a pipeline to easily collect aerial and street city
views, accompanied by ground-truth camera poses and a range of additional data
modalities. Flexible controls over environmental factors like light, weather,
human and car crowd are also available in our pipeline, supporting the need of
various tasks covering city-scale neural rendering and beyond. The resulting
pilot dataset, MatrixCity, contains 67k aerial images and 452k street images
from two city maps of total size \(28km^2\). On top of MatrixCity, a thorough
benchmark is also conducted, which not only reveals unique challenges of the
task of city-scale neural rendering, but also highlights potential improvements
for future works. The dataset and code will be publicly available at our
project page: https://city-super.github.io/matrixcity/.