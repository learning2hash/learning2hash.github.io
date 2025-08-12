---
layout: publication
title: 'DAEMON: Dataset-agnostic Explainable Malware Classification Using Multi-stage
  Feature Mining'
authors: Ron Korine, Danny Hendler
conference: IEEE Access
year: 2021
bibkey: korine2020daemon
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.01855'}]
tags: ["Datasets"]
short_authors: Ron Korine, Danny Hendler
---
Numerous metamorphic and polymorphic malicious variants are generated
automatically on a daily basis by mutation engines that transform the code of a
malicious program while retaining its functionality, in order to evade
signature-based detection. These automatic processes have greatly increased the
number of malware variants, deeming their fully-manual analysis impossible.
Malware classification is the task of determining to which family a new
malicious variant belongs. Variants of the same malware family show similar
behavioral patterns. Thus, classifying newly discovered malicious programs and
applications helps assess the risks they pose. Moreover, malware classification
facilitates determining which of the newly discovered variants should undergo
manual analysis by a security expert, in order to determine whether they belong
to a new family (e.g., one whose members exploit a zero-day vulnerability) or
are simply the result of a concept drift within a known malicious family. This
motivated intense research in recent years on devising high-accuracy automatic
tools for malware classification. In this work, we present DAEMON - a novel
dataset-agnostic malware classifier. A key property of DAEMON is that the type
of features it uses and the manner in which they are mined facilitate
understanding the distinctive behavior of malware families, making its
classification decisions explainable. We've optimized DAEMON using a
large-scale dataset of x86 binaries, belonging to a mix of several malware
families targeting computers running Windows. We then re-trained it and applied
it, without any algorithmic change, feature re-engineering or parameter tuning,
to two other large-scale datasets of malicious Android applications consisting
of numerous malware families. DAEMON obtained highly accurate classification
results on all datasets, establishing that it is also platform-agnostic.