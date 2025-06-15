---
layout: publication
title: 'Patch2cad: Patchwise Embedding Learning For In-the-wild Shape Retrieval From A Single Image'
authors: Weicheng Kuo, Anelia Angelova, Tsung-yi Lin, Angela Dai
conference: "Arxiv"
year: 2021
citations: 17
bibkey: kuo2021patchwise
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2108.09368'}
tags: ['Evaluation Metrics', 'ANN Search']
---
3D perception of object shapes from RGB image input is fundamental towards
semantic scene understanding, grounding image-based perception in our spatially
3-dimensional real-world environments. To achieve a mapping between image views
of objects and 3D shapes, we leverage CAD model priors from existing
large-scale databases, and propose a novel approach towards constructing a
joint embedding space between 2D images and 3D CAD models in a patch-wise
fashion -- establishing correspondences between patches of an image view of an
object and patches of CAD geometry. This enables part similarity reasoning for
retrieving similar CADs to a new image view without exact matches in the
database. Our patch embedding provides more robust CAD retrieval for shape
estimation in our end-to-end estimation of CAD model shape and pose for
detected objects in a single input image. Experiments on in-the-wild, complex
imagery from ScanNet show that our approach is more robust than state of the
art in real-world scenarios without any exact CAD matches.
