---
layout: publication
title: Avscan2vec Feature Learning On Antivirus Scan Data For Production-scale Malware Corpora
authors: Joyce Robert J., Patel Tirth, Nicholas Charles, Raff Edward
conference: "Arxiv"
year: 2023
bibkey: joyce2023feature
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.06228"}
tags: ['ARXIV', 'Supervised']
---
When investigating a malicious file, searching for related files is a common
task that malware analysts must perform. Given that production malware corpora
may contain over a billion files and consume petabytes of storage, many feature
extraction and similarity search approaches are computationally infeasible. Our
work explores the potential of antivirus (AV) scan data as a scalable source of
features for malware. This is possible because AV scan reports are widely
available through services such as VirusTotal and are ~100x smaller than the
average malware sample. The information within an AV scan report is abundant
with information and can indicate a malicious file's family, behavior, target
operating system, and many other characteristics. We introduce AVScan2Vec, a
language model trained to comprehend the semantics of AV scan data. AVScan2Vec
ingests AV scan data for a malicious file and outputs a meaningful vector
representation. AVScan2Vec vectors are ~3 to 85x smaller than popular
alternatives in use today, enabling faster vector comparisons and lower memory
usage. By incorporating Dynamic Continuous Indexing, we show that
nearest-neighbor queries on AVScan2Vec vectors can scale to even the largest
malware production datasets. We also demonstrate that AVScan2Vec vectors are
superior to other leading malware feature vector representations across nearly
all classification, clustering, and nearest-neighbor lookup algorithms that we
evaluated.
