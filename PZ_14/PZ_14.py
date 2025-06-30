# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.


with open('C:\\Users\\vasil\\Desktop\\popovpython\\PZ_14\\ip_address.txt', 'r') as infile:
    
    zero_octet_ips = []
    other_ips = []

    
    for line in infile:
        
        ip = line.strip()
        
        
        if ip.count('.') == 3:
            
            octets = ip.split('.')
            try:
                
                if int(octets[3]) == 0:
                    zero_octet_ips.append(ip)
                else:
                    other_ips.append(ip)
            except ValueError:
                print(f"Некорректный IP-адрес: {ip}")


with open('zero_octet_ips.txt', 'w') as outfile1:
    for ip in zero_octet_ips:
        outfile1.write(ip + '\n')


with open('other_ips.txt', 'w') as outfile2:
    for ip in other_ips:
        outfile2.write(ip + '\n')


count_zero_octet = len(zero_octet_ips)
count_other = len(other_ips)


print(f"Количество строк с нулевым четвертым октетом: {count_zero_octet}")
print(f"Количество остальных строк: {count_other}")
