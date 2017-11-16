# coding: utf-8
 
from fabric.api import run, env
from fabric.colors import green

from jump import helpers


def _set_env(server):
    env.host_string = helpers.get_env('%s_host' % server)
    env.user = helpers.get_env('%s_user' % server)
    env.password = helpers.get_env('%s_password' % server)


def main(args):
    server = args[0]
    _set_env(server)
    
    print(green('Initializing deploy on %s. This could take a while...' % server))
    run('pwd')
    run('bin/magento maintenance:enable')
    run('composer update')
    run('bin/magento setup:upgrade')
    run('bin/magento deploy:mode:set production')
    run('bin/magento maintenance:disable')
    print(green('Deploy successful on %s.') % server)