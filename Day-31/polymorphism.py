class Hotstar:
    def __init__(self,name):
        print(f'welcome to hotstar:{name}')
    def login(self):
        print('login')
    def dashboard(self):
        print('dashboard')
    def search(self):
        print('search')
    def playpause(self):
        print('pause,replay,resume,forward')
    def history(self):
        print('recent videos')
    def ads(self):
        print('ads running')
    def access(self):
        print('limited access')
    def download(self):
        print('unable to download')

class Premium(Hotstar):
    def __init__(self,name):
        print(f'welcome to hotstar Premium:{name}')
    def ads(self):
        print('no ads')
    def access(self):
        print('unlimited access')
    def download(self):
        print('can download')

dheeraj=Hotstar('dheeraj')
dheeraj.login()
dheeraj.dashboard()
dheeraj.search()
dheeraj.playpause()
dheeraj.history()
dheeraj.ads()
dheeraj.access()
dheeraj.download()

dheeru=Premium('dheeraj')
dheeru.login()
dheeru.dashboard()
dheeru.search()
dheeru.playpause()
dheeru.history()
dheeru.ads()
dheeru.access()
dheeru.download()