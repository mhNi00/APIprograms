import requests
import json
check = 'y'
print("Give me a domain name and i'll give you the information you need!")
x = input("Write the domain name here...")
p = {'key':'DEBNKSEM8P9IHLTAC5KW3BCWTPB7KTZA','domain':x}
response = requests.get("https://api.ip2whois.com/v1", p)
while check == 'y':
    print("Here is the information you can get:")
    print("""domain | Domain name. 
    domain_id |	Domain name ID.
    status 	|		Domain name status.
    create_date 	|	 	Domain name creation date.
    update_date 	|	 	Domain name updated date.
    expire_date 	|	 	Domain name expiration date.
    domain_age 	|	 	Domain name age in day(s).
    whois_server 	|	 	WHOIS server name.
    registrar
        iana_id 	|	 	Registrar IANA ID.
        name 	|	 	Registrar name.
        url 	|	 	Registrar URL.
    registrant
        name 	|	 	Registrant name.
        organization 	|	 	Registrant organization.
        street_address 	|	 	Registrant street address.
        city 	|	 	Registrant city.
        region 	|	 	Registrant region.
        zip_code 	|	 	Registrant ZIP Code.
        country 	|	 	Registrant country.
        phone 	|	 	Registrant phone number.
        fax 	|	 	Registrant fax number.
        email 	|	 	Registrant email address.
    admin
        name 	|	 	Admin name.
        organization 	|	 	Admin organization.
        street_address 	|	 	Admin street address.
        city 	|	 	Admin city.
        region 	|	 	Admin region.
        zip_code 	|	 	Admin ZIP Code.
        country 	|	 	Admin country.
        phone 	|	 	Admin phone number.
        fax 	|	 	Admin fax number.
        email 	|	 	Admin email address.
    tech
        name 	|	 	Tech name.
        organization 	|	 	Tech organization.
        street_address 	|	 	Tech street address.
        city 	|	 	Tech city.
        region 	|	 	Tech region.
        zip_code 	|	 	Tech ZIP Code.
        country 	|	 	Tech country.
        phone 	|	 	Tech phone number.
        fax 	|	 	Tech fax number.
        email 	|	 	Tech email address.
    billing
        name 	|	 	Billing name.
        organization 	|	 	Billing organization.
        street_address 	|	 	Billing street address.
        city 	|	 	Billing city.
        region 	|	 	Billing region.
        zip_code 	|	 	Billing ZIP Code.
        country 	|	 	Billing country.
        phone 	|	 	Billing phone number.
        fax 	|	 	Billing fax number.
        email 	|	 	Billing email address.
    name_servers 	|	 	Name servers
    error_code 	|	 	Error code in this query.
    error_message 	|	 	More information about the error of this query. """)
    y = input()
    if y in ['billing', 'tech', 'admin', 'registrant', 'admin']:
        y = response.json()[y][input()]
    else:
        y = response.json()[y]
    if y == "":
        print("Unfortunately, there is no information on the subject.")
    else:
        print(y)
    print("Do you want to extract more information ? Press y if you do or x if you want to quit.")
    check = input()

