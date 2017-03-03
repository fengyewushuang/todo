from fabric.api import *

env.host=['192.168.1.106']
env.user='root'
env.password = 'root'

def hello():
    print "hello world"

def deploy():
    with cd('/root/todo'):
        run('git pull')
        sudo('supervisorctl status')