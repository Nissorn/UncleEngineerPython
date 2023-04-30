class Phone:
    def __init__(self,name,series):
        self.name = name
        self.series = series

    def quickShare(self): #quickshare is feature for tranfer file only on samsung
        if self.name == 'Samsung':
            print(f'transfer file complete')
        else:
            print('your devices not support quick share')
        


if __name__ == '__main__':

    samsung1 = Phone('Samsung','S23')
    samsung2 = Phone('Samsung','S22 Ultra')
    iphone = Phone('iPhone','14 Pro')

    iphone.quickShare()
    samsung1.quickShare()
    