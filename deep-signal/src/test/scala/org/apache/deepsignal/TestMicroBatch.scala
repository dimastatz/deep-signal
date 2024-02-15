package org.apache.deepsignal

import scala.util.Success
import org.scalatest.funsuite.AnyFunSuite
import org.apache.deepsignal.whisper.MicroBatch


class TestMicroBatch extends AnyFunSuite{
    test("testSimpleCase") {
        val context = "testSimpleCase".getBytes()
        val tryLoadModel = MicroBatch.loadModel("", "")
        assert(MicroBatch.process(context, tryLoadModel.get) == Success(""))
    }

    test("testLoadModel") {
        val tryLoadModel = MicroBatch.loadModel("", "")
        assert(tryLoadModel.isFailure)
    }
}
