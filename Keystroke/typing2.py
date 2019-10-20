# Can we read the features from the file
DEBUG = True
password = raw_input()
features = raw_input()

if DEBUG:
    print "password = {}".format(password)
    print "features = {}".format(features)
    

password = password.split(",")
password = password[:len(password)/2 + 1]
password = ''.join(password)

features = features.split(",")
features = [float(a) for a in features]
key_press = features[:len(features)/2]
key_inter = features[len(features)/2 + 1:]

if DEBUG:
    print "password = {}".format(password)
    print "features = {}".format(features)
    print "press times = {}".format(key_press)
    print "inter times = {}".format(key_inter)

def grab(password, features):
    password = password.split(",")
    password = password[:len(password)/2 + 1]
    password = ''.join(password)
    features = features.split(",")
    features = [float(a) for a in features]
    key_press = features[:len(features)/2]
    key_inter = features[len(features)/2 + 1:]

    return password, key_press, key_inter


