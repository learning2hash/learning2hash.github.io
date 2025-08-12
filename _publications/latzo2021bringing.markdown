---
layout: publication
title: Bringing Forensic Readiness To Modern Computer Firmware
authors: Tobias Latzo, Florian Hantke, Lukas Kotschi, Felix Freiling
conference: Arxiv
year: 2021
bibkey: latzo2021bringing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.05697'}]
tags: []
short_authors: Latzo et al.
---
Today's computer systems come with a pre-installed tiny operating system, which is also known as UEFI. UEFI has slowly displaced the former legacy PC-BIOS while the main task has not changed: It is responsible for booting the actual operating system. However, features like the network stack make it also useful for other applications. This paper introduces UEberForensIcs, a UEFI application that makes it easy to acquire memory from the firmware, similar to the well-known cold boot attacks. There is even UEFI code called by the operating system during runtime, and we demonstrate how to utilize this for forensic purposes.