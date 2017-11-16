# coding: utf-8
 
from fabric.api import run, env

from jump import helpers


def _set_env(server):
    env.host_string = helpers.get_env('%s_host' % server)
    env.user = helpers.get_env('%s_user' % server)
    env.password = helpers.get_env('%s_password' % server)


def main(args):
    _set_env(args[0])
    
    run('pwd')