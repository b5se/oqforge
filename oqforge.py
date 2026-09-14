import os
import banner
from urllib.parse import quote

def query_link(query):

    searchURL = 'https://www.google.com/search?q=' + quote(query)

    return f'\033]8;;{searchURL}\033\\{searchURL}\033]8;;\033\\'

def person_search():

    name = input('Name: ')
    location = input('Location (optional): ')
    organization = input('Organization (optional): ')
    
    print()

    print('What type of search do you want to perform?')
    print()
    print(' [1] General')
    print(' [2] Social Media')
    print(' [3] Professional')
    print(' [4] Documents')
    print(' [5] Images')
    print(' [6] All')
    print()
    
    searchType = input('Select: ')

    generalQuery = []
    socialQuery = []
    professionalQuery = []
    docQuery = []
    imageQuery = []

    if searchType == '1' or searchType == '6':

        generalQuery.append(f'"{name}"')

        if location:
            generalQuery.append(f'"{name}" "{location}"')

        if organization:
            generalQuery.append(f'"{name}" "{organization}"')

        if location and organization:
            generalQuery.append(f'"{name}" "{location}" "{organization}"')

        if searchType == '1':

            for query in generalQuery:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '6':

        socialQuery.append(f'"{name}" site:linkedin.com')
        socialQuery.append(f'"{name}" site:instagram.com')
        socialQuery.append(f'"{name}" site:facebook.com')
        socialQuery.append(f'"{name}" site:x.com')
        socialQuery.append(f'"{name}" site:reddit.com')
        socialQuery.append(f'"{name}" site:tiktok.com')
        socialQuery.append(f'"{name}" site:youtube.com')
        socialQuery.append(f'"{name}" site:github.com')
        socialQuery.append(f'"{name}" site:threads.com')
        socialQuery.append(f'"{name}" site:pinterest.com')

        if searchType == '2':

            for query in socialQuery:

                print(query)
                print(query_link(query))
                print()
        
    if searchType == '3' or searchType == '6':

        professionalQuery.append(f'"{name}" resume')
        professionalQuery.append(f'"{name}" CV')
        professionalQuery.append(f'"{name}" "professional profile"')
        professionalQuery.append(f'"{name}" "work history"')
        professionalQuery.append(f'"{name}" "employment history"')
        professionalQuery.append(f'"{name}" portfolio')
        professionalQuery.append(f'"{name}" publications')

        if searchType == '3':
        
                    for query in professionalQuery:
        
                        print(query)
                        print(query_link(query))
                        print()
        
    if searchType == '4' or searchType == '6':

        docQuery.append(f'"{name}" filetype:pdf')
        docQuery.append(f'"{name}" filetype:doc')
        docQuery.append(f'"{name}" filetype:docx')
        docQuery.append(f'"{name}" filetype:xls')
        docQuery.append(f'"{name}" filetype:xlsx')
        docQuery.append(f'"{name}" filetype:ppt')
        docQuery.append(f'"{name}" filetype:pptx')
        docQuery.append(f'"{name}" filetype:txt')
        docQuery.append(f'"{name}" filetype:csv')
        docQuery.append(f'"{name}" filetype:rtf')

        if searchType == '4':
        
                    for query in docQuery:
        
                        print(query)
                        print(query_link(query))
                        print()
        
    if searchType == '5' or searchType == '6':

        imageQuery.append(f'"{name}" images')
        imageQuery.append(f'"{name}" photo')
        imageQuery.append(f'"{name}" photograph')
        imageQuery.append(f'"{name}" picture')
        imageQuery.append(f'"{name}" portrait')
        imageQuery.append(f'"{name}" headshot')
        imageQuery.append(f'"{name}" profile photo')

        if searchType == '5':
        
                    for query in imageQuery:
        
                        print(query)
                        print(query_link(query))
                        print()
        
    if searchType == '6':

        allQueries = generalQuery + socialQuery + professionalQuery + docQuery + imageQuery

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def username_search():

    username = input("Username: ")

    print("What type of search do you want to perform?")
    print()
    print(' [1] General')
    print(' [2] Social Media')
    print(' [3] All')
    print()

    searchType = input("Select: ")

    generalQuery = []
    socialQuery = []

    if searchType == '1' or searchType == '3':

        generalQuery.append(f'"{username}"')

        if searchType == '1':

            for query in generalQuery:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '3':

        socialQuery.append(f'"{username}" site:linkedin.com')
        socialQuery.append(f'"{username}" site:instagram.com')
        socialQuery.append(f'"{username}" site:facebook.com')
        socialQuery.append(f'"{username}" site:x.com')
        socialQuery.append(f'"{username}" site:reddit.com')
        socialQuery.append(f'"{username}" site:tiktok.com')
        socialQuery.append(f'"{username}" site:youtube.com')
        socialQuery.append(f'"{username}" site:github.com')
        socialQuery.append(f'"{username}" site:threads.com')
        socialQuery.append(f'"{username}" site:pinterest.com')

        if searchType == '2':

            for query in socialQuery:

                print(query)
                print(query_link(query))
                print()

    if searchType == '3':

        allQueries = generalQuery + socialQuery

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def email_search():

    email = input("Email: ")

    print("What type of search do you want to perform?")
    print()
    print(" [1] General")
    print(" [2] Professional/Academic")
    print(" [3] Documents/Public Directories/Config Files")
    print(" [4] All")
    print()

    searchType = input("Select: ")

    generalQueries = []
    professionalQueries = []
    docQueries = []

    if searchType == '1' or searchType == '4':

        generalQueries.append(f'"{email}"')
        generalQueries.append(f'"{email}" site:pastebin.com')
        generalQueries.append(f'"{email}" site:ghostbin.co')
        generalQueries.append(f'"{email}" site:paste.ee')
        generalQueries.append(f'"{email}" "index of" "breach"')

        if searchType == '1':

            for query in generalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '4':

        professionalQueries.append(f'"{email}" site:linkedin.com')
        professionalQueries.append(f'"{email}" site:github.com')
        professionalQueries.append(f'"{email}" site:researchgate.net')
        professionalQueries.append(f'"{email}" site:academia.edu')

        if searchType == '2':

            for query in professionalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '3' or searchType == '4':

        docQueries.append(f'"{email}" filetype:sql')
        docQueries.append(f'"{email}" filetype:txt')
        docQueries.append(f'"{email}" filetype:env')
        docQueries.append(f'"{email}" filetype:doc')
        docQueries.append(f'"{email}" filetype:docx')
        docQueries.append(f'"{email}" filetype:xls')
        docQueries.append(f'"{email}" filetype:xlsx')
        docQueries.append(f'"{email}" filetype:ppt')
        docQueries.append(f'"{email}" filetype:pptx')
        docQueries.append(f'"{email}" filetype:csv')
        docQueries.append(f'"{email}" filetype:rtf')
        docQueries.append(f'"{email}" intitle:"index of" "users"')

        if searchType == '3':

            for query in docQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '4':

        allQueries = generalQueries + professionalQueries + docQueries

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def phone_number_search():

    phoneNumber = input("Phone Number: ")

    print("What type of search do you want to perform?")
    print()
    print(" [1] General")
    print(" [2] Social Media")
    print(" [3] Public Records/Directories")
    print(" [4] All")
    print()

    searchType = input("Select: ")

    generalQueries = []
    socialQueries = []
    directoryQueries = []

    if searchType == '1' or searchType == '4':

        generalQueries.append(f'"{phoneNumber}"')
        generalQueries.append(f'"{phoneNumber}" reverse phone lookup')
        generalQueries.append(f'"{phoneNumber}"')
        generalQueries.append(f'"{phoneNumber}" "contact"')
        generalQueries.append(f'"{phoneNumber}" "phone"')

        if searchType == '1':

            for query in generalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '4':

        socialQueries.append(f'"{phoneNumber}" site:facebook.com')
        socialQueries.append(f'"{phoneNumber}" site:instagram.com')
        socialQueries.append(f'"{phoneNumber}" site:linkedin.com')
        socialQueries.append(f'"{phoneNumber}" site:x.com')
        socialQueries.append(f'"{phoneNumber}" site:reddit.com')
        socialQueries.append(f'"{phoneNumber}" site:tiktok.com')

        if searchType == '2':

            for query in socialQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '3' or searchType == '4':

        directoryQueries.append(f'"{phoneNumber}" directory')
        directoryQueries.append(f'"{phoneNumber}" "public records"')
        directoryQueries.append(f'"{phoneNumber}" "business directory"')
        directoryQueries.append(f'"{phoneNumber}" "contact information"')

        if searchType == '3':

            for query in directoryQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '4':

        allQueries = generalQueries + socialQueries + directoryQueries

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def company_search():

    company = input("Company: ")

    print("What type of search do you want to perform?")
    print()
    print(" [1] General")
    print(" [2] Social Media")
    print(" [3] Professional")
    print(" [4] Documents")
    print(" [5] News")
    print(" [6] All")
    print()

    searchType = input("Select: ")

    generalQueries = []
    socialQueries = []
    professionalQueries = []
    docQueries = []
    newsQueries = []

    if searchType == '1' or searchType == '6':

        generalQueries.append(f'"{company}"')
        generalQueries.append(f'"{company}" about')
        generalQueries.append(f'"{company}" contact')
        generalQueries.append(f'"{company}" headquarters')
        generalQueries.append(f'"{company}" employees')

        if searchType == '1':

            for query in generalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '6':

        socialQueries.append(f'"{company}" site:linkedin.com')
        socialQueries.append(f'"{company}" site:facebook.com')
        socialQueries.append(f'"{company}" site:instagram.com')
        socialQueries.append(f'"{company}" site:x.com')
        socialQueries.append(f'"{company}" site:youtube.com')
        socialQueries.append(f'"{company}" site:reddit.com')

        if searchType == '2':

            for query in socialQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '3' or searchType == '6':

        professionalQueries.append(f'"{company}" employees')
        professionalQueries.append(f'"{company}" leadership')
        professionalQueries.append(f'"{company}" executives')
        professionalQueries.append(f'"{company}" careers')
        professionalQueries.append(f'"{company}" jobs')
        professionalQueries.append(f'"{company}" "work history"')

        if searchType == '3':

            for query in professionalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '4' or searchType == '6':

        docQueries.append(f'"{company}" filetype:pdf')
        docQueries.append(f'"{company}" filetype:doc')
        docQueries.append(f'"{company}" filetype:docx')
        docQueries.append(f'"{company}" filetype:xls')
        docQueries.append(f'"{company}" filetype:xlsx')
        docQueries.append(f'"{company}" filetype:ppt')
        docQueries.append(f'"{company}" filetype:pptx')
        docQueries.append(f'"{company}" filetype:csv')

        if searchType == '4':

            for query in docQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '5' or searchType == '6':

        newsQueries.append(f'"{company}" news')
        newsQueries.append(f'"{company}" announcement')
        newsQueries.append(f'"{company}" acquisition')
        newsQueries.append(f'"{company}" lawsuit')
        newsQueries.append(f'"{company}" partnership')

        if searchType == '5':

            for query in newsQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '6':

        allQueries = generalQueries + socialQueries + professionalQueries + docQueries + newsQueries

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def domain_search():

    domain = input("Domain: ")

    print("What type of search do you want to perform?")
    print()
    print(" [1] General")
    print(" [2] Subdomains")
    print(" [3] Documents")
    print(" [4] Technology/Infrastructure")
    print(" [5] All")
    print()

    searchType = input("Select: ")

    generalQueries = []
    subdomainQueries = []
    docQueries = []
    technologyQueries = []

    if searchType == '1' or searchType == '5':

        generalQueries.append(f'site:{domain}')
        generalQueries.append(f'site:{domain} "contact"')
        generalQueries.append(f'site:{domain} "about"')
        generalQueries.append(f'site:{domain} "login"')
        generalQueries.append(f'site:{domain} "admin"')

        if searchType == '1':

            for query in generalQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '2' or searchType == '5':

        subdomainQueries.append(f'site:*.{domain}')
        subdomainQueries.append(f'site:{domain} -www')
        subdomainQueries.append(f'site:dev.{domain}')
        subdomainQueries.append(f'site:staging.{domain}')
        subdomainQueries.append(f'site:test.{domain}')

        if searchType == '2':

            for query in subdomainQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '3' or searchType == '5':

        docQueries.append(f'site:{domain} filetype:pdf')
        docQueries.append(f'site:{domain} filetype:doc')
        docQueries.append(f'site:{domain} filetype:docx')
        docQueries.append(f'site:{domain} filetype:xls')
        docQueries.append(f'site:{domain} filetype:xlsx')
        docQueries.append(f'site:{domain} filetype:ppt')
        docQueries.append(f'site:{domain} filetype:pptx')
        docQueries.append(f'site:{domain} filetype:csv')
        docQueries.append(f'site:{domain} filetype:txt')

        if searchType == '3':

            for query in docQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '4' or searchType == '5':

        technologyQueries.append(f'site:{domain} "powered by"')
        technologyQueries.append(f'site:{domain} "server"')
        technologyQueries.append(f'site:{domain} "Apache"')
        technologyQueries.append(f'site:{domain} "nginx"')
        technologyQueries.append(f'site:{domain} "WordPress"')

        if searchType == '4':

            for query in technologyQueries:

                print(query)
                print(query_link(query))
                print()

    if searchType == '5':

        allQueries = generalQueries + subdomainQueries + docQueries + technologyQueries

        for query in allQueries:

            print(query)
            print(query_link(query))
            print()

def custom_search():

    pass

while True:

    print()
    banner.print_banner()

    print(' [1]  Person')
    print(' [2]  Username')
    print(' [3]  Email')
    print(' [4]  Phone Number')
    print(' [5]  Company')
    print(' [6]  Domain')
    print(' [7]  Custom Search')
    print(' [0]  Exit')
    print()

    searchChoice = input('Select: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if searchChoice == '1':
        person_search()
    elif searchChoice == '2':
        username_search()
    elif searchChoice == '3':
        email_search()
    elif searchChoice == '4':
        phone_number_search()
    elif searchChoice == '5':
        company_search()
    elif searchChoice == '6':
        domain_search()
    elif searchChoice == '7':
        custom_search()
    elif searchChoice == '0':
        print('Exiting OQForge...')
        break
    else:
        print('Invalid choice')