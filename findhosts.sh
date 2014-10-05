declare -A known_hosts

known_hosts['192.168.0.1']='NETGEAR Cable Modem'
known_hosts['192.168.0.15']="Tyler's Laptop"
known_hosts['192.168.0.13']="Tyler's Moto X"
known_hosts['192.168.0.16']="Keenan's Desktop Computer"
known_hosts['192.168.0.18']="Tyler's Desktop Computer"
known_hosts['192.168.0.19']="Tyler's Server"
known_hosts['192.168.0.10']="NETGEAR USB Storage"

unknown_host_found=0
yes=1
for HOST in ` sudo nmap -sP 192.168.0.* | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'`
do 
    echo -n "Host Detected: "
	if [ ${known_hosts[$HOST]+abc} ]
		then
			echo "${known_hosts[$HOST]}"; 
	else
		printf "UNKNOWN HOST DETECTED!"
		unknown_host_found=1
	fi
	#echo " "
done

if [ "$unknown_host_found" -eq "$yes"  ]
	then 
		echo "One or more unknown host(s) were detected. Define new host IP address? (y/n)"
		read res
fi
