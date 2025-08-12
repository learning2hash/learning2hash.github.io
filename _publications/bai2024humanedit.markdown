---
layout: publication
title: 'Humanedit: A High-quality Human-rewarded Dataset For Instruction-based Image
  Editing'
authors: Jinbin Bai, Wei Chow, Ling Yang, Xiangtai Li, Juncheng Li, Hanwang Zhang,
  Shuicheng Yan
conference: Arxiv
year: 2024
bibkey: bai2024humanedit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.04280'}]
tags: ["Datasets", "Evaluation"]
short_authors: Bai et al.
---
We present HumanEdit, a high-quality, human-rewarded dataset specifically
designed for instruction-guided image editing, enabling precise and diverse
image manipulations through open-form language instructions. Previous
large-scale editing datasets often incorporate minimal human feedback, leading
to challenges in aligning datasets with human preferences. HumanEdit bridges
this gap by employing human annotators to construct data pairs and
administrators to provide feedback. With meticulously curation, HumanEdit
comprises 5,751 images and requires more than 2,500 hours of human effort
across four stages, ensuring both accuracy and reliability for a wide range of
image editing tasks. The dataset includes six distinct types of editing
instructions: Action, Add, Counting, Relation, Remove, and Replace,
encompassing a broad spectrum of real-world scenarios. All images in the
dataset are accompanied by masks, and for a subset of the data, we ensure that
the instructions are sufficiently detailed to support mask-free editing.
Furthermore, HumanEdit offers comprehensive diversity and high-resolution \(1024
\times 1024\) content sourced from various domains, setting a new versatile
benchmark for instructional image editing datasets. With the aim of advancing
future research and establishing evaluation benchmarks in the field of image
editing, we release HumanEdit at
https://huggingface.co/datasets/BryanW/HumanEdit.