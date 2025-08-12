---
layout: publication
title: Boosting Image Forgery Detection Using Resampling Features And Copy-move Analysis
authors: Tajuddin Manhar Mohammed, Jason Bunk, Lakshmanan Nataraj, Jawadul H. Bappy,
  Arjuna Flenner, B. S. Manjunath, Shivkumar Chandrasekaran, Amit K. Roy-Chowdhury,
  Lawrence Peterson
conference: Electronic Imaging
year: 2018
bibkey: mohammed2018boosting
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.03154'}]
tags: []
short_authors: Mohammed et al.
---
Realistic image forgeries involve a combination of splicing, resampling,
cloning, region removal and other methods. While resampling detection
algorithms are effective in detecting splicing and resampling, copy-move
detection algorithms excel in detecting cloning and region removal. In this
paper, we combine these complementary approaches in a way that boosts the
overall accuracy of image manipulation detection. We use the copy-move
detection method as a pre-filtering step and pass those images that are
classified as untampered to a deep learning based resampling detection
framework. Experimental results on various datasets including the 2017 NIST
Nimble Challenge Evaluation dataset comprising nearly 10,000 pristine and
tampered images shows that there is a consistent increase of 8%-10% in
detection rates, when copy-move algorithm is combined with different resampling
detection algorithms.