---
layout: publication
title: 'Seq-sg2sl: Inferring Semantic Layout From Scene Graph Through Sequence To
  Sequence Learning'
authors: Boren Li, Boyu Zhuang, Mingyang Li, Jian Gu
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: li2019seq
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.06592'}]
tags: ["ICCV"]
short_authors: Li et al.
---
Generating semantic layout from scene graph is a crucial intermediate task
connecting text to image. We present a conceptually simple, flexible and
general framework using sequence to sequence (seq-to-seq) learning for this
task. The framework, called Seq-SG2SL, derives sequence proxies for the two
modality and a Transformer-based seq-to-seq model learns to transduce one into
the other. A scene graph is decomposed into a sequence of semantic fragments
(SF), one for each relationship. A semantic layout is represented as the
consequence from a series of brick-action code segments (BACS), dictating the
position and scale of each object bounding box in the layout. Viewing the two
building blocks, SF and BACS, as corresponding terms in two different
vocabularies, a seq-to-seq model is fittingly used to translate. A new metric,
semantic layout evaluation understudy (SLEU), is devised to evaluate the task
of semantic layout prediction inspired by BLEU. SLEU defines relationships
within a layout as unigrams and looks at the spatial distribution for n-grams.
Unlike the binary precision of BLEU, SLEU allows for some tolerances spatially
through thresholding the Jaccard Index and is consequently more adapted to the
task. Experimental results on the challenging Visual Genome dataset show
improvement over a non-sequential approach based on graph convolution.