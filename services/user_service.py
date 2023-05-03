import json
from models.machine import Inserttable, db

def create_logic():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return '==================TABLES CREATED=================='

    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='


def insert_logic():
    data = json.load(open("data.json", 'r'))  # reading file data.json
    for i, b in enumerate('{0:016b}'.format(data['StateId'])):
        if int(b) == 1:
            example = Inserttable(machineid=data["MachineId"], stateid=data["StateId"],
                                  speed=data["Speed"], statechange=data["StateChange"],
                                  unixtime=data["UnixTime"], extras=data["Extras"],
                                  state="ON")

            db.session.add(example)
            # db.session.commit()

        else:
            example = Inserttable(machineid=data["MachineId"], stateid=data["StateId"],
                                  speed=data["Speed"], statechange=data["StateChange"],
                                  unixtime=data["UnixTime"], extras=data["Extras"],
                                  state="OFF")

            db.session.add(example)
            # db.session.commit()
    return '==================DATA INSERTED=================='
    db.session.commit()
    # db.session.close()