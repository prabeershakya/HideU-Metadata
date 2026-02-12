# 🔐 HideU Metadata – Digital Forensics & Steganography Suite

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

**HideU Metadata** is a powerful, all‑in‑one graphical forensic toolkit.  
It enables investigators, students, and security enthusiasts to **extract metadata**, **hide & reveal secret messages in images**, **detect steganographic traces**, **batch‑process entire folders**, and **inspect raw hexadecimal data** – all through a sleek, modern dark‑themed interface.

---

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🖼️ Screenshots](#️-screenshots)
- [🚀 Installation](#-installation)
- [📖 Usage Guide](#-usage-guide)
- [🧩 Dependencies](#-dependencies)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## ✨ Key Features

### 📊 Metadata Explorer
- **File System Metadata** – name, size, creation/modification/access timestamps.
- **Cryptographic Hashes** – MD5, SHA‑1, SHA‑256 (computed instantly).
- **Image Metadata** – EXIF (camera, exposure, GPS), dimensions, format, animated GIF detection.
- **Document Metadata** – PDF (author, title, pages, encryption), DOCX/XLSX (core properties, word count, sheets).
- **Live Statistics** – file count, size, hash count, last modified date.

### 🔓 Steganography Lab (LSB)
- **Hide** any text message inside **PNG, BMP, TIFF** images (lossless formats).
- **Reveal** hidden messages from previously encoded PNG files.
- **Capacity Estimator** – shows maximum bytes you can hide in the selected image.
- **JPEG Warning** – alerts that lossy compression will destroy hidden data.
- **Pure LSB embedding** – no password obfuscation, direct bit‑level encoding.

### 🔎 Steganalysis Tools
- **LSB Ratio** – percentage of 1s in the least significant bits.
- **Entropy Calculation** – measures pixel randomness (high values suggest encrypted/carved data).
- **File Size Anomaly Detection** – compares actual size with expected size.
- **Automated Suspicion Indicators** – highlights potential steganographic content.

### 📦 Batch Processor
- Scan an entire folder (top‑level) and analyse every file.
- Display: file name, type, size, truncated MD5, heuristic status (**✅ Clean**, **⚠️ Large**, **🔴 Executable**).
- Export full report as a **text file**.
- Results stored for JSON export.

### 🔢 Hex Inspector
- Load any file and view its **hexadecimal + ASCII representation**.
- 16 bytes per line, classic `offset: hex bytes   ascii` format.
- Truncated after 2 KB for performance (configurable).

### 💾 Reporting & Export
- **Export metadata & batch results to JSON** – includes timestamp and full forensic data.
- **Clear Session** – reset all tabs and stored data with one click.

---

## 🚀 Installation

### Prerequisites
- Python **3.8 or higher**
- `pip` (Python package installer)

### Step‑by‑Step

1. **Clone the repository**  
   ```bash
   git clone https://github.com/prabeershakya/hideu-metadata.git
   cd hideu-metadata
