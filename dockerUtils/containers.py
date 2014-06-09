# -*- coding: utf-8 -*-
#
# author: Matthieu DANIEL <matthieu.daniel@bull.net>
# Script to launch Qnib Terminal
# 
#

from fabric.api import *
from fabric.colors import *

docker_cmd = 'docker -H 192.168.1.41:6000'

@task
@hosts('localhost')
def pullall():
	"""
	Pull all the docker images and containers
	"""
	print(red('\t\tStarting download of QNIBTerminal images\t\t'))
	# pull all the needed images
	#docker_images = {'fd20','terminal','helixdns','elk','slurm','compute'}
	docker_images = ['fd20','terminal','helixdns','elk','slurm','compute']
	for image in docker_images:
		print docker_cmd+' pull qnib/'+image
		#run(docker_cmd+' pull qnib/'+image)
		local(docker_cmd+' pull qnib/'+image)
		# run('docker pull qnib/'+image)

@task
@hosts('localhost')
def startQNIBTerminal():
	"""
	Start all the containers to launch QNIBTerminal
	"""
	print(red('Launch contrainers for QNIBTerminal'))
	startDNS()
	pass

@task
@hosts('localhost')
def startDNS():
	"""
	Starts DNS, the first container of QNIBTerminal
	"""
	print(red('Launch DNS'))
	pass

@task
@hosts('localhost')
def startELK():
	"""
	Starts ELK container and links with DNS
	"""
	print(red('Launch ELK'))
	pass

@task
@hosts('localhost')
def startCARBON():
	"""
	Starts Carbon contrainer
	"""
