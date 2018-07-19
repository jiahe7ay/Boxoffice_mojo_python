'''
@author=7aY
@verison=
@Todo()
@since:

'''
class Moon:
    '''


    '''
    def __init__(self):
        pass
    def str2date(self,str,function=1):
        '''
        传入str字符串，将字符串转换成 数字的月份
        :param str:
        :return:
        '''
        if function==1:
            if str==' Jan':
                str='1'
            elif str=='Feb':
                str='2'
            elif str =='Mar':
                str='3'
            elif str =='Apr':
                str='4'
            elif str =='May':
                str='5'
            elif str =='Jun':
                str='6'
            elif str=='Jul':
                str='7'
            elif str=='Aug':
                str='8'
            elif str=='Sept':
                str='9'
            elif str=='Oct':
                str='10'
            elif str =='Nov':
                str='11'
            else:
                str='12'
            return str

        elif function==2:
            if str=='JANUARY':
                str='1'
            elif str=='FEBRUARY':
                str='2'
            elif str =='MARCH':
                str='3'
            elif str =='APRIL':
                str='4'
            elif str =='MAY':
                str='5'
            elif str =='JUNE':
                str='6'
            elif str=='JULY':
                str='7'
            elif str=='AUGUST':
                str='8'
            elif str=='SEPTEMBER':
                str='9'
            elif str=='OCTOBER':
                str='10'
            elif str =='NOVEMBER':
                str='11'
            elif str =='DECEMBER':
                str='12'
            return str

