#Used to pass control to another statement if we cannot do much work on a block of code at a time but want to keep the block of code for future use
#Used to pass control to a null statement
print('\n#using pass statement in a loop')
n=10
for i in range(n):
    #pass can be used as a placeholder(storage) when code is to be added later
    pass

def get_db_secrets():
    #have not got DB details and aws secret id at the moment
    pass
print('All the other statements will be executed normally')