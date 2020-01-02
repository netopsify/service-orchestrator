when CLIENT_ACCEPTED { snat 10.197.225.[getfield [IP::client_addr] "." 4] }
