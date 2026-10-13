---
lang: zh-CN
translation_url: /
layout: about
title: 关于我
description: 杨佶昌的学术主页。香港大学电机与计算机工程系博士后研究员，研究方向包括存内计算、忆阻器、模拟电路与边缘人工智能。
permalink: /zh/
subtitle: 博士后研究员 · 香港大学电机与计算机工程系
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
    <div class="profile-contact-address"><i class="fa-solid fa-location-dot" aria-hidden="true"></i><span>香港大学电机与计算机工程系</span></div>
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

我目前在**香港大学电机与计算机工程系**从事博士后研究，合作导师为**汪涵教授**，同时隶属于香港大学先进半导体与集成电路中心（CASIC）。博士期间，我师从**汪涵教授**和**王中锐教授**。我以第一作者或共同第一作者身份在 *Nature Communications*、*Science Advances*、*Advanced Materials* 及 IEDM（3 篇）发表论文或获论文接收。

我的研究聚焦于先进半导体器件与边缘人工智能计算系统，重点方向是<span class="research-emphasis">存内计算</span>。目前，我主要开展基于忆阻器（RRAM）的存内计算系统电路优化，致力于突破边缘端高效推理与本地学习面临的硬件瓶颈。

除芯片本身外，我也围绕芯片构建嵌入式系统，在电路设计、<span class="research-emphasis">软硬件协同设计</span>和控制系统仿真方面积累了实践经验。结合此前在电力电子与电机控制领域的研究基础，我希望将存内计算引入工业控制与嵌入式应用，构建更智能、更高效的边缘计算系统。

<div class="research-topics" aria-label="研究方向">
  <span><i class="fa-solid fa-microchip" aria-hidden="true"></i>存内计算</span>
  <span><i class="fa-solid fa-layer-group" aria-hidden="true"></i>忆阻器</span>
  <span><i class="fa-solid fa-network-wired" aria-hidden="true"></i>边缘人工智能</span>
  <span><i class="fa-solid fa-wave-square" aria-hidden="true"></i>模拟电路</span>
</div>

<h2 id="news" class="section-heading"><i class="fa-solid fa-bullhorn" aria-hidden="true"></i>最新动态</h2>

<div class="news-scroll" tabindex="0" role="region" aria-label="最新动态">
{% include news-list.liquid %}
</div>

<h2 id="selected-publications" class="section-heading"><i class="fa-solid fa-book-open" aria-hidden="true"></i>代表论文</h2>


{% assign selected = site.publications | where: "selected", true | sort: "selected_order" %}
{% include publication-list.liquid papers=selected compact=true %}

[查看全部论文 →]({{ '/zh/publications/' | relative_url }})

<h2 id="education" class="section-heading"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>教育经历</h2>

{% include education.liquid %}

<h2 id="talks" class="section-heading"><i class="fa-solid fa-microphone" aria-hidden="true"></i>学术报告</h2>

{% include talks-list.liquid %}

<h2 id="teaching" class="section-heading"><i class="fa-solid fa-chalkboard-user" aria-hidden="true"></i>教学经历</h2>

{% include teaching-list.liquid %}
