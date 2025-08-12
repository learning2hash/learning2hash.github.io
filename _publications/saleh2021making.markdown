---
layout: publication
title: 'Making Honey Files Sweeter: Sentryfs -- A Service-oriented Smart Ransomware
  Solution'
authors: Abdul Rahim Saleh, Gihad Al-Nemera, Saif Al-Otaibi, Rashid Tahir, Mohammed
  Alkhatib
conference: Arxiv
year: 2021
bibkey: saleh2021making
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.12792'}]
tags: ["Privacy & Security", "Tools & Libraries"]
short_authors: Saleh et al.
---
The spread of ransomware continues to cause devastation and is a major
concern for the security community. An often-used technique against this threat
is the use of honey (or canary) files, which serve as ``trip wires'' to detect
ransomware in its early stages. However, in our analysis of ransomware samples
from the wild, we discovered that attackers are well-aware of these traps, and
newer variants use several evasive strategies to bypass traditional honey
files. Hence, we present the design of SentryFS - a specialized file system
that strategically ``sprays'' specially-crafted honey files across the file
system. The canaries are generated using Natural Language Processing (NLP) and
the content and the metadata is constantly updated to make the canaries appear
more attractive for smarter ransomware that is selective in choosing victim
files. Furthermore, to assist with the management of the honey files, SentryFS
connects with an anti-ransomware web service to download the latest
intelligence on novel ransomware strategies to update the canaries. Finally, as
a contingency, SentryFS also leverages file clones to prevent processes from
writing to files directly in the event a highly stealthy ransomware goes
undetected. In this case, the ransomware encrypts the clones rather than the
actual files, leaving users' data unmodified. An AI agent then assigns a
suspicion score to the write activity so that users can approve/discard the
changes. As an early-warning system, the proposed design might help mitigate
the problem of ransomware.