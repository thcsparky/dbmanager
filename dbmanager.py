import os
import json

#For creating databases ntsuff

class dbjs:


    def __init__(self, dbfile1):
        self.dbjson = {}
        self.dbcount = 0
        self.dbfile = dbfile1
        try:
            f = open(self.dbfile)
            f2 = f.read()
            f.close()
            if f2.find('{') > -1 and f2.find('}') > -1:
                self.dbjson = json.loads(f2)
                self.dbcount = len(self.dbjson) -1
            else:
                self.dbjson = {}
        except Exception as ono:
            print(ono)
            print ('\n')
            self.dbjson = {}
            self.dbcount = len(self.dbjson)

    def SaveAll(self):
        fz = open(self.dbfile, 'w')
        try:
            f = json.dumps(self.dbjson)
        except:
            return('No JSON to save!')

        fz.write(f)
        return('Saved to: ' + self.dbfile)

    def Append1(self, subdict):
        self.dbcount = str(len(self.dbjson))

        self.dbjson[str(self.dbcount)] = subdict
        return('Added data into memory.\n')

    def RemKey(self, str):
        try:
            del self.dbjson[str]
            return('Deleted: ' + str)
        except:
            return('Probably nothing found')
            
    def RemAt(self, str):
        if len(self.dbjson) > 0:
            for key, value in self.dbjson:
                if value['name'] == str:
                    del (self.dbjson[key])
                    return('Success.')
            return('Nothing found.')

        else:
            return('Failure.\n')

    def Shotgun(self):
        self.dbjson = {}
        return(self.dbjson)

    def WriteContent(self, new):
    # IDEA:
        if new is dict:
            self.dbjson = new
            return('Set in memory. Warning: using a write command will replace your previous data entirely!\n')
        else:
            return('Pass a dictionary only.\n')

    def ReadCurrent(self):
        return(self.dbjson)

    def ReadAll(self):
        if len(self.dbjson) > 0:
            return(self.dbjson)
        else:
            return({})
