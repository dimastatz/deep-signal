package org.apache.deepsignal

import org.apache.deepsignal.whisper.MicroBatch
import org.scalatest.funsuite.AnyFunSuite


class TestMicroBatch extends AnyFunSuite{
    test("testLoadModel") {
        val tryLoadModel = MicroBatch.loadModel("", "")
        assert(tryLoadModel.isFailure)
    }
}
