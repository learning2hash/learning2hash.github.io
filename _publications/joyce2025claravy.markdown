---
layout: publication
title: 'Claravy: A Tool For Scalable And Accurate Malware Family Labeling'
authors: Robert J. Joyce, Derek Everett, Maya Fuchs, Edward Raff, James Holt
conference: Companion Proceedings of the ACM on Web Conference 2025
year: 2025
bibkey: joyce2025claravy
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.02759'}]
tags: ["Scalability"]
short_authors: Joyce et al.
---
Determining the family to which a malicious file belongs is an essential
component of cyberattack investigation, attribution, and remediation.
Performing this task manually is time consuming and requires expert knowledge.
Automated tools using that label malware using antivirus detections lack
accuracy and/or scalability, making them insufficient for real-world
applications. Three pervasive shortcomings in these tools are responsible: (1)
incorrect parsing of antivirus detections, (2) errors during family alias
resolution, and (3) an inappropriate antivirus aggregation strategy. To address
each of these, we created our own malware family labeling tool called ClarAVy.
ClarAVy utilizes a Variational Bayesian approach to aggregate detections from a
collection of antivirus products into accurate family labels. Our tool scales
to enormous malware datasets, and we evaluated it by labeling \(\approx\)40
million malicious files. ClarAVy has 8 and 12 percentage points higher accuracy
than the prior leading tool in labeling the MOTIF and MalPedia datasets,
respectively.