---
layout: publication
title: Virtual Machine Introspection Based Malware Behavior Profiling And Family Grouping
authors: Shun-Wen Hsiao, Yeali S. Sun, Meng Chang Chen
conference: Arxiv
year: 2017
bibkey: hsiao2017virtual
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.01697'}]
tags: []
short_authors: Shun-Wen Hsiao, Yeali S. Sun, Meng Chang Chen
---
The proliferation of malwares have been attributed to the alternations of a
handful of original malware source codes. The malwares alternated from the same
origin share some intrinsic behaviors and form a malware family. Expediently,
identifying its malware family when a malware is first seen on the Internet can
provide useful clues to mitigate the threat. In this paper, a malware profiler
(VMP) is proposed to profile the execution behaviors of a malware by leveraging
virtual machine introspection (VMI) technique. The VMP inserts plug-ins inside
the virtual machine monitor (VMM) to record the invoked API calls with their
input parameters and return values as the profile of malware. In this paper, a
popular similarity measurement Jaccard distance and a phylogenetic tree
construction method are adopted to discover malware families. The studies of
malware profiles show the malwares from a malware family are very similar to
each others and distinct from other malware families as well as benign
software. This paper also examines VMP against existing anti-malware detection
engines and some well-known malware grouping methods to compare the goodness in
their malware family constructions. A peer voting approach is proposed and the
results show VMP is better than almost all of the compared anti-malware
engines, and compatible with the fine tuned text-mining approach and high order
N-gram approaches. We also establish a malware profiling website based on VMP
for malware research.