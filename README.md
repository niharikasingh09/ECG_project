
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
### ✅ How to Run
```bash
pip install wfdb numpy scipy matplotlib
python ecg_project.py
```



### 📊 Output Results

#### ✅ Raw ECG Signal
Shows the original ECG waveform from MIT-BIH dataset.

![Raw ECG](Screenshots/raw_signal.png)

---

#### ✅ Filtered ECG Signal (Noise Removed)
Applied 0.5–40 Hz bandpass filter to remove noise and baseline drift.

![Filtered ECG](Screenshots/filtered_signal.png)

---

#### ✅ R-Peak Detection
Detected R-peaks used to calculate Heart Rate (BPM).

![R Peak Detection](Screenshots/rpeak_detection.png)

---
