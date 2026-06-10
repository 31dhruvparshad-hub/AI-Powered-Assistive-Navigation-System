# AI-Powered Assistive Navigation System 
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ccee9855-0d45-4b9b-807f-dadf926a019a" />


## Overview

An AI-powered assistive navigation system designed to enhance independent mobility through real-time obstacle detection, spatial awareness, and intelligent voice guidance.

The system leverages YOLOv8-based object detection, proximity estimation, danger-zone analysis, and adaptive audio feedback to identify obstacles and provide navigation instructions in dynamic environments.

---

## Features

* Real-Time Object Detection using YOLOv8
* Spatial Localization (Left / Center / Right)
* Proximity Estimation
* Danger Zone Analysis
* Closest Obstacle Prioritization
* Adaptive Voice Guidance
* Real-Time Webcam Processing
* FPS Monitoring
* Accessibility-Focused Navigation Assistance

---

## System Architecture

Camera Feed
→ YOLOv8 Object Detection
→ Position Detection
→ Distance Estimation
→ Danger Zone Analysis
→ Navigation Decision Engine
→ Audio Guidance

---

## Technology Stack

* Python
* YOLOv8
* OpenCV
* NumPy
* PyTorch
* pyttsx3

---

## Example Voice Alerts

* "Person ahead. Move left."
* "Chair ahead. Move right."
* "Caution. Person on your left."
* "Person nearby."

---

## Project Workflow

1. Capture live video from webcam.
2. Detect obstacles using YOLOv8.
3. Determine obstacle position.
4. Estimate obstacle proximity.
5. Identify potential collision risks.
6. Generate contextual voice guidance.

---

## Future Enhancements

* Monocular Depth Estimation (MiDaS / Depth Anything)
* Multi-Object Tracking
* GPS Integration
* Route Planning
* Edge Deployment on Raspberry Pi
* Emergency SOS System

---

## Author

Dhruv Parshad
