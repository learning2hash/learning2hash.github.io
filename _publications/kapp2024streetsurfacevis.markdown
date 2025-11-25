---
layout: publication
title: 'Streetsurfacevis: A Dataset Of Crowdsourced Street-level Imagery Annotated
  By Road Surface Type And Quality'
authors: "Alexandra Kapp, Edith Hoffmann, Esther Weigmann, Helena Mihaljevi\u0107"
conference: Scientific Data 12 (2025) 92
year: 2024
bibkey: kapp2024streetsurfacevis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.21454'}]
tags: ["Datasets", "Similarity Search"]
short_authors: Kapp et al.
---
Road unevenness significantly impacts the safety and comfort of traffic
participants, especially vulnerable groups such as cyclists and wheelchair
users. To train models for comprehensive road surface assessments, we introduce
StreetSurfaceVis, a novel dataset comprising 9,122 street-level images mostly
from Germany collected from a crowdsourcing platform and manually annotated by
road surface type and quality. By crafting a heterogeneous dataset, we aim to
enable robust models that maintain high accuracy across diverse image sources.
As the frequency distribution of road surface types and qualities is highly
imbalanced, we propose a sampling strategy incorporating various external label
prediction resources to ensure sufficient images per class while reducing
manual annotation. More precisely, we estimate the impact of (1) enriching the
image data with OpenStreetMap tags, (2) iterative training and application of a
custom surface type classification model, (3) amplifying underrepresented
classes through prompt-based classification with GPT-4o and (4) similarity
search using image embeddings. Combining these strategies effectively reduces
manual annotation workload while ensuring sufficient class representation.