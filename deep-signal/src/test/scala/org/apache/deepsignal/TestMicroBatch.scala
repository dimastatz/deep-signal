package org.apache.deepsignal

import java.nio.file.Paths
import org.scalatest.funsuite.AnyFunSuite
import org.apache.deepsignal.whisper.MicroBatch


class TestMicroBatch extends AnyFunSuite{
    test("testLoadModel") {
        println(Paths.get(".").toAbsolutePath)
        val tryLoadModel = MicroBatch.loadModel("", "")
        assert(tryLoadModel.isFailure)
    }
}
