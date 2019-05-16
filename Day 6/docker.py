import subprocess as sp
import os
n=int(input("Provide no of dockers to run: "))
	
#id_docker = input("Enter Name")


for i in range(n):
	id_docker = input("Enter Name : ")
	# print("Enter Name")
	#sp.getoutput("docker run -itd --name {} centos:latest".format(id_docker))
	os.system(" docker run -itd --name {} -v /run/media/root/RHEL-7.5\ Server.x86_64:/dvd -v /root/Desktop/rhel7_5_rpm_extras:/rpm -v /root/Desktop/rhel7_extra_new_rpm:/new_rpm -v /root/Desktop/python_lib:/python_lib  centos:latest".format(id_docker))
	#os.system("docker exec -d  {} rm  -f /etc/yum.repos.d/*".format(id_docker))
	#sp.getoutput("docker cp yum_file.repo {}:/etc/yum.repos.d/".format(id_docker))


	sp.getoutput("docker cp file.sh {}:/".format(id_docker))
	sp.getoutput("docker exec {} bash file.sh".format(id_docker))

	sp.getoutput("docker cp yum_file.repo {}:/etc/yum.repos.d/".format(id_docker))
#t= input("Which docker do you want to enter : ")
#sp.getoutput("docker start {} ".format(t))
#os.system("docker attach {}".format(t))


# sp.getoutput("bash docker.sh")
