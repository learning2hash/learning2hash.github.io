---
layout: publication
title: 'A Survey On Patch-based Synthesis: GPU Implementation And Optimization'
authors: Hadi Abdi Khojasteh
conference: Arxiv
year: 2020
bibkey: khojasteh2020a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.06278'}]
tags: ["Image Retrieval", "Similarity Search", "Survey Paper"]
short_authors: Hadi Abdi Khojasteh
---
This thesis surveys the research in patch-based synthesis and algorithms for
finding correspondences between small local regions of images. We additionally
explore a large kind of applications of this new fast randomized matching
technique. One of the algorithms we have studied in particular is PatchMatch,
can find similar regions or "patches" of an image one to two orders of
magnitude faster than previous techniques. The algorithmic program is driven by
applying mathematical properties of nearest neighbors in natural images. It is
observed that neighboring correspondences tend to be similar or "coherent" and
use this observation in algorithm in order to quickly converge to an
approximate solution. The algorithm is the most general form can find k-nearest
neighbor matching, using patches that translate, rotate, or scale, using
arbitrary descriptors, and between two or more images. Speed-ups are obtained
over various techniques in an exceeding range of those areas. We have explored
many applications of PatchMatch matching algorithm. In computer graphics, we
have explored removing unwanted objects from images, seamlessly moving objects
in images, changing image aspect ratios, and video summarization. In computer
vision we have explored denoising images, object detection, detecting image
forgeries, and detecting symmetries. We conclude by discussing the restrictions
of our algorithmic program, GPU implementation and areas for future analysis.