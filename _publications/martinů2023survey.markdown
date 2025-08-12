---
layout: publication
title: A Survey Of Feature Detection Methods For Localisation Of Plain Sections Of
  Axial Brain Magnetic Resonance Imaging
authors: "Ji\u0159\xED Martin\u016F, Jan Novotn\xFD, Karel Ad\xE1mek, Petr \u010C\
  erm\xE1k, Ji\u0159\xED Kozel, David \u0160koloud\xEDk"
conference: Biomedical Signal Processing and Control
year: 2023
bibkey: "martin\u016F2023survey"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.04173'}]
tags: ["Survey Paper"]
short_authors: "Martin\u016F et al."
---
Matching MRI brain images between patients or mapping patients' MRI slices to
the simulated atlas of a brain is key to the automatic registration of MRI of a
brain. The ability to match MRI images would also enable such applications as
indexing and searching MRI images among multiple patients or selecting images
from the region of interest. In this work, we have introduced robustness,
accuracy and cumulative distance metrics and methodology that allows us to
compare different techniques and approaches in matching brain MRI of different
patients or matching MRI brain slice to a position in the brain atlas. To that
end, we have used feature detection methods AGAST, AKAZE, BRISK, GFTT, HardNet,
and ORB, which are established methods in image processing, and compared them
on their resistance to image degradation and their ability to match the same
brain MRI slice of different patients. We have demonstrated that some of these
techniques can correctly match most of the brain MRI slices of different
patients. When matching is performed with the atlas of the human brain, their
performance is significantly lower. The best performing feature detection
method was a combination of SIFT detector and HardNet descriptor that achieved
93% accuracy in matching images with other patients and only 52% accurately
matched images when compared to atlas.