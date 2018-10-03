import os



def test_status():
    filePath = "test.log"
    status = {'INFO': 0, "WARNING": 0, "ERROR": 0}
    err = 0
    war = 0
    info = 0

    try:
        if os.path.exists(filePath) == True:
            with open(filePath,'r') as log_file:
                for line in log_file:
                    found = line.split(" ")
                    date,time,type= found[0],found[1],found[2]
                    if type == "INFO":
                        info  += 1
                    elif type == "WARNING":
                        war += 1
                    elif type == "ERROR":
                        err += 1
                    else:
                        print ("No log found",type)

            print(status)


            assert info == 50
            assert war == 110
            assert err == 3
        else:
            print ("Log file does not exist.")

    except Exception as E:
            print ("unexpected error occurred : ", E)




test_status()