---
layout: publication
title: Re-purposing Perceptual Hashing Based Client Side Scanning For Physical Surveillance
authors: Ashish Hooda, Andrey Labunets, Tadayoshi Kohno, Earlence Fernandes
conference: Arxiv
year: 2022
bibkey: hooda2022re
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.04107'}]
tags: ["Hashing Methods", "Robustness"]
short_authors: Hooda et al.
---
Content scanning systems employ perceptual hashing algorithms to scan user
content for illegal material, such as child pornography or terrorist
recruitment flyers. Perceptual hashing algorithms help determine whether two
images are visually similar while preserving the privacy of the input images.
Several efforts from industry and academia propose to conduct content scanning
on client devices such as smartphones due to the impending roll out of
end-to-end encryption that will make server-side content scanning difficult.
However, these proposals have met with strong criticism because of the
potential for the technology to be misused and re-purposed. Our work informs
this conversation by experimentally characterizing the potential for one type
of misuse -- attackers manipulating the content scanning system to perform
physical surveillance on target locations. Our contributions are threefold: (1)
we offer a definition of physical surveillance in the context of client-side
image scanning systems; (2) we experimentally characterize this risk and create
a surveillance algorithm that achieves physical surveillance rates of >40% by
poisoning 5% of the perceptual hash database; (3) we experimentally study the
trade-off between the robustness of client-side image scanning systems and
surveillance, showing that more robust detection of illegal material leads to
increased potential for physical surveillance.