---
layout: publication
title: 'Doremi: First Glance At A Universal OMR Dataset'
authors: "Elona Shatri, Gy\xF6rgy Fazekas"
conference: Arxiv
year: 2021
bibkey: shatri2021doremi
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.07786'}]
tags: ["Datasets"]
short_authors: "Elona Shatri, Gy\xF6rgy Fazekas"
---
The main challenges of Optical Music Recognition (OMR) come from the nature
of written music, its complexity and the difficulty of finding an appropriate
data representation. This paper provides a first look at DoReMi, an OMR dataset
that addresses these challenges, and a baseline object detection model to
assess its utility. Researchers often approach OMR following a set of small
stages, given that existing data often do not satisfy broader research. We
examine the possibility of changing this tendency by presenting more metadata.
Our approach complements existing research; hence DoReMi allows harmonisation
with two existing datasets, DeepScores and MUSCIMA++. DoReMi was generated
using a music notation software and includes over 6400 printed sheet music
images with accompanying metadata useful in OMR research. Our dataset provides
OMR metadata, MIDI, MEI, MusicXML and PNG files, each aiding a different stage
of OMR. We obtain 64% mean average precision (mAP) in object detection using
half of the data. Further work includes re-iterating through the creation
process to satisfy custom OMR models. While we do not assume to have solved the
main challenges in OMR, this dataset opens a new course of discussions that
would ultimately aid that goal.