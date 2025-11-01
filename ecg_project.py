import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# Load record from data folder
record = wfdb.rdrecord('data/101')
signal = record.p_signal[:,0]  # first ECG channel

fs = 360  # Sampling frequency (MIT-BIH standard)

# Plot raw ECG signal
plt.plot(signal)
plt.title("Raw ECG Signal")
plt.show()
from scipy.signal import butter, filtfilt

# Bandpass filter (0.5Hz – 40Hz)
lowcut = 0.5
highcut = 40
b, a = butter(4, [lowcut/(fs/2), highcut/(fs/2)], btype='band')
filtered = filtfilt(b, a, signal)

plt.figure(figsize=(10,4))
plt.plot(filtered)
plt.title("Filtered ECG Signal (Noise Removed)")
plt.show()
from scipy.signal import find_peaks

# detect R peaks
peaks, _ = find_peaks(filtered, distance=fs*0.25, height=np.mean(filtered))

plt.figure(figsize=(10,4))
plt.plot(filtered)
plt.plot(peaks, filtered[peaks], "x")
plt.title("R-Peaks Detection")
plt.show()

# ---- HEART RATE CALCULATION ----
# RR intervals (difference between R-peaks)
rr_intervals = np.diff(peaks) / fs  # seconds between beats

# Calculate heart rate
heart_rate = 60 / np.mean(rr_intervals)

print("\n-----------------------------")
print(f"Estimated Heart Rate = {round(heart_rate)} BPM")
print("-----------------------------\n")
