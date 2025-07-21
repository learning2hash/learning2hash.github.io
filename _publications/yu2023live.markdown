---
layout: publication
title: Live Laparoscopic Video Retrieval with Compressed Uncertainty
authors: Yu et al.
conference: Medical Image Analysis
year: 2023
bibkey: yu2023live
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.04301'}]
tags: ["Video-Retrieval"]
---
Searching through large volumes of medical data to retrieve relevant
information is a challenging yet crucial task for clinical care. However the
primitive and most common approach to retrieval, involving text in the form of
keywords, is severely limited when dealing with complex media formats.
Content-based retrieval offers a way to overcome this limitation, by using rich
media as the query itself. Surgical video-to-video retrieval in particular is a
new and largely unexplored research problem with high clinical value,
especially in the real-time case: using real-time video hashing, search can be
achieved directly inside of the operating room. Indeed, the process of hashing
converts large data entries into compact binary arrays or hashes, enabling
large-scale search operations at a very fast rate. However, due to fluctuations
over the course of a video, not all bits in a given hash are equally reliable.
In this work, we propose a method capable of mitigating this uncertainty while
maintaining a light computational footprint. We present superior retrieval
results (3-4 % top 10 mean average precision) on a multi-task evaluation
protocol for surgery, using cholecystectomy phases, bypass phases, and coming
from an entirely new dataset introduced here, critical events across six
different surgery types. Success on this multi-task benchmark shows the
generalizability of our approach for surgical video retrieval.