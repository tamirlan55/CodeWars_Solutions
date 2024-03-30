# https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/python

'''In this kata we are going to mimic a software versioning system.

You have to implement a VersionManager class.

It should accept an optional parameter that represents the initial version. 
The input will be in one of the following formats: "{MAJOR}", "{MAJOR}.{MINOR}", 
or "{MAJOR}.{MINOR}.{PATCH}". More values may be provided after PATCH but they should be ignored. 
If these 3 parts are not decimal values, an exception with the message 
"Error occured while parsing version!" should be thrown. 
If the initial version is not provided or is an empty string, use "0.0.1" by default.

This class should support the following methods, all of which should be chainable (except release):

major() - increase MAJOR by 1, set MINOR and PATCH to 0
minor() - increase MINOR by 1, set PATCH to 0
patch() - increase PATCH by 1
rollback() - return the MAJOR, MINOR, and PATCH to their values before the previous 
major/minor/patch call, or throw an exception with the message "Cannot rollback!" 
if there's no version to roll back to. Multiple calls to rollback() 
should be possible and restore the version history
release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
May the binary force be with you!
'''

class NonExistingElementError(Exception):
    '''Срабатывает, когда в списке хранящем прошлые версии не осталось элементов'''
    pass

class VersionManager:
    '''Класс менеджер версий'''
    def __init__(self, version: str = '0.0.1'):
        self.version = version
        self.version_back = []

        arr = self.version.split('.')
        if self.version == '':
            self.version = '0.0.1'
        elif len(arr) < 3:
            arr.append('0')
            arr.append('0')
            arr = arr[0:3]
            self.version = '.'.join(arr)
        elif len(arr) > 3:
            arr = arr[0:3]
            self.version = '.'.join(arr)



    def major(self):
        '''Функция изменения версии'''
        self.version_back.append(self.version)
        arr = self.version.split('.')
        arr[0] = str(int(arr[0]) + 1)
        arr[1] = '0'
        arr[2] = '0'
        self.version = '.'.join(arr)
        return self

    def minor(self):
        '''Функция изменения версий'''
        print(f'hello {self.version}')
        self.version_back.append(self.version)
        arr = self.version.split('.')
        arr[1] = str(int(arr[1]) + 1)
        arr[2] = '0'
        self.version = '.'.join(arr)
        return self

    def patch(self):
        '''Функция изменения версий'''
        self.version_back.append(self.version)
        arr = self.version.split('.')
        arr[2] = str(int(arr[2]) + 1)
        self.version = '.'.join(arr)
        return self

    def rollback(self):
        '''Фнкция возвращающая предыдущую версию'''
        if len(self.version_back) == 0:
            raise NonExistingElementError('Cannot rollback!')
        self.version = self.version_back[-1]
        self.version_back.pop()

    def release(self):
        '''Функция возвращающая текущую версию'''
        return self.version

    
if __name__ == '__main__':

    wc3 = VersionManager('12.4.1.3.5')

    wc3.minor().minor()
    print(wc3.version)
