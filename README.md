<div align="center">
<h1 align="center"> DeepSignal </h1> 
<h3>An Open-Source Framework for Multimedia Processing on Apache Spark</br></h3>
<img src="https://img.shields.io/badge/Progress-1%25-red"> <img src="https://img.shields.io/badge/Feedback-Welcome-green">
</br>
</br>
<kbd>
<img src="/docs/images/deep-signal.png" width="256px"> 
</kbd>
</div>


## Overview
With the pervasive adoption of cameras and microphones, coupled with the surge in remote communication via video and audio calls, the volume of multimedia data is rapidly expanding. This trend underscores the critical importance of video and audio analysis across diverse sectors, including healthcare, finance, and education. Recognizing this need, the Deep Signal framework emerges as a solution, aiming to provide centralized, real-time analysis of multimedia data. 

- Deep Signal, leveraging [Apache Spark's](https://spark.apache.org/) robust infrastructure, simplifies scalable processing and analysis. It ensures smooth integration across different programming languages and provides accessible tools for developers to extract valuable insights from multimedia sources. These tasks range from analyzing sentiments in customer service calls to categorizing content in video streams.

- While Apache Spark excels in handling structured data through Spark SQL, [DataFrames](https://github.com/apache/spark/blob/master/python/pyspark/sql/dataframe.py), and [Datasets](https://github.com/apache/spark/blob/master/sql/core/src/main/scala/org/apache/spark/sql/Dataset.scala), its support for unstructured data, such as text, is also strong with [RDDs](https://github.com/apache/spark/blob/master/core/src/main/scala/org/apache/spark/rdd/RDD.scala). However, when dealing with media data (binary), developers are left to navigate on their own. They lack support for essential operations like speech-to-text conversion, translation, speaker diarization, and object detection.

- To bridge this gap, Deep Signal introduces new interfaces, namely MediaRDD and MediaDStream. These interfaces provide a user-friendly approach for working with distributed collections of media data, enabling ease of use, scalability, and advanced functionality when processing video and audio files.


## Deep Signal Concepts
Deep Signal introduces two new objects to Apache Spark - MediaRDD for Batch processing and MediaDStream for Streaming. MediaRDD is an extension of Apache Spark's RDD, designed for handling distributed media files efficiently. It streamlines operations like speech-to-text conversion, audio file translation, speaker diarization, and more within the Spark framework. This specialized support simplifies multimedia processing tasks for developers.
<div align="center">
<img src="/docs/images/RDD.png"> 
<div>Media <a href="https://spark.apache.org/docs/latest/rdd-programming-guide.html">RDD</a> for DeepSignal Batch</div>
</div><br/>
MediaDStream is an extension of Apache Spark's DStream designed for handling media streams like video and audio. It simplifies the real-time processing and analysis of continuous media data within Spark's streaming framework. With MediaDStream, developers can easily ingest, process, and analyze streaming media content in real-time. It offers specialized functionalities for tasks such as object detection, speech recognition, and sentiment analysis as data flows in. MediaDStream integrates seamlessly with other components of the Spark ecosystem, enabling the development of end-to-end multimedia processing pipelines.
<div align="center">
<img src="/docs/images/Dstream.png"> 
<div>Media <a href="https://spark.apache.org/docs/latest/streaming-programming-guide.html">DStream</a> for DeepSignal Streaming</div>
</div>

## Deep Signal Key Features

### Analyzing Audio data with Deep Signal yields following insights:
- Speech Content: Extracting spoken words, sentences, or phrases from audio files, which is useful for tasks like speech recognition, transcription, or language translation.
- Speaker Identification: Determining the identity of speakers in the audio, which can aid in tasks such as speaker verification, forensic analysis, or speaker diarization.
- Emotional Tone: Analyzing acoustic features related to prosody, intonation, and voice quality to infer the emotional state of speakers, useful for applications like sentiment analysis or emotion detection.
- Environmental Sounds: Identifying and categorizing sounds from the environment, such as footsteps, traffic noise, or bird chirps, which can be used for applications like audio surveillance, wildlife monitoring, or environmental analysis.
- Musical Content: Analyzing musical characteristics such as pitch, rhythm, melody, and timbre, which can be used for tasks like music transcription, genre classification, or recommendation systems.
- Background Noise: Quantifying the level and characteristics of background noise in the audio, which is useful for tasks like noise reduction, enhancement, or quality assessment.
- Audio Effects: Detecting and analyzing audio effects such as reverb, echo, distortion, or filtering, which can be useful for audio production, sound engineering, or forensic analysis.
- Language and Dialect: Identifying the language or regional accent of speakers in the audio, useful for tasks like language detection, dialect recognition, or sociolinguistic analysis.
- Temporal Patterns: Analyzing temporal patterns and trends in the audio signal, such as speech rate, pauses, or turn-taking behavior, which can provide insights into conversational dynamics or speech fluency.

### Analyzing Video data with Deep Signal provides the following insights:
- Visual Content: Extracting visual elements such as objects, scenes, and people present in the video frames.
- Motion Analysis: Analyzing motion patterns, trajectories, and velocities of objects or individuals within the video.
- Activity Recognition: Detecting and categorizing different activities or events occurring in the video, such as walking, running, or gesturing.
- Facial Recognition: Identifying and recognizing faces of individuals appearing in the video, which can be useful for tasks like identity verification or surveillance.
- Object Tracking: Tracking the movement of specific objects or individuals across multiple frames of the video.
- Emotion Detection: Analyzing facial expressions and body language to infer the emotional states of individuals in the video.
- Scene Understanding: Understanding the context and content of different scenes within the video, such as indoor or outdoor environments, day or night scenes, etc.
- Text Recognition: Extracting and recognizing text present in the video frames, such as subtitles, captions, or textual overlays
- Audio Content: Extracting audio signals from the video for further analysis, such as speech recognition, speaker identification, or environmental sound classification.
- Quality Assessment: Evaluating the quality of the video, including factors like resolution, frame rate, compression artifacts, and visual clarity.
- Event Detection: Detecting and identifying specific events or anomalies within the video, such as accidents, crowd gatherings, or abnormal behaviors.
- Content Summarization: Generating summaries or keyframes of the video to provide a concise representation of its content.

# How-To
```scala
// create Spark Context
val sc = new SparkContext(...)

// transcribe audio files
val audioRDD: MediaRDD = sc.mediaFile("path_to_audio_files")
val transcription = audioRDD.collectTranscription()

// collect object from video files
val videoRDD: MediaRDD = sc.mediaFile("path_to_video_files")
val objects = videoRDD.collectObjects()
```
[TBD]() - Add more examples, (streaming ?)







