---
layout: publication
title: Locally Uniform Comparison Image Descriptor
authors: Andrew Ziegler, Eric Christiansen, David Kriegman, Serge Belongie
conference: "Neural Information Processing Systems"
year: 2012
bibkey: ziegler2012locally
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2012/hash/c20ad4d76fe97759aa27a0c99bff6710-Abstract.html"}
tags: ['NEURIPS']
---
Keypoint matching between pairs of images using popular descriptors like SIFT or a faster variant called SURF is at the heart of many computer vision algorithms including recognition mosaicing and structure from motion. For real-time mobile applications very fast but less accurate descriptors like BRIEF and related methods use a random sampling of pairwise comparisons of pixel intensities in an image patch. Here we introduce Locally Uniform Comparison Image Descriptor (LUCID) a simple description method based on permutation distances between the ordering of intensities of RGB values between two patches. LUCID is computable in linear time with respect to patch size and does not require floating point computation. An analysis reveals an underlying issue that limits the potential of BRIEF and related approaches compared to LUCID. Experiments demonstrate that LUCID is faster than BRIEF and its accuracy is directly comparable to SURF while being more than an order of magnitude faster.
