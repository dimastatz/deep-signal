package org.apache.deepsignal.whisper

import ai.djl.Model

import java.nio.file.Paths
import scala.util.Try


object MicroBatch {
    def loadModel(path: String, name: String): Try[Model] = Try {
        val model = Model.newInstance(name)
        model.load(Paths.get(path))
        model
    }
}

