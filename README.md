# ECG Signal Filtering & Heart Rate Detection 🫀

This project processes an ECG signal, removes noise, detects R-peaks, and calculates heart rate using the MIT-BIH dataset.

### 📌 Features
- Load real ECG data (MIT-BIH Dataset)
- Noise removal using Bandpass Filter (0.5–40Hz)
- R-peak detection using SciPy
- Heart Rate Calculation (BPM)
- Matplotlib ECG graph visualization

### 🛠 Tech Stack
- Python
- WFDB
- NumPy
- SciPy
- Matplotlib

### 📎 Dataset
MIT-BIH Arrhythmia Database

### ▶ How to Run
```bash
pip install wfdb numpy scipy matplotlib
python ecg_project.py

