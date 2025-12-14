---
layout: publication
title: 'SLAN: Self-locator Aided Network For Cross-modal Understanding'
authors: Jiang-Tian Zhai, Qi Zhang, Tong Wu, Xing-Yu Chen, Jiang-Jiang Liu, Bo Ren,
  Ming-Ming Cheng
conference: Arxiv
year: 2022
bibkey: zhai2022slan
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.16208'}]
tags: [Image Retrieval, Few-shot & Zero-shot, Multimodal Retrieval]
short_authors: Zhai et al.
---
Learning fine-grained interplay between vision and language allows to a more
accurate understanding for VisionLanguage tasks. However, it remains
challenging to extract key image regions according to the texts for semantic
alignments. Most existing works are either limited by textagnostic and
redundant regions obtained with the frozen detectors, or failing to scale
further due to its heavy reliance on scarce grounding (gold) data to pre-train
detectors. To solve these problems, we propose Self-Locator Aided Network
(SLAN) for cross-modal understanding tasks without any extra gold data. SLAN
consists of a region filter and a region adaptor to localize regions of
interest conditioned on different texts. By aggregating cross-modal
information, the region filter selects key regions and the region adaptor
updates their coordinates with text guidance. With detailed region-word
alignments, SLAN can be easily generalized to many downstream tasks. It
achieves fairly competitive results on five cross-modal understanding tasks
(e.g., 85.7% and 69.2% on COCO image-to-text and text-to-image retrieval,
surpassing previous SOTA methods). SLAN also demonstrates strong zero-shot and
fine-tuned transferability to two localization tasks.