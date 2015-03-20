#!/usr/bin/python
#################
### CSF Monitor Script
######################

# Test String
# "123.255.248.243" "*" "1" "inout" "1" "(sshd) Failed SSH login from 123.255.248.243 (IN/India/-): 5 in the last 3600 secs" "Mar 20 06:48:26 alpha sshd[12175]: Did not receive identification string from 123.255.248.243\nMar 20 06:52:56 alpha sshd[12233]: Invalid user mafish from 123.255.248.243\nMar 20 06:56:09 alpha sshd[12322]: Invalid user doctor from 123.255.248.243\nMar 20 06:57:35 alpha sshd[12336]: Invalid user virus from 123.255.248.243\nMar 20 06:59:01 alpha sshd[12347]: Invalid user windows from 123.255.248.243\n" "LF_SSHD"

#############################
########### Includes ########
#############################
import sys
import MySQLdb


#############################
####### Definitions  ########
#############################


#############################
######## Main ###############
#############################
###########
### Vars ##
###########
dbsrvr = "localhost"                                                           #Server DB address
dbuser = "your_user"                                                              #User with privlages
dbpw = "password"
dbmain = "database"                                                            #Working DB
dbtable = "queue" 
argCount = len(sys.argv) #Count # of Arguments passed
#################
##########################
 # Database Connection stuff
db = MySQLdb.connect(dbsrvr,dbuser,dbpw, dbmain )
cursor = db.cursor()

if argCount > 3: #If > 3 MUST be ban
    ##Set correct variables
    offenderIP = str(sys.argv[1]) #The IP address or CIDR being blocked
    blockedPort = str(sys.argv[2]) #Port, comma separated list or * for all ports
    blockType = str(sys.argv[3]) #0=temporary block, 1=permanent block
    blockDirection = str(sys.argv[5]) #Direction of block: in, out or inout
    blockMsg = str(sys.argv[6]) # Message containing reason for block
    blockLogs = str(sys.argv[7]) # The logs lines that triggered the block (will have /n newline chars)
    blockTrigger = str(sys.argv[8]) # The configuration settings triggered
    #sqlall = "" #Prepare SQL Query
    #cursor.execute(sqlall) #Execute SQL Query
    #db.commit() #Commit Changes
    
else: #Must be UNBan
    ##Set correct variables
    offenderIP = str(sys.argv[1]) #The IP address or CIDR being Unblocked
    if len(sys.argv) == 3: # Only set port if it exists. 
        portsOffender = str(sys.argv[2]) #Ports being unblocked    
        
    #sqlall = "" #Prepare SQL Query
    #cursor.execute(sqlall) #Execute SQL Query
    #db.commit() #Commit Changes
