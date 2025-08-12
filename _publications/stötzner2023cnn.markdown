---
layout: publication
title: CNN Based Cuneiform Sign Detection Learned From Annotated 3D Renderings And
  Mapped Photographs With Illumination Augmentation
authors: "Ernst St\xF6tzner, Timo Homburg, Hubert Mara"
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: "st\xF6tzner2023cnn"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.11277'}]
tags: ["Datasets", "ICCV"]
short_authors: "Ernst St\xF6tzner, Timo Homburg, Hubert Mara"
---
Motivated by the challenges of the Digital Ancient Near Eastern Studies
(DANES) community, we develop digital tools for processing cuneiform script
being a 3D script imprinted into clay tablets used for more than three
millennia and at least eight major languages. It consists of thousands of
characters that have changed over time and space. Photographs are the most
common representations usable for machine learning, while ink drawings are
prone to interpretation. Best suited 3D datasets that are becoming available.
We created and used the HeiCuBeDa and MaiCuBeDa datasets, which consist of
around 500 annotated tablets. For our novel OCR-like approach to mixed image
data, we provide an additional mapping tool for transferring annotations
between 3D renderings and photographs. Our sign localization uses a RepPoints
detector to predict the locations of characters as bounding boxes. We use image
data from GigaMesh's MSII (curvature, see https://gigamesh.eu) based rendering,
Phong-shaded 3D models, and photographs as well as illumination augmentation.
The results show that using rendered 3D images for sign detection performs
better than other work on photographs. In addition, our approach gives
reasonably good results for photographs only, while it is best used for mixed
datasets. More importantly, the Phong renderings, and especially the MSII
renderings, improve the results on photographs, which is the largest dataset on
a global scale.