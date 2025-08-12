---
layout: publication
title: 'Many-shot From Low-shot: Learning To Annotate Using Mixed Supervision For
  Object Detection'
authors: Carlo Biffi, Steven McDonagh, Philip Torr, Ales Leonardis, Sarah Parisot
conference: Lecture Notes in Computer Science
year: 2020
bibkey: biffi2020many
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.09694'}]
tags: ["Few Shot & Zero Shot", "Supervised"]
short_authors: Biffi et al.
---
Object detection has witnessed significant progress by relying on large,
manually annotated datasets. Annotating such datasets is highly time consuming
and expensive, which motivates the development of weakly supervised and
few-shot object detection methods. However, these methods largely underperform
with respect to their strongly supervised counterpart, as weak training signals
*often* result in partial or oversized detections. Towards solving this
problem we introduce, for the first time, an online annotation module (OAM)
that learns to generate a many-shot set of *reliable* annotations from a
larger volume of weakly labelled images. Our OAM can be jointly trained with
any fully supervised two-stage object detection method, providing additional
training annotations on the fly. This results in a fully end-to-end strategy
that only requires a low-shot set of fully annotated images. The integration of
the OAM with Fast(er) R-CNN improves their performance by \(17%\) mAP, \(9%\)
AP50 on PASCAL VOC 2007 and MS-COCO benchmarks, and significantly outperforms
competing methods using mixed supervision.