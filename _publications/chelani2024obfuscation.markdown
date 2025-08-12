---
layout: publication
title: Obfuscation Based Privacy Preserving Representations Are Recoverable Using
  Neighborhood Information
authors: Kunal Chelani, Assia Benbihi, Fredrik Kahl, Torsten Sattler, Zuzana Kukelova
conference: Arxiv
year: 2024
bibkey: chelani2024obfuscation
citations: 0
additional_links: [{name: Code, url: 'https://github.com/kunalchelani/RecoverPointsNeighborhood'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.11536'}]
tags: []
short_authors: Chelani et al.
---
Rapid growth in the popularity of AR/VR/MR applications and cloud-based
visual localization systems has given rise to an increased focus on the privacy
of user content in the localization process. This privacy concern has been
further escalated by the ability of deep neural networks to recover detailed
images of a scene from a sparse set of 3D or 2D points and their descriptors -
the so-called inversion attacks. Research on privacy-preserving localization
has therefore focused on preventing these inversion attacks on both the query
image keypoints and the 3D points of the scene map. To this end, several
geometry obfuscation techniques that lift points to higher-dimensional spaces,
i.e., lines or planes, or that swap coordinates between points % have been
proposed. In this paper, we point to a common weakness of these obfuscations
that allows to recover approximations of the original point positions under the
assumption of known neighborhoods. We further show that these neighborhoods can
be computed by learning to identify descriptors that co-occur in neighborhoods.
Extensive experiments show that our approach for point recovery is practically
applicable to all existing geometric obfuscation schemes. Our results show that
these schemes should not be considered privacy-preserving, even though they are
claimed to be privacy-preserving. Code will be available at
https://github.com/kunalchelani/RecoverPointsNeighborhood.