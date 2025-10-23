<div align="center">
<h1 align="center"> DeepSignal </h1> 
<h3>Audio-Based Conversation Analysis</br></h3>
<img src="https://img.shields.io/badge/Progress-1%25-red"> <img src="https://img.shields.io/badge/Feedback-Welcome-green">
</br>
</br>
<kbd>
<img src="/docs/images/deep-signal.png" width="256px"> 
</kbd>
</div>

# 🎧 DeepSignal — Audio-Based Conversation Analysis

**DeepSignal** is a Python library designed to extract rich analytical signals directly from audio files — without relying on transcripts or text analysis. It focuses purely on acoustic and prosodic features to help researchers, developers, and data scientists understand conversational dynamics, emotional tone, and speaking patterns.

---

## 🚀 Features

AudioSignals provides end-to-end analysis of raw audio conversations, including:

| Category | Description | Example Metrics |
|-----------|--------------|-----------------|
| 🎚️ **Basic Audio Stats** | Extracts simple sound metrics useful for quality and consistency checks. | RMS Energy, Duration, Silence Ratio |
| 🗣️ **Voice Activity Detection (VAD)** | Identifies speaking vs. silence segments. | Speech Segments, Turn Counts |
| 🎵 **Pitch & Prosody** | Analyzes intonation and variation in tone. | Average Pitch, Pitch Variance |
| 💬 **Speech Tempo** | Measures speaking rate and rhythm. | Words per Minute (approx), Speech Rate |
| 🔊 **Energy Dynamics** | Examines loudness variation to detect emphasis or excitement. | Mean Energy, Energy Variability |
| 😠 **Emotion & Tone Estimation** | Classifies emotional states using pretrained acoustic models. | Calm, Happy, Angry, Sad |
| ⏱️ **Overlap & Turn-Taking** | Detects interruptions and conversational overlap. | Speaker Overlap %, Turn Durations |
| 🌈 **Spectral Features** | Extracts frequency-domain data for ML and acoustic analysis. | MFCCs, Spectral Centroid, Roll-off |
| 🎯 **Audio Quality** | Evaluates clarity and background noise. | SNR (Signal-to-Noise Ratio), Distortion |
| 🧠 **Derived Conversation Insights** | Combines features to infer interaction quality. | Engagement Index, Talk/Listen Ratio |

---

## 🧩 Example Use Cases

- Conversation analytics for **call centers** or **AI voice agents**  
- Measuring **emotional tone** or **stress levels** in speech  
- Detecting **dominance** or **interruptions** in meetings  
- Generating **audio-based KPIs** for human–AI interactions  
- Building **real-time feedback tools** for voice communication training  

---

## 🛠️ Installation

```bash
pip install audiosignals
```

---

## 🧪 Quick Start

```python
from audiosignals import AudioAnalyzer

# Load and analyze an audio file
analyzer = AudioAnalyzer("conversation.wav")

# Run full analysis
report = analyzer.analyze_all()

# Print summary
print(report.summary())

# Access individual feature groups
print(report.pitch.mean)
print(report.energy.variance)
print(report.emotion.probabilities)
```

---

## 📊 Example Output

```json
{
  "duration_sec": 180.4,
  "speech_segments": 56,
  "average_pitch_hz": 201.3,
  "pitch_variance": 32.8,
  "mean_energy": -20.5,
  "energy_variability": 0.17,
  "speech_rate_wpm": 142,
  "emotion": {
    "calm": 0.52,
    "happy": 0.28,
    "angry": 0.12,
    "sad": 0.08
  },
  "overlap_ratio": 0.07,
  "engagement_index": 0.81
}
```

---

## ⚙️ Architecture Overview

```
audiosignals/
│
├── core/
│   ├── audio_loader.py         # Handles input normalization, channel merging
│   ├── feature_extractor.py    # Extracts MFCCs, pitch, energy, etc.
│   ├── vad_detector.py         # Voice activity segmentation
│   ├── prosody_analyzer.py     # Pitch, tone, tempo analysis
│   ├── emotion_estimator.py    # Acoustic emotion classification
│   ├── quality_metrics.py      # Noise and clarity estimation
│   └── report_builder.py       # Combines results into structured JSON
│
├── models/
│   ├── emotion_model.onnx
│   └── vad_model.onnx
│
└── utils/
    ├── visualization.py        # Waveform and spectrum plots
    └── audio_helpers.py
```

---

## 🧬 Technical Dependencies

| Library | Purpose |
|----------|----------|
| **librosa** | Audio feature extraction |
| **pyAudioAnalysis** | Energy and tempo metrics |
| **webrtcvad** | Voice activity detection |
| **torch / onnxruntime** | Emotion classification models |
| **numpy / scipy** | Signal processing |
| **matplotlib** | Visualization (optional) |

---

## 🧠 Example Analysis Pipeline

```python
from audiosignals.pipeline import AudioPipeline

pipeline = AudioPipeline([
    "vad",
    "pitch",
    "energy",
    "emotion",
    "turn_taking"
])

results = pipeline.run("meeting.wav")
results.plot_waveform()
```

---

## 📈 Metrics Summary

| Metric | Description |
|---------|-------------|
| `duration_sec` | Total length of the audio file |
| `speech_segments` | Number of detected speaking parts |
| `speech_rate_wpm` | Approximate speech tempo |
| `average_pitch_hz` | Average fundamental frequency |
| `energy_variability` | Standard deviation of loudness |
| `overlap_ratio` | % of overlapping speech between speakers |
| `emotion` | Probabilities of acoustic emotion categories |
| `engagement_index` | Combined measure of voice energy, tempo, and tone consistency |

---

## 🧰 CLI Usage

```bash
audiosignals analyze conversation.wav --plot
```

Output includes JSON summary + waveform visualization.

---

## 🧑‍💻 Example Integration

Integrate with your AI or analytics platform:

```python
from audiosignals import AudioAnalyzer

analyzer = AudioAnalyzer("agent_call.wav")
signals = analyzer.get_signals()
agent_metrics = {
    "engagement": signals["engagement_index"],
    "emotion": signals["emotion"]["happy"],
    "speech_rate": signals["speech_rate_wpm"]
}
```

---

## 🔍 Future Roadmap

- [ ] Real-time streaming analysis  
- [ ] Speaker diarization and identification  
- [ ] Gender and age acoustic profiling  
- [ ] Conversation quality score model  
- [ ] REST API integration  

---

## 🧑‍🔬 Author

Developed by **Charles Day & Contributors**  
📫 Contributions welcome via pull requests and GitHub issues.

---

## 📄 License

MIT License © 2025 AudioSignals Team
