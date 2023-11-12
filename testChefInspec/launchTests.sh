# Tests ftp
inspec exec /root/ftp/ -t ssh://paco:1234@192.168.1.3

# Tests mysql
inspec exec /root/mysql/ -t ssh://paco:1234@192.168.1.5

# Tests http (apache2)
inspec exec /root/http/ -t ssh://paco:1234@192.168.1.4

# Tests ssh
inspec exec /root/ssh/ -t ssh://paco:1234@192.168.1.4
