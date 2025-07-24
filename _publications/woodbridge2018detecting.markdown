---
layout: publication
title: Detecting Homoglyph Attacks With A Siamese Neural Network
authors: Jonathan Woodbridge, Hyrum S. Anderson, Anjum Ahuja, Daniel Grant
conference: 2018 IEEE Security and Privacy Workshops (SPW)
year: 2018
bibkey: woodbridge2018detecting
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.09738'}]
tags: ["Datasets", "Evaluation", "Privacy & Security", "Tree Based ANN"]
short_authors: Woodbridge et al.
---
A homoglyph (name spoofing) attack is a common technique used by adversaries
to obfuscate file and domain names. This technique creates process or domain
names that are visually similar to legitimate and recognized names. For
instance, an attacker may create malware with the name svch0st.exe so that in a
visual inspection of running processes or a directory listing, the process or
file name might be mistaken as the Windows system process svchost.exe. There
has been limited published research on detecting homoglyph attacks. Current
approaches rely on string comparison algorithms (such as Levenshtein distance)
that result in computationally heavy solutions with a high number of false
positives. In addition, there is a deficiency in the number of publicly
available datasets for reproducible research, with most datasets focused on
phishing attacks, in which homoglyphs are not always used. This paper presents
a fundamentally different solution to this problem using a Siamese
convolutional neural network (CNN). Rather than leveraging similarity based on
character swaps and deletions, this technique uses a learned metric on strings
rendered as images: a CNN learns features that are optimized to detect visual
similarity of the rendered strings. The trained model is used to convert
thousands of potentially targeted process or domain names to feature vectors.
These feature vectors are indexed using randomized KD-Trees to make similarity
searches extremely fast with minimal computational processing. This technique
shows a considerable 13% to 45% improvement over baseline techniques in terms
of area under the receiver operating characteristic curve (ROC AUC). In
addition, we provide both code and data to further future research.