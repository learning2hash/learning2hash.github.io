---
layout: publication
title: 'Comics Datasets Framework: Mix Of Comics Datasets For Detection Benchmarking'
authors: "Emanuele Vivoli, Irene Campaioli, Mariateresa Nardoni, Niccol\xF2 Biondi,\
  \ Marco Bertini, Dimosthenis Karatzas"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: vivoli2024comics
citations: 1
additional_links: [{name: Code, url: 'https://github.com/emanuelevivoli/cdf,'}, {
    name: Paper, url: 'https://arxiv.org/abs/2407.03540'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Vivoli et al.
---
Comics, as a medium, uniquely combine text and images in styles often
distinct from real-world visuals. For the past three decades, computational
research on comics has evolved from basic object detection to more
sophisticated tasks. However, the field faces persistent challenges such as
small datasets, inconsistent annotations, inaccessible model weights, and
results that cannot be directly compared due to varying train/test splits and
metrics. To address these issues, we aim to standardize annotations across
datasets, introduce a variety of comic styles into the datasets, and establish
benchmark results with clear, replicable settings. Our proposed Comics Datasets
Framework standardizes dataset annotations into a common format and addresses
the overrepresentation of manga by introducing Comics100, a curated collection
of 100 books from the Digital Comics Museum, annotated for detection in our
uniform format. We have benchmarked a variety of detection architectures using
the Comics Datasets Framework. All related code, model weights, and detailed
evaluation processes are available at https://github.com/emanuelevivoli/cdf,
ensuring transparency and facilitating replication. This initiative is a
significant advancement towards improving object detection in comics, laying
the groundwork for more complex computational tasks dependent on precise object
recognition.