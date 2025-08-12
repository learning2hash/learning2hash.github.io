---
layout: publication
title: Towards Content-based Pixel Retrieval In Revisited Oxford And Paris
authors: Guoyuan An, Woo Jae Kim, Saelyne Yang, Rong Li, Yuchi Huo, Sung-Eui Yoon
conference: Arxiv
year: 2023
bibkey: an2023towards
citations: 0
additional_links: [{name: Code, url: 'https://github.com/anguoyuan/Pixel_retrieval-Segmented_instance_retrieval\}\{this'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.05438'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: An et al.
---
This paper introduces the first two pixel retrieval benchmarks. Pixel
retrieval is segmented instance retrieval. Like semantic segmentation extends
classification to the pixel level, pixel retrieval is an extension of image
retrieval and offers information about which pixels are related to the query
object. In addition to retrieving images for the given query, it helps users
quickly identify the query object in true positive images and exclude false
positive images by denoting the correlated pixels. Our user study results show
pixel-level annotation can significantly improve the user experience.
  Compared with semantic and instance segmentation, pixel retrieval requires a
fine-grained recognition capability for variable-granularity targets. To this
end, we propose pixel retrieval benchmarks named PROxford and PRParis, which
are based on the widely used image retrieval datasets, ROxford and RParis.
Three professional annotators label 5,942 images with two rounds of
double-checking and refinement. Furthermore, we conduct extensive experiments
and analysis on the SOTA methods in image search, image matching, detection,
segmentation, and dense matching using our pixel retrieval benchmarks. Results
show that the pixel retrieval task is challenging to these approaches and
distinctive from existing problems, suggesting that further research can
advance the content-based pixel-retrieval and thus user search experience. The
datasets can be downloaded from
\href\{https://github.com/anguoyuan/Pixel_retrieval-Segmented_instance_retrieval\}\{this
link\}.