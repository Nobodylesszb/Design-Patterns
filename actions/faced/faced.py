from alert import AlarmSensor,WaterSprinker,EmergencyDialer

class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()

if __name__=="__main__":
    emergency_facade=EmergencyFacade()
    emergency_facade.runAll()

"""
output:
Alarm Ring...
Spray Water...
Dial 119...

"""