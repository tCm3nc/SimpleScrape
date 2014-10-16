__author__ = 'tCm!'

import sys
import twitter


def main():
    consumer_key = "INSERT_CONSUMER_KEY_HERE"
    consumer_secret = "INSERT_CONSUMER_SECRET_HERE"
    access_token = "INSERT_ACCESS_TOKEN_HERE"
    access_token_secret = "INSERT_ACCESS_TOKEN_SECRET_HERE"

    api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)
    try:
        search = api.GetSearch("Yosemite", None, None, None, None, 200, None, None, "mixed", None)
        # print[s.Status for s in status]
        print "Found %d entries" % search.__len__()
        for s in search:
            print s.text
            if (s.text.find("Installed") != -1) \
                    | (s.text.find("installed") != -1) \
                    | (s.text.find("Downloaded") != -1) \
                    | (s.text.find("download") != -1) \
                    | (s.text.find("GB") != -1) \
                    :
                    print "---------------------------------------------------------------------------"
                    print "Found something : "
                    print s.text
                    print s.user
                    print s.source
                    print "---------------------------------------------------------------------------"
    except:
        print("Could not find details of what you wanted")
        print(sys.exc_info())

if __name__ == "__main__":
    main()