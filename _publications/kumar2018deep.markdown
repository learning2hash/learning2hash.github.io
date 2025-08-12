---
layout: publication
title: Deep Spectral Correspondence For Matching Disparate Image Pairs
authors: Arun Cs Kumar, Shefali Srivastava, Anirban Mukhopadhyay, Suchendra M. Bhandarkar
conference: Arxiv
year: 2018
bibkey: kumar2018deep
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.04642'}]
tags: []
short_authors: Kumar et al.
---
A novel, non-learning-based, saliency-aware, shape-cognizant correspondence
determination technique is proposed for matching image pairs that are
significantly disparate in nature. Images in the real world often exhibit high
degrees of variation in scale, orientation, viewpoint, illumination and affine
projection parameters, and are often accompanied by the presence of textureless
regions and complete or partial occlusion of scene objects. The above
conditions confound most correspondence determination techniques by rendering
impractical the use of global contour-based descriptors or local pixel-level
features for establishing correspondence. The proposed deep spectral
correspondence (DSC) determination scheme harnesses the representational power
of local feature descriptors to derive a complex high-level global shape
representation for matching disparate images. The proposed scheme reasons about
correspondence between disparate images using high-level global shape cues
derived from low-level local feature descriptors. Consequently, the proposed
scheme enjoys the best of both worlds, i.e., a high degree of invariance to
affine parameters such as scale, orientation, viewpoint, illumination afforded
by the global shape cues and robustness to occlusion provided by the low-level
feature descriptors. While the shape-based component within the proposed scheme
infers what to look for, an additional saliency-based component dictates where
to look at thereby tackling the noisy correspondences arising from the presence
of textureless regions and complex backgrounds. In the proposed scheme, a joint
image graph is constructed using distances computed between interest points in
the appearance (i.e., image) space. Eigenspectral decomposition of the joint
image graph allows for reasoning about shape similarity to be performed
jointly, in the appearance space and eigenspace.