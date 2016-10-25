"""Word count topology"""

from streamparse import Grouping, Topology

from bolts import MultiBolt, TypeOne, TypeTwo
from spouts import ValueSpout


class WordCount(Topology):
    value_spout = ValueSpout.spec()
    multi_bolt = MultiBolt.spec(inputs={value_spout: Grouping.SHUFFLE})
    one_bolt = TypeOne.spec(inputs={multi_bolt['word']: Grouping.SHUFFLE})
    two_bolt = TypeTwo.spec(inputs={multi_bolt['number']: Grouping.SHUFFLE})
