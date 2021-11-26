# encoding: utf-8


class DataStore:
    """
    Store of measurements and times
    """

    def __init__(self):
        self.times = []
        self.measurements = []

    def add_measurement(self, date, value):
        """
        Add the given value to the data store

        :param date: Date of the measurement
        :type date: str

        :param value: Value to add
        :type value: int or float
        """

        self.measurements.append(value)
        self.times.append(date)

    def print_measurements(self):
        """
        print the measurements and times
        """

        for time, value in zip(self.times, self.measurements):
            print(time, value)

    def get_max(self):
        """
        return the maximum measurement
        """
        
        return max(self.measurements)
    
    def get_min(self):
        """
        return the minimum measurement
        """
        
        return min(self.measurements)
    
    def get_mean(self):
        """
        return the mean of the measurements
        """
        
        return float(sum(self.measurements)) / float(len(self.measurements))


class AccumulatingStore(DataStore):
    def __init__(self):
        super().__init__()
        self.accumulation = []
        
    def add_measurement(self, date, value):
        """
        Add measurement to accumulation
        
        :param date: Date of measurement
        :param value: Measurement value
        """
        
        super().add_measurement(date, value)
        
        # set the case where this is the first measurement
        last_acc = 0
        
        # Get the last measurement if we have one
        if self.accumulation:
            last_acc = self.acc[-1]
            
            # add the accumulated value
            self.accumulation.append(last_acc + value)