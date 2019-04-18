import urllib.request as req
import urllib.error as err
import json , sys
#for non US restaurants
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf_16', buffering=1)
#?? some Mehran Restaurant & Catering,Banyan Tree is missing fixed?

def printRestaurents(data) :
    for rest in json.load(data)['results'] :
        print(F"{rest['name']},{rest['rating']},{rest['vicinity']}")
#check google api ?? entries here
            
def main() :
    url = "https://geoip-db.com/json"
    ipData= json.load(req.urlopen(url))
    lat = str(ipData['latitude'])
    lon = str(ipData['longitude'])
    urlData = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+lon+'&radius=20000&type=restaurant&keyword=cruise&key=AIzaSyAEChEu64NfjSt4xPK79gTJFyPI_20EpR0'
    
    try:
        #to open url
        data = req.urlopen(urlData)
    except err.HTTPError as exp :
        print(F'HTTPError :{exp.code}')
    except err.URLError as exp :
        print(F'URLError :{exp.reason}')
    else:
        printRestaurents(data)
    
if __name__ == '__main__' :
    main()