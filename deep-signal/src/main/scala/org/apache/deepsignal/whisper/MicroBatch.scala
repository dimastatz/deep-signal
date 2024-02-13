package org.apache.deepsignal.whisper


object MicroBatch {
    def process(payload: Array[Byte]): String = {
        payload.length.toString
    }
}

