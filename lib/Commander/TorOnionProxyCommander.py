#!/usr/bin/env python3
#sys.path.append(os.path.abspath('../'))
from Environment.TorEnvironment import TorEnvironment
from Commander.TorBaseCommander import TorBaseCommander
from Wrapper.Tor import Tor


class TorOnionProxyCommander(TorBaseCommander):
    def __init__(self, **kwargs):
        '''
        doc doc doc
        '''
        if 'nick_name' not in kwargs:
            kwargs['nick_name'] = 'op'

        super(TorOnionProxyCommander, self).__init__(
                        conf_tmpl='torrc.op.tmpl', **kwargs)

    def run(self, **kwargs):
        return self.exe.run_tor_op(**kwargs)
