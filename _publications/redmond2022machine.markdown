---
layout: publication
title: Machine Learning With DBOS
authors: "Robert Redmond, Nathan W. Weckwerth, Brian S. Xia, Qian Li, Peter Kraft,\
  \ Deeptaanshu Kumar, \xC7a\u011Fatay Demiralp, Michael Stonebraker"
conference: Arxiv
year: 2022
bibkey: redmond2022machine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.05101'}]
tags: []
short_authors: Redmond et al.
---
We recently proposed a new cluster operating system stack, DBOS, centered on
a DBMS. DBOS enables unique support for ML applications by encapsulating ML
code within stored procedures, centralizing ancillary ML data, providing
security built into the underlying DBMS, co-locating ML code and data, and
tracking data and workflow provenance. Here we demonstrate a subset of these
benefits around two ML applications. We first show that image classification
and object detection models using GPUs can be served as DBOS stored procedures
with performance competitive to existing systems. We then present a 1D CNN
trained to detect anomalies in HTTP requests on DBOS-backed web services,
achieving SOTA results. We use this model to develop an interactive anomaly
detection system and evaluate it through qualitative user feedback,
demonstrating its usefulness as a proof of concept for future work to develop
learned real-time security services on top of DBOS.