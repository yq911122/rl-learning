#!/usr/bin/python
# -*- coding: utf-8 -*-

class DeepQNetworkEnhancer():
    
    def __init__(self, dqn):
        self.dqn = dqn
    
    def apply_double_dqn(self):
        self.dqn.get_input_q_values = self.dqn.get_double_dqn_input_q_values
        return self.dqn
        
    def apply_prioritized_replay(self):
        pass