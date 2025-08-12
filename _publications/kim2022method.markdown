---
layout: publication
title: A Method For Decrypting Data Infected With Hive Ransomware
authors: Giyoon Kim, Soram Kim, Soojin Kang, Jongsung Kim
conference: Journal of Information Security and Applications
year: 2022
bibkey: kim2022method
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.08477'}]
tags: ["Privacy & Security"]
short_authors: Kim et al.
---
Among the many types of malicious codes, ransomware poses a major threat.
Ransomware encrypts data and demands a ransom in exchange for decryption. As
data recovery is impossible if the encryption key is not obtained, some
companies suffer from considerable damage, such as the payment of huge amounts
of money or the loss of important data. In this paper, we analyzed Hive
ransomware, which appeared in June 2021. Hive ransomware has caused immense
harm, leading the FBI to issue an alert about it. To minimize the damage caused
by Hive Ransomware and to help victims recover their files, we analyzed Hive
Ransomware and studied recovery methods. By analyzing the encryption process of
Hive ransomware, we confirmed that vulnerabilities exist by using their own
encryption algorithm. We have recovered the master key for generating the file
encryption key partially, to enable the decryption of data encrypted by Hive
ransomware. We recovered 95% of the master key without the attacker's RSA
private key and decrypted the actual infected data. To the best of our
knowledge, this is the first successful attempt at decrypting Hive ransomware.
It is expected that our method can be used to reduce the damage caused by Hive
ransomware.