---
layout: publication
title: 'MOTIF: A Large Malware Reference Dataset With Ground Truth Family Labels'
authors: Robert J. Joyce, Dev Amlani, Charles Nicholas, Edward Raff
conference: Arxiv
year: 2021
bibkey: joyce2021motif
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.15031'}]
tags: ["Datasets", "Evaluation"]
short_authors: Joyce et al.
---
Malware family classification is a significant issue with public safety and
research implications that has been hindered by the high cost of expert labels.
The vast majority of corpora use noisy labeling approaches that obstruct
definitive quantification of results and study of deeper interactions. In order
to provide the data needed to advance further, we have created the Malware
Open-source Threat Intelligence Family (MOTIF) dataset. MOTIF contains 3,095
malware samples from 454 families, making it the largest and most diverse
public malware dataset with ground truth family labels to date, nearly 3x
larger than any prior expert-labeled corpus and 36x larger than the prior
Windows malware corpus. MOTIF also comes with a mapping from malware samples to
threat reports published by reputable industry sources, which both validates
the labels and opens new research opportunities in connecting opaque malware
samples to human-readable descriptions. This enables important evaluations that
are normally infeasible due to non-standardized reporting in industry. For
example, we provide aliases of the different names used to describe the same
malware family, allowing us to benchmark for the first time accuracy of
existing tools when names are obtained from differing sources. Evaluation
results obtained using the MOTIF dataset indicate that existing tasks have
significant room for improvement, with accuracy of antivirus majority voting
measured at only 62.10% and the well-known AVClass tool having just 46.78%
accuracy. Our findings indicate that malware family classification suffers a
type of labeling noise unlike that studied in most ML literature, due to the
large open set of classes that may not be known from the sample under
consideration