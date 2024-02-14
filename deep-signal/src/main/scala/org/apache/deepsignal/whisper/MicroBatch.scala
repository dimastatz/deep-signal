package org.apache.deepsignal.whisper

import ai.djl.Model
import scala.util.Try
import java.nio.file.Paths


object MicroBatch {
    def loadModel(path: String, name: String): Try[Model] = Try {
        val model = Model.newInstance(name)
        model.load(Paths.get(path))
        model
    }


    def process(payload: Array[Byte]): String = {
        payload.length.toString
    }
}

