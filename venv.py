# -*- coding: utf-8 -*-
import os
import sys


class Pathenv:
    """
    [Usage]
    from virtualenv import Pathenv
    Pathenv.apply_virtualenv('_venv')
    import requests
    """
    SCRIPT_DIR = os.path.realpath(os.path.dirname(__file__))

    @classmethod
    def apply_virtualenv(cls, virtualenv):
        os_distinct = 'Scripts' if os.name is 'nt' else 'bin'
        activate_this_path = os.path.join(cls.SCRIPT_DIR, virtualenv, os_distinct, 'activate_this.py')

        if os.path.isfile(activate_this_path):
            # Python3: exec(open(...).read(), Python 2: execfile(...)
            if sys.version_info > (3,):
                exec (open(activate_this_path).read(), dict(__file__=activate_this_path))
            else:
                execfile(activate_this_path, dict(__file__=activate_this_path))