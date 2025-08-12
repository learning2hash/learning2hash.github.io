---
layout: publication
title: On Utilizing Relationships For Transferable Few-shot Fine-grained Object Detection
authors: "Ambar Pal, Arnau Ramisa, Amit Kumar K C, Ren\xE9 Vidal"
conference: Arxiv
year: 2022
bibkey: pal2022utilizing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.00770'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Pal et al.
---
State-of-the-art object detectors are fast and accurate, but they require a
large amount of well annotated training data to obtain good performance.
However, obtaining a large amount of training annotations specific to a
particular task, i.e., fine-grained annotations, is costly in practice. In
contrast, obtaining common-sense relationships from text, e.g., "a table-lamp
is a lamp that sits on top of a table", is much easier. Additionally,
common-sense relationships like "on-top-of" are easy to annotate in a
task-agnostic fashion. In this paper, we propose a probabilistic model that
uses such relational knowledge to transform an off-the-shelf detector of coarse
object categories (e.g., "table", "lamp") into a detector of fine-grained
categories (e.g., "table-lamp"). We demonstrate that our method, RelDetect,
achieves performance competitive to finetuning based state-of-the-art object
detector baselines when an extremely low amount of fine-grained annotations is
available (\(0.2%\) of entire dataset). We also demonstrate that RelDetect is
able to utilize the inherent transferability of relationship information to
obtain a better performance (\(+5\) mAP points) than the above baselines on an
unseen dataset (zero-shot transfer). In summary, we demonstrate the power of
using relationships for object detection on datasets where fine-grained object
categories can be linked to coarse-grained categories via suitable
relationships.