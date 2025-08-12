---
layout: publication
title: 'Knowledge Discovery In Optical Music Recognition: Enhancing Information Retrieval
  With Instance Segmentation'
authors: Elona Shatri, George Fazekas
conference: Proceedings of the 16th International Joint Conference on Knowledge Discovery,
  Knowledge Engineering and Knowledge Management
year: 2024
bibkey: shatri2024knowledge
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.15002'}]
tags: ["Datasets", "Evaluation"]
short_authors: Elona Shatri, George Fazekas
---
Optical Music Recognition (OMR) automates the transcription of musical
notation from images into machine-readable formats like MusicXML, MEI, or MIDI,
significantly reducing the costs and time of manual transcription. This study
explores knowledge discovery in OMR by applying instance segmentation using
Mask R-CNN to enhance the detection and delineation of musical symbols in sheet
music. Unlike Optical Character Recognition (OCR), OMR must handle the
intricate semantics of Common Western Music Notation (CWMN), where symbol
meanings depend on shape, position, and context. Our approach leverages
instance segmentation to manage the density and overlap of musical symbols,
facilitating more precise information retrieval from music scores. Evaluations
on the DoReMi and MUSCIMA++ datasets demonstrate substantial improvements, with
our method achieving a mean Average Precision (mAP) of up to 59.70% in dense
symbol environments, achieving comparable results to object detection.
Furthermore, using traditional computer vision techniques, we add a parallel
step for staff detection to infer the pitch for the recognised symbols. This
study emphasises the role of pixel-wise segmentation in advancing accurate
music symbol recognition, contributing to knowledge discovery in OMR. Our
findings indicate that instance segmentation provides more precise
representations of musical symbols, particularly in densely populated scores,
advancing OMR technology. We make our implementation, pre-processing scripts,
trained models, and evaluation results publicly available to support further
research and development.