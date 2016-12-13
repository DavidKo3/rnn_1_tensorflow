
## refer http://www.wildml.com/2016/08/rnns-in-tensorflow-a-practical-guide-and-undocumented-features

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf

sequences = [[1,2,3] , [4,5,1],[1,2]]
label_sequences = [[0,1,0], [1, 0,0], [1,1]]

def make_example(sequence, labels):
    # The object we return
    ex = tf.train.SequenceExample()
    # A non-sequencial feature of our example
    sequence_lengh  = len(sequence)
    print( sequence_lengh)
    ex.context.feature["length"].int64_list.value.append(sequence_lengh)
    
    
make_example(sequences, label_sequences)
    