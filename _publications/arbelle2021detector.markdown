---
layout: publication
title: Detector-free Weakly Supervised Grounding By Separation
authors: Assaf Arbelle, Sivan Doveh, Amit Alfassy, Joseph Shtok, Guy Lev, Eli Schwartz,
  Hilde Kuehne, Hila Barak Levi, Prasanna Sattigeri, Rameswar Panda, Chun-Fu Chen,
  Alex Bronstein, Kate Saenko, Shimon Ullman, Raja Giryes, Rogerio Feris, Leonid Karlinsky
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: arbelle2021detector
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.09829'}]
tags: ["ICCV"]
short_authors: Arbelle et al.
---
Nowadays, there is an abundance of data involving images and surrounding
free-form text weakly corresponding to those images. Weakly Supervised
phrase-Grounding (WSG) deals with the task of using this data to learn to
localize (or to ground) arbitrary text phrases in images without any additional
annotations. However, most recent SotA methods for WSG assume the existence of
a pre-trained object detector, relying on it to produce the ROIs for
localization. In this work, we focus on the task of Detector-Free WSG (DF-WSG)
to solve WSG without relying on a pre-trained detector. We directly learn
everything from the images and associated free-form text pairs, thus
potentially gaining an advantage on the categories unsupported by the detector.
The key idea behind our proposed Grounding by Separation (GbS) method is
synthesizing `text to image-regions' associations by random alpha-blending of
arbitrary image pairs and using the corresponding texts of the pair as
conditions to recover the alpha map from the blended image via a segmentation
network. At test time, this allows using the query phrase as a condition for a
non-blended query image, thus interpreting the test image as a composition of a
region corresponding to the phrase and the complement region. Using this
approach we demonstrate a significant accuracy improvement, of up to \(8.5%\)
over previous DF-WSG SotA, for a range of benchmarks including Flickr30K,
Visual Genome, and ReferIt, as well as a significant complementary improvement
(above \(7%\)) over the detector-based approaches for WSG.