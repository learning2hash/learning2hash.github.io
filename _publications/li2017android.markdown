---
layout: publication
title: Android Malware Clustering Through Malicious Payload Mining
authors: Yuping Li, Jiyong Jang, Xin Hu, Xinming Ou
conference: Lecture Notes in Computer Science
year: 2017
bibkey: li2017android
citations: 64
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.04795'}]
tags: []
short_authors: Li et al.
---
Clustering has been well studied for desktop malware analysis as an effective
triage method. Conventional similarity-based clustering techniques, however,
cannot be immediately applied to Android malware analysis due to the excessive
use of third-party libraries in Android application development and the
widespread use of repackaging in malware development. We design and implement
an Android malware clustering system through iterative mining of malicious
payload and checking whether malware samples share the same version of
malicious payload. Our system utilizes a hierarchical clustering technique and
an efficient bit-vector format to represent Android apps. Experimental results
demonstrate that our clustering approach achieves precision of 0.90 and recall
of 0.75 for Android Genome malware dataset, and average precision of 0.98 and
recall of 0.96 with respect to manually verified ground-truth.