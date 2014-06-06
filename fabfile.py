# -*- coding: utf-8 -*-
#
# author: Matthieu DANIEL <matthieu.daniel@bull.net>
# Script to launch Qnib Terminal
# 
#


from fabric.api import *
from fabric.colors import *

@task
def whoami():
    """
    Information about the host machine
    """
    all_informations = run('uname -a',quiet=True)
    fqdn = run('hostname -f',quiet=True)
    print(yellow('Informations : ')+all_informations)
    print(yellow('FQDN : ')+fqdn)

@task
@hosts('localhost')
def eval_docker_version():
	"""
	checks client/server version
	"""
	dver = run('docker version |egrep \"(Client|Server) version:\"|awk -F\: \'{print $2}\'|uniq|sed -e \'s/ //g\'',quiet=True,warn_only=True)
	print(red('Docker version : \t'+ dver ))

@task
@hosts('localhost')
def eval_cpuset():
	"""
	Evaluation of the number of CPUs
	"""
	num_cpu = run('grep -c ^processor /proc/cpuinfo',quiet=True,warn_only=True)
	print(red('Number of cpus : \t'+num_cpu))


@task
@hosts('localhost')
def pullall():
	"""
	Pull all the docker images and containers
	"""
	print(red('\t\tStarting download of QNIBTerminal images\t\t'))
	# pull all the needed images
	docker_images={'fd20','terminal','helixdns','elk','slurm','compute'}
	for image in docker_images:
		print 'docker pull qnib/'+image
		# run('docker pull qnib/'+image)
