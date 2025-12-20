---
layout: publication
title: Towards Zero-shot Camera Trap Image Categorization
authors: "Ji\u0159\xED Vysko\u010Dil, Lukas Picek"
conference: Arxiv
year: 2024
bibkey: "vysko\u010Dil2024towards"
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.12769'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: "Ji\u0159\xED Vysko\u010Dil, Lukas Picek"
---
This paper describes the search for an alternative approach to the automatic
categorization of camera trap images. First, we benchmark state-of-the-art
classifiers using a single model for all images. Next, we evaluate methods
combining MegaDetector with one or more classifiers and Segment Anything to
assess their impact on reducing location-specific overfitting. Last, we propose
and test two approaches using large language and foundational models, such as
DINOv2, BioCLIP, BLIP, and ChatGPT, in a zero-shot scenario. Evaluation carried
out on two publicly available datasets (WCT from New Zealand, CCT20 from the
Southwestern US) and a private dataset (CEF from Central Europe) revealed that
combining MegaDetector with two separate classifiers achieves the highest
accuracy. This approach reduced the relative error of a single BEiTV2
classifier by approximately 42% on CCT20, 48% on CEF, and 75% on WCT.
Besides, as the background is removed, the error in terms of accuracy in new
locations is reduced to half. The proposed zero-shot pipeline based on DINOv2
and FAISS achieved competitive results (1.0% and 4.7% smaller on CCT20, and
CEF, respectively), which highlights the potential of zero-shot approaches for
camera trap image categorization.