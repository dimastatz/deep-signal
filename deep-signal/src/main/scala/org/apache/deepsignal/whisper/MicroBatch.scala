package org.apache.deepsignal.whisper

import ai.djl.Model
import scala.util.Try
import java.nio.file.Paths
import ai.djl.translate.Translator


object MicroBatch {
    def loadModel(path: String, name: String): Try[Model] = Try {
        val model = Model.newInstance(name)
        model.load(Paths.get(path))
        model
    }


    def process(payload: Array[Byte], model: Model): Try[String] = Try {
        val translator = getTranslator()
        val predictor = model.newPredictor(translator)
        predictor.predict(payload)
    }

    def getTranslator(): Translator[Array[Byte], String] = ???
}

