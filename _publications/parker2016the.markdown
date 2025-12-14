---
layout: publication
title: 'The CUDA LATCH Binary Descriptor: Because Sometimes Faster Means Better'
authors: Christopher Parker, Matthew Daiter, Kareem Omar, Gil Levi, Tal Hassner
conference: Lecture Notes in Computer Science
year: 2016
bibkey: parker2016the
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.03986'}]
tags: [Uncategorized]
short_authors: Parker et al.
---
Accuracy, descriptor size, and the time required for extraction and matching
are all important factors when selecting local image descriptors. To optimize
over all these requirements, this paper presents a CUDA port for the recent
Learned Arrangement of Three Patches (LATCH) binary descriptors to the GPU
platform. The design of LATCH makes it well suited for GPU processing. Owing to
its small size and binary nature, the GPU can further be used to efficiently
match LATCH features. Taken together, this leads to breakneck descriptor
extraction and matching speeds. We evaluate the trade off between these speeds
and the quality of results in a feature matching intensive application. To this
end, we use our proposed CUDA LATCH (CLATCH) to recover structure from motion
(SfM), comparing 3D reconstructions and speed using different representations.
Our results show that CLATCH provides high quality 3D reconstructions at
fractions of the time required by other representations, with little, if any,
loss of reconstruction quality.