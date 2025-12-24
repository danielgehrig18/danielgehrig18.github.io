---
title: "Event-based Agile Object Catching with a Quadrupedal Robot"
authors:
- Benedek Forrai*
- Takahiro Miki*
- Daniel Gehrig*
- Marco Hutter
- Davide Scaramuzza

author_notes:
- "Equal contribution"
- "Equal contribution"
##date: "2015-09-01T00:00:00Z"
#doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-05-29T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Int. Conf. Robot. Autom. (ICRA)*"
publication_short: ""

abstract: "Quadrupedal robots are conquering various applications in indoor and outdoor environments due to their capability to navigate challenging uneven terrains. Exteroceptive information greatly enhances this capability since perceiving their surroundings allows them to adapt their controller and thus achieve higher levels of robustness. However, sensors such as LiDARs and RGB cameras do not provide sufficient information to quickly and precisely react in a highly dynamic environment since they suffer from a bandwidth-latency tradeoff. They require significant bandwidth at high frame rates while featuring significant perceptual latency at lower frame rates, thereby limiting their versatility on resource constrained platforms. In this work, we tackle this problem by equipping our quadruped with an event camera, which does not suffer from this tradeoff due to its asynchronous and sparse operation. In levering the low latency of the events, we push the limits of quadruped agility and demonstrating high-speed ball catching with a net for the first time. We show that our quadruped equipped with an event-camera can catch objects at maximum speeds of 15 m/s from 4 meters, with a success rate of 83%. With a VGA event camera, our method runs at 100 Hz on an NVIDIA Jetson Orin."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
- Computer Vision
- Reinforcement Learning
featured: True

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/ICRA23_Forrai.pdf
url_code: 'https://github.com/uzh-rpg/event-based_object_catching_anymal/'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/FpsVB8EO54M'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
Here we explore the advantages of using event cameras to catch high-speed objects at up 15 m/s with the quadrupedal robot ANYmal. Our paper "Event-based Agile Object Catching with a Quadrupedal Robot" was featured on IEEE Spectrum. Read the article [here](https://spectrum.ieee.org/quadrupedal-robot).
{{% /callout %}}
