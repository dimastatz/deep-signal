package org.apache.deepsignal

import org.scalatest.funsuite.AnyFunSuite
import org.apache.deepsignal.whisper.MicroBatch


class TestMicroBatch extends AnyFunSuite{
    test("testSimpleCase") {
        val context = "testSimpleCase".getBytes()
        assert(MicroBatch.process(context) == context.length.toString)
    }
}
