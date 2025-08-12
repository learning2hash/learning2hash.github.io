---
layout: publication
title: Few-shot Relation Extraction With Hybrid Visual Evidence
authors: Jiaying Gong, Hoda Eldardiry
conference: LREC-COLING 2024
year: 2024
bibkey: gong2024few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.00724'}]
tags: ["COLING", "Few Shot & Zero Shot", "LREC"]
short_authors: Jiaying Gong, Hoda Eldardiry
---
The goal of few-shot relation extraction is to predict relations between name
entities in a sentence when only a few labeled instances are available for
training. Existing few-shot relation extraction methods focus on uni-modal
information such as text only. This reduces performance when there are no clear
contexts between the name entities described in text. We propose a multi-modal
few-shot relation extraction model (MFS-HVE) that leverages both textual and
visual semantic information to learn a multi-modal representation jointly. The
MFS-HVE includes semantic feature extractors and multi-modal fusion components.
The MFS-HVE semantic feature extractors are developed to extract both textual
and visual features. The visual features include global image features and
local object features within the image. The MFS-HVE multi-modal fusion unit
integrates information from various modalities using image-guided attention,
object-guided attention, and hybrid feature attention to fully capture the
semantic interaction between visual regions of images and relevant texts.
Extensive experiments conducted on two public datasets demonstrate that
semantic visual information significantly improves the performance of few-shot
relation prediction.