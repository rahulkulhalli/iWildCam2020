import os
'''
import tensorflow as tf


class Logger(object):
    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""
        self.writer = tf.summary.FileWriter(log_dir)

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""
        summary = tf.Summary(value=[tf.Summary.Value(tag=tag, simple_value=value)])
        self.writer.add_summary(summary, step)

    def list_of_scalars_summary(self, tag_value_pairs, step):
        """Log scalar variables."""
        summary = tf.Summary(value=[tf.Summary.Value(tag=tag, simple_value=value) for tag, value in tag_value_pairs])
        self.writer.add_summary(summary, step)
'''
  
class Logger:
    
    def __init__(self, log_dir):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_string = []
        
    def write_log(self, epoch):
        with open(os.path.join(self.log_dir, '{}.txt'.format(epoch)), 'w') as f:
            f.write('\n'.join(self.log_string))
        self.log_string = []
            
    def list_of_scalars_summary(self, tag_value_pairs, step):
        values = []
        for pair in tag_value_pairs:
            values.append('{}: {}'.format(pair[0], pair[1]))
        string = ' | '.join([str(step)] + values)
        self.log_string.append(string)