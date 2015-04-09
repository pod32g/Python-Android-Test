'''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import json
import urllib2, cStringIO, urllib
import os


def makeDir(dir_str):
        if not os.path.exists(dir_str):
            os.makedirs(dir_str)

def call():
    data = urllib.urlopen('http://donmai.us/posts.json')
    response = json.load(data)

    return response

def getNames(data, f):
    l = []   
    for d in data:
        try:
            if not f:
                if d['rating'] == 's':
                    l.append(d['file_url'].split('/')[2])
                pass
            else:
                l.append(d['file_url'].split('/')[2])
            pass
        except Exception, e:
            print e
            pass
        '''
        if d['rating'] == 'q':
            try:
                l.append(d['file_url'].split('/')[2])
                pass
            except Exception, e:
                print e
                pass
        pass
        '''
    return l


def getImages(data, f):
    l = []   
    for d in data:
        try:
            if not f:
                if d['rating'] == 's':
                    l.append("http://donmai.us" + d['file_url'])
                pass
            else:
                print "zukulento"
                l.append("http://donmai.us" + d['file_url'])
        except Exception, e:
            pass
        '''
        if d['rating'] == 'q':
            try:
                l.append("http://donmai.us" + d['file_url'])
            except Exception, e:
                pass
        pass
        '''
    return l

def saveImages():
    images_dir = 'images'
    zukulento = False
    makeDir(images_dir)
    current_json = call()
    url_list = getImages(current_json, zukulento)
    name_list = getNames(current_json, zukulento)

    m = len(name_list)
    i = 0

    for x in url_list:
        urllib.urlretrieve(x, images_dir + '/' + name_list[i])
        i += 1
    pass




        