---
layout: about
title: About
permalink: /
subtitle: 杨佶昌 · Postdoctoral Fellow · Department of Electrical and Computer Engineering, HKU
redirect_from:
  - /about/
  - /about.html
profile:
  align: right
  image: avatar2.JPG
  image_circular: false
  more_info: >
    <ul class="profile-contact-links">
      <li><a href="mailto:yangjc100@connect.hku.hk"><i class="fa-solid fa-envelope" aria-hidden="true"></i><span>yangjc100@connect.hku.hk</span></a></li>
      <li><a href="https://scholar.google.com/citations?user=HpkVT94AAAAJ"><i class="ai ai-google-scholar" aria-hidden="true"></i><span>Google Scholar</span></a></li>
      <li><a href="https://orcid.org/0000-0003-3760-6762"><i class="ai ai-orcid" aria-hidden="true"></i><span>ORCID</span></a></li>
      <li><a href="https://www.researchgate.net/profile/Jichang-Yang"><i class="ai ai-researchgate" aria-hidden="true"></i><span>ResearchGate</span></a></li>
    </ul>
    <div class="profile-contact-address"><i class="fa-solid fa-location-dot" aria-hidden="true"></i><span>Dept. of ECE, HKU</span></div>
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

I am a Postdoctoral Fellow in the **Department of Electrical and Computer Engineering, The University of Hong Kong (HKU)**, supervised by **Prof. Han Wang**. I am also with the **Center for Advanced Semiconductors and Integrated Circuits (CASIC), HKU**. During my PhD, I was advised by **Prof. Han Wang** and **Prof. Zhongrui Wang**. As a first or co-first author, I have papers published or accepted in **Nature Communications**, **Science Advances**, and **Advanced Materials**, and at **IEDM (3 papers)**. My research lies at the intersection of advanced semiconductor devices and next-generation Edge AI computing systems, with a specific focus on <span class="research-emphasis">in-memory computing</span>. My current work involves the circuit-level optimization of RRAM-based in-memory computing systems, aiming to overcome the hardware bottlenecks that limit efficient inference and on-device learning at the edge.

Beyond the chip itself, I build the embedded systems around it, with hands-on experience in circuit design, <span class="research-emphasis">hardware-software co-design</span>, and control system simulation, drawing on my earlier background in power electronics and motor control. I aim to empower traditional industrial frameworks by integrating the intelligent capabilities of in-memory computing, leveraging the synergistic strengths of both to build smarter and more efficient edge computing systems.

<div class="research-topics" aria-label="Research interests">
  <span><i class="fa-solid fa-microchip" aria-hidden="true"></i>In-memory computing</span>
  <span><i class="fa-solid fa-layer-group" aria-hidden="true"></i>Resistive memory</span>
  <span><i class="fa-solid fa-network-wired" aria-hidden="true"></i>Edge AI</span>
  <span><i class="fa-solid fa-wave-square" aria-hidden="true"></i>Analog circuits</span>
</div>

<h2 id="news" class="section-heading"><i class="fa-solid fa-bullhorn" aria-hidden="true"></i>News</h2>

<div class="news-scroll" tabindex="0" role="region" aria-label="News and updates">
{% include news-list.liquid %}
</div>

<h2 id="selected-publications" class="section-heading"><i class="fa-solid fa-book-open" aria-hidden="true"></i>Selected publications</h2>


{% assign selected = site.publications | where: "selected", true | sort: "selected_order" %}
{% include publication-list.liquid papers=selected compact=true %}

[View all publications →]({{ '/publications/' | relative_url }})

<h2 id="education" class="section-heading"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>Education</h2>

{% include education.liquid %}

<h2 id="talks" class="section-heading"><i class="fa-solid fa-microphone" aria-hidden="true"></i>Talks</h2>

{% include talks-list.liquid %}

<h2 id="teaching" class="section-heading"><i class="fa-solid fa-chalkboard-user" aria-hidden="true"></i>Teaching</h2>

{% include teaching-list.liquid %}
