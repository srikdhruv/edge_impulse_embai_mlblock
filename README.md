# 🩺 Edge AI Cardiac Diagnostic Tool using Earbuds

### Project Overview
This project demonstrates the feasibility of using commodity earbuds as a low-cost cardiac diagnostic tool. The system captures heart sounds using earbuds, processes the audio locally on the device, and performs classification to detect cardiac anomalies such as murmurs. The primary goal is to enable real-time, privacy-preserving health monitoring on consumer devices.

---

## 🌟 Key Features
- **Edge Deployment:** Uses Edge Impulse to deploy lightweight models directly to mobile devices.
- **Real-Time Inference:** Denoises audio and classifies heart sounds locally.
- **Custom ML Block:** Integrates a CNN classifier as a custom block in Edge Impulse.
- **High Portability:** Uses Docker to package the model and dependencies.

---

## 🛠️ Installation & Setup

### Prerequisites
- Docker installed and running.
- A valid Edge Impulse account (Enterprise required for custom ML blocks).
- Python 3.9 or higher.

### 1. Clone the repository
```bash
git clone https://github.com/srikdhruv/edge_impulse_embai_mlblock.git
cd edge_impulse_embai_mlblock
