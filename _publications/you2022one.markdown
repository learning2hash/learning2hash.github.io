---
layout: publication
title: One-shot General Object Localization
authors: Yang You, Zhuochen Miao, Kai Xiong, Weiming Wang, Cewu Lu
conference: Arxiv
year: 2022
bibkey: you2022one
citations: 0
additional_links: [{name: Code, url: 'https://github.com/qq456cvb/OneLoc'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.13392'}]
tags: []
short_authors: You et al.
---
This paper presents a general one-shot object localization algorithm called
OneLoc. Current one-shot object localization or detection methods either rely
on a slow exhaustive feature matching process or lack the ability to generalize
to novel objects. In contrast, our proposed OneLoc algorithm efficiently finds
the object center and bounding box size by a special voting scheme. To keep our
method scale-invariant, only unit center offset directions and relative sizes
are estimated. A novel dense equalized voting module is proposed to better
locate small texture-less objects. Experiments show that the proposed method
achieves state-of-the-art overall performance on two datasets: OnePose dataset
and LINEMOD dataset. In addition, our method can also achieve one-shot
multi-instance detection and non-rigid object localization. Code repository:
https://github.com/qq456cvb/OneLoc.